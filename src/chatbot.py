"""
GoodWe EV ChargeOps Assistant — Chatbot Sprint 2
Autores: Brenno Gomes (RM 570525), Eduardo Moreira (RM 569923),
         Enzo Stahal (RM 569001), Matheus Bruno (RM 572944)

Funcionalidades:
  - System prompt com contexto GoodWe EV Challenge 2026
  - Histórico de mensagens (memória de contexto)
  - Few-shot prompting embutido
  - Interface de chat via terminal
"""

import os
import json
from datetime import datetime
from openai import OpenAI

#  Configuração da API
# Nunca exponha a chave diretamente no código.

def get_client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "Variável de ambiente OPENAI_API_KEY não encontrada.\n"
            "Configure com: export OPENAI_API_KEY='sua-chave'\n"
            "No Colab: use a aba Secrets (🔑) e chame userdata.get('OPENAI_API_KEY')"
        )
    return OpenAI(api_key=api_key)


# System Prompt (contexto GoodWe)
SYSTEM_PROMPT = """
Você é o GoodWe EV ChargeOps Assistant, um assistente operacional inteligente
desenvolvido para o EV Challenge 2026 da GoodWe Brazil.

## SEU PAPEL
Você auxilia síndicos, administradoras de condomínio, moradores e técnicos de
manutenção a gerenciar eletropostos e sessões de recarga de veículos elétricos
em condomínios residenciais equipados com carregadores GoodWe.

## CONTEXTO DO PROBLEMA (EV Challenge 2026)
A GoodWe identificou que condomínios com múltiplos carregadores compartilhados
enfrentam os seguintes desafios:
1. Falta de orquestração de potência entre recargas simultâneas (risco de sobrecarga)
2. Ausência de registro automático de sessões de recarga (kWh, duração, custo)
3. Inexistência de relatórios e faturamento automatizado por morador
4. Dificuldade de comunicação entre moradores e síndico sobre uso e custos
5. Falta de diagnóstico remoto de falhas nos carregadores

## SUAS COMPETÊNCIAS
Você pode auxiliar com:
- **Gestão de sessões**: iniciar, pausar, encerrar e registrar sessões de recarga
- **Orquestração de potência**: regras de balanceamento entre carregadores simultâneos
- **Relatórios**: consumo por morador, custo por período, histórico de recargas
- **Faturamento**: cálculo de custos baseado em kWh consumido e tarifa vigente
- **Regras do condomínio**: horários permitidos, limites de uso, agendamentos
- **Diagnóstico de falhas**: identificar e orientar sobre erros comuns dos carregadores GoodWe
- **Dúvidas técnicas**: especificações dos carregadores GoodWe (séries ESAC, EV chargers)

## PERSONAS QUE VOCÊ ATENDE
- **Síndico/Administrador**: gestão completa, relatórios, cobranças, configuração de regras
- **Morador/Usuário**: consulta de consumo próprio, agendamento, dúvidas de uso
- **Técnico de manutenção**: diagnóstico, erros, especificações técnicas

## COMPORTAMENTO ESPERADO
- Responda sempre em português do Brasil
- Seja objetivo e direto, mas acolhedor
- Para solicitações fora do escopo, redirecione gentilmente ao tema de eletropostos/GoodWe
- Quando não souber algo específico, indique que o usuário consulte o manual técnico GoodWe ou o suporte oficial
- Use linguagem adequada ao perfil: técnica para técnicos, simples para moradores

## EXEMPLOS DE INTERAÇÃO (few-shot)

Usuário: "Quantos kWh o apartamento 42 consumiu em abril?"
Assistente: "Para consultar o consumo do apartamento 42 em abril, acesse o painel administrativo em Relatórios > Consumo por Unidade > selecione Abril. O sistema exibirá o total de kWh consumidos, custo calculado e número de sessões realizadas. Posso explicar como exportar esse relatório em PDF ou Excel?"

Usuário: "O carregador está mostrando erro E04, o que faço?"
Assistente: "O erro E04 nos carregadores GoodWe indica falha de comunicação com a rede (timeout de conexão). Passos para resolver: (1) Verifique se o cabo de rede/Wi-Fi do carregador está conectado; (2) Reinicie o carregador pelo botão traseiro por 10 segundos; (3) Aguarde 2 minutos para reconexão automática. Se o erro persistir, registre um chamado técnico com o código E04 e o número de série do equipamento."

Usuário: "Como configurar o limite de potência para 3 carregadores simultâneos?"
Assistente: "Para configurar o balanceamento de potência entre 3 carregadores simultâneos, acesse: Configurações > Gerenciamento de Carga > Modo Compartilhado. Defina a potência total disponível do quadro (ex: 22 kW) e o sistema distribuirá automaticamente entre os carregadores ativos. Recomendo usar o modo 'Equalizado' para distribuição igualitária ou 'Prioridade' se algum morador tiver prioridade especificada em convenção."
"""

# Classe principal do Chatbot 

class GoodWeChargeBot:
    """
    Chatbot GoodWe EV ChargeOps com memória de contexto (histórico completo)
    e few-shot prompting embutido no system prompt.
    """

    MODEL = "gpt-4o-mini"           # Custo-benefício excelente para o escopo
    MAX_TOKENS = 1024
    TEMPERATURE = 0.4               # Mais focado/determinístico para respostas técnicas

    def __init__(self):
        self.client = get_client()
        self.conversation_history: list[dict] = []
        self.session_start = datetime.now().isoformat()
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    def _build_messages(self) -> list[dict]:
        """Monta a lista completa de mensagens para a API (system + histórico)."""
        return [{"role": "system", "content": SYSTEM_PROMPT}] + self.conversation_history

    def send_message(self, user_message: str) -> str:
        """
        Envia uma mensagem do usuário e retorna a resposta do assistente.
        Mantém o histórico completo para memória de contexto.
        """
        # Adiciona mensagem do usuário ao histórico
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Chama a API com o histórico completo
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=self._build_messages(),
            max_tokens=self.MAX_TOKENS,
            temperature=self.TEMPERATURE,
        )

        assistant_message = response.choices[0].message.content

        # Adiciona resposta do assistente ao histórico
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def reset_conversation(self):
        """Limpa o histórico para iniciar nova conversa."""
        self.conversation_history = []
        print("\n[Histórico limpo. Nova conversa iniciada.]\n")

    def export_session(self, filepath: str = None):
        """Exporta o histórico da sessão em JSON para fins de log/auditoria."""
        if filepath is None:
            filepath = f"session_{self.session_id}.json"
        session_data = {
            "session_id": self.session_id,
            "session_start": self.session_start,
            "session_end": datetime.now().isoformat(),
            "model": self.MODEL,
            "turns": len(self.conversation_history) // 2,
            "history": self.conversation_history
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
        print(f"[Sessão exportada para: {filepath}]")
        return filepath

    def get_stats(self) -> dict:
        """Retorna estatísticas básicas da sessão atual."""
        return {
            "turns": len(self.conversation_history) // 2,
            "model": self.MODEL,
            "session_id": self.session_id,
        }


#  Interface de terminal 

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║        GoodWe EV ChargeOps Assistant — Sprint 2             ║
║        EV Challenge 2026 | Powered by OpenAI GPT-4o-mini    ║
╠══════════════════════════════════════════════════════════════╣
║  Comandos:                                                   ║
║   /reset   → limpa o histórico da conversa                  ║
║   /export  → exporta a sessão em JSON                       ║
║   /stats   → exibe estatísticas da sessão                   ║
║   /sair    → encerra o chatbot                              ║
╚══════════════════════════════════════════════════════════════╝
"""

def run_terminal_chat():
    """Loop principal de chat via terminal."""
    print(BANNER)

    try:
        bot = GoodWeChargeBot()
    except EnvironmentError as e:
        print(f"\n❌ ERRO DE CONFIGURAÇÃO:\n{e}\n")
        return

    print("✅ Chatbot inicializado. Como posso ajudar?\n")

    while True:
        try:
            user_input = input("Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nEncerrando chatbot...")
            break

        if not user_input:
            continue

        # Comandos especiais
        if user_input.lower() == "/sair":
            print("Até logo! 👋")
            break
        elif user_input.lower() == "/reset":
            bot.reset_conversation()
            continue
        elif user_input.lower() == "/export":
            bot.export_session()
            continue
        elif user_input.lower() == "/stats":
            stats = bot.get_stats()
            print(f"\n[Stats] Turnos: {stats['turns']} | Modelo: {stats['model']} | Sessão: {stats['session_id']}\n")
            continue

        # Envio da mensagem
        print("\nAssistente: ", end="", flush=True)
        try:
            response = bot.send_message(user_input)
            print(response)
        except Exception as e:
            print(f"\n❌ Erro ao chamar a API: {e}")
        print()


if __name__ == "__main__":
    run_terminal_chat()
