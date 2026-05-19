#  GoodWe EV ChargeOps Assistant — Sprint 2

**EV Challenge 2026 | GoodWe Brazil**

Chatbot operacional com IA para gestão de eletropostos em condomínios, com suporte a síndicos, moradores e técnicos de manutenção.

---

##  Integrantes

| Nome | RM |
|------|----|
| Brenno Gomes | 570525 |
| Eduardo Moreira | 569923 |
| Enzo Stahal | 569001 |
| Matheus Bruno | 572944 |

---

##  Problema abordado (EV Challenge 2026)

A GoodWe identificou que condomínios com múltiplos carregadores compartilhados enfrentam:

1. Falta de orquestração de potência entre recargas simultâneas (risco de sobrecarga)
2. Ausência de registro automático de sessões (kWh, duração, custo)
3. Inexistência de relatórios e faturamento automatizado por morador
4. Dificuldade de comunicação entre moradores e síndico
5. Falta de diagnóstico remoto de falhas

---

##  Funcionalidades implementadas na Sprint 2

- ✅ **System prompt com contexto GoodWe** — modelo restrito ao escopo do EV Challenge
- ✅ **Memória de contexto** — histórico completo de mensagens por sessão
- ✅ **Few-shot prompting** — 3 exemplos Q&A embutidos no system prompt para padronizar respostas
- ✅ **Múltiplas personas** — comportamento adaptado a síndico, morador e técnico
- ✅ **Exportação de sessão** — log JSON automático da conversa
- ✅ **Interface terminal** com comandos especiais (`/reset`, `/export`, `/stats`, `/sair`)
- ✅ **Notebook Google Colab** pronto para uso

---

##  Estrutura do projeto

```
goodwe-chatbot/
├── src/
│   └── chatbot.py                          # Chatbot principal (terminal)
├── tests/
│   └── run_tests.py                        # Script de execução dos 5 casos de teste
├── docs/
│   ├── resultados_testes.md                # Resultados documentados (Sprint 2)
│   ├── perguntas_respostas.md              # Modelo de Q&A (Sprint 1)
│   └── fluxograma.mmd                      # Fluxograma do sistema (Sprint 1)
├── prompts/
│   └── system_prompt.txt                   # System prompt isolado
├── GoodWe_EV_ChargeOps_Chatbot_Sprint2.ipynb  # Notebook Google Colab
├── requirements.txt
└── README.md
```

---

##  Dependências

- Python 3.10+
- `openai >= 1.30.0`

---

##  Variáveis de ambiente

**NUNCA exponha sua API Key no código ou no repositório.**

### Terminal / IDE local

```bash
export OPENAI_API_KEY="sk-sua-chave-aqui"
```

No Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY = "sk-sua-chave-aqui"
```

### Google Colab

1. Abra o painel lateral **Secrets** (ícone 🔑)
2. Adicione um secret com nome `OPENAI_API_KEY` e o valor da sua chave
3. Execute o notebook — a chave é carregada automaticamente via `userdata.get()`

---

##  Como executar

### Opção 1 — Terminal

```bash
# 1. Clone o repositório
git clone https://github.com/BrennoGomes1/goodwe-chatbot.git
cd goodwe-chatbot

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure a API Key
export OPENAI_API_KEY="sk-sua-chave"

# 4. Execute o chatbot
python src/chatbot.py
```

### Opção 2 — Google Colab

1. Abra `GoodWe_EV_ChargeOps_Chatbot_Sprint2.ipynb` no Google Colab
2. Configure o secret `OPENAI_API_KEY` (ícone 🔑 na barra lateral)
3. Execute as células em ordem
4. Edite a variável `mensagem` na célula interativa e execute para conversar

### Comandos disponíveis no terminal

| Comando | Função |
|---------|--------|
| `/reset` | Limpa o histórico da conversa |
| `/export` | Exporta a sessão em JSON |
| `/stats` | Exibe estatísticas da sessão atual |
| `/sair` | Encerra o chatbot |

---

##  Executar os testes

```bash
python tests/run_tests.py
```

Executa os 5 casos de teste do modelo da Sprint 1 e exibe as respostas obtidas.  
Os resultados documentados com avaliação qualitativa estão em [`docs/resultados_testes.md`](docs/resultados_testes.md).

---

##  Exemplos de uso

```
Você: Três moradores estão carregando ao mesmo tempo e a energia caiu. O que aconteceu?

Assistente: O que ocorreu foi uma sobrecarga elétrica causada pela demanda simultânea
dos três carregadores sem gerenciamento de potência ativo. Cada carregador GoodWe pode
demandar entre 7,4 kW (monofásico) e 22 kW (trifásico)...
```

```
Você: O carregador do box 7 está com erro E04. O que faço?

Assistente: O erro E04 indica falha de comunicação com a rede. Passos:
1. Verifique conectividade (cabo/Wi-Fi)
2. Reinicie o carregador por 10 segundos
3. Verifique se a porta 8883 (MQTT) está liberada...
```

---

##  Técnicas implementadas

| Técnica | Descrição | Impacto |
|---------|-----------|---------|
| **System Prompt contextualizado** | Injeta o problema GoodWe e personas | Respostas dentro do escopo |
| **Few-shot prompting** | 3 exemplos Q&A no system prompt | Padroniza formato e profundidade |
| **Memória de contexto** | Histórico completo enviado em cada requisição | Diálogos contínuos e coerentes |
| **Personas diferenciadas** | Comportamento adaptado ao perfil do usuário | Respostas adequadas a cada público |

---

##  Resultados dos testes — Resumo

| # | Persona | Categoria | Avaliação |
|---|---------|-----------|-----------|
| 1 | Morador | Consulta de consumo | ✅ Adequada |
| 2 | Síndico | Orquestração de potência | ✅ Adequada |
| 3 | Síndico | Relatório e faturamento | ✅ Adequada |
| 4 | Técnico | Diagnóstico de falha | ✅ Adequada |
| 5 | Morador | Agendamento e tarifa | ✅ Adequada |

**Taxa de sucesso: 5/5 (100%)** — ver [`docs/resultados_testes.md`](docs/resultados_testes.md) para detalhes completos.

---

##  Modelo e parâmetros

| Parâmetro | Valor | Justificativa |
|-----------|-------|---------------|
| Modelo | `gpt-4o-mini` | Custo-benefício para produção, bom raciocínio técnico |
| Temperature | `0.4` | Respostas mais determinísticas e focadas |
| Max tokens | `1024` | Respostas completas sem desperdício |


## Sprint 1 (planejamento)

O planejamento completo, fluxograma e system prompt base da Sprint 1 estão disponíveis em:
- `docs/fluxograma.mmd`
- `docs/perguntas_respostas.md`
- `prompts/system_prompt.txt`
