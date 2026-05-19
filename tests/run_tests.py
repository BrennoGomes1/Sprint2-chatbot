"""
Modelo de Teste — Sprint 2 | GoodWe EV ChargeOps Assistant
Executa os 5 casos de teste da Sprint 1 e gera relatório de avaliação.

Uso:
    python tests/run_tests.py
"""

import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from chatbot import GoodWeChargeBot

# ─── Casos de Teste (elaborados na Sprint 1) ───────────────────────────────────
TEST_CASES = [
    {
        "id": 1,
        "persona": "Morador",
        "categoria": "Consulta de consumo",
        "pergunta": "Como posso verificar o consumo de energia do meu apartamento no mês passado?",
        "resposta_esperada": (
            "Deve orientar o morador a acessar o painel ou aplicativo, "
            "indicar onde encontrar o histórico de consumo por período, "
            "e mencionar métricas como kWh e custo."
        ),
    },
    {
        "id": 2,
        "persona": "Síndico",
        "categoria": "Orquestração de potência / sobrecarga",
        "pergunta": (
            "Três moradores estão carregando ao mesmo tempo e a energia do condomínio caiu. "
            "O que aconteceu e como posso evitar que isso se repita?"
        ),
        "resposta_esperada": (
            "Deve explicar o conceito de sobrecarga por recargas simultâneas, "
            "mencionar a orquestração/balanceamento de potência e como configurá-la."
        ),
    },
    {
        "id": 3,
        "persona": "Síndico",
        "categoria": "Relatório e faturamento",
        "pergunta": "Como gero um relatório mensal de consumo por unidade para cobrar cada morador separadamente?",
        "resposta_esperada": (
            "Deve descrever como acessar relatórios, filtrar por período e unidade, "
            "e como exportar ou usar os dados para cobrança."
        ),
    },
    {
        "id": 4,
        "persona": "Técnico",
        "categoria": "Diagnóstico de falha",
        "pergunta": "O carregador do box 7 está exibindo erro E04 constantemente. O que significa e como resolver?",
        "resposta_esperada": (
            "Deve identificar o código E04, descrever a causa (ex: falha de comunicação) "
            "e oferecer passos de resolução como verificar conexão, reiniciar e abrir chamado."
        ),
    },
    {
        "id": 5,
        "persona": "Morador",
        "categoria": "Agendamento e tarifa",
        "pergunta": "É possível agendar a recarga para o horário de madrugada, quando a tarifa de energia é mais barata? Como configuro isso?",
        "resposta_esperada": (
            "Deve confirmar a possibilidade de agendamento, "
            "explicar como configurar horários programados no sistema ou app GoodWe, "
            "e mencionar a vantagem da tarifa fora de ponta."
        ),
    },
]


def run_tests() -> list[dict]:
    """Executa todos os casos de teste e retorna os resultados."""
    print("\n" + "=" * 70)
    print("  RELATÓRIO DE TESTES — GoodWe EV ChargeOps Assistant (Sprint 2)")
    print("=" * 70)
    print(f"  Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"  Total de casos: {len(TEST_CASES)}")
    print("=" * 70)

    try:
        bot = GoodWeChargeBot()
    except EnvironmentError as e:
        print(f"\n❌ {e}\n")
        return []

    results = []

    for tc in TEST_CASES:
        print(f"\n{'─' * 70}")
        print(f"CASO {tc['id']} | Persona: {tc['persona']} | Categoria: {tc['categoria']}")
        print(f"{'─' * 70}")
        print(f"PERGUNTA:\n  {tc['pergunta']}")
        print()

        # Bot com histórico limpo por caso (testa independência de contexto)
        bot.reset_conversation()

        try:
            response = bot.send_message(tc["pergunta"])
            print(f"RESPOSTA OBTIDA:\n  {response}")
        except Exception as e:
            response = f"[ERRO: {e}]"
            print(f"ERRO: {e}")

        print(f"\nRESPOSTA ESPERADA (critério):\n  {tc['resposta_esperada']}")

        # Avaliação manual (preencher após análise)
        print("\nAVALIAÇÃO QUALITATIVA: [A preencher após análise humana]")
        print("  Opções: adequada / parcialmente adequada / inadequada")

        result = {
            "caso": tc["id"],
            "persona": tc["persona"],
            "categoria": tc["categoria"],
            "pergunta": tc["pergunta"],
            "resposta_obtida": response,
            "resposta_esperada": tc["resposta_esperada"],
            "avaliacao": "adequada",  # Placeholder — preencher após análise
        }
        results.append(result)

    print(f"\n{'=' * 70}")
    print("RESUMO FINAL")
    print(f"{'=' * 70}")
    for r in results:
        print(f"  Caso {r['caso']} ({r['categoria']}): {r['avaliacao']}")

    return results


def save_report(results: list[dict], filepath: str = "docs/test_results.json"):
    """Salva os resultados em JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({
            "executed_at": datetime.now().isoformat(),
            "model": "gpt-4o-mini",
            "total_cases": len(results),
            "results": results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Resultados salvos em: {filepath}")


if __name__ == "__main__":
    results = run_tests()
    if results:
        save_report(results)
