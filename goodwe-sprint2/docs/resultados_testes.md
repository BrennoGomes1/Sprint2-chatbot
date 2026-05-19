# Resultados dos Testes — Sprint 2
**GoodWe EV ChargeOps Assistant | EV Challenge 2026**

Data de execução: 19/05/2026  
Modelo utilizado: `gpt-4o-mini` | Temperature: `0.4` | Max tokens: `1024`

---

## Caso de Teste 1 — Consulta de Consumo (Persona: Morador)

**Pergunta enviada:**
> Como posso verificar o consumo de energia do meu apartamento no mês passado?

**Resposta obtida:**
> Para verificar o consumo de energia do seu apartamento no mês passado, siga estas etapas:
>
> 1. **Acesse o aplicativo ou painel web GoodWe EV ChargeOps** com seu login de morador.
> 2. Navegue até **Meu Consumo > Histórico de Recargas**.
> 3. Filtre pelo mês desejado usando o seletor de período.
> 4. O sistema exibirá o total de **kWh consumidos**, o **custo estimado** com base na tarifa configurada e o **número de sessões** realizadas.
>
> Se não tiver acesso ao aplicativo, solicite ao síndico um extrato mensal — ele pode gerar e exportar o relatório pelo painel administrativo.

**Resposta esperada (critério Sprint 1):** Orientar o morador a acessar o painel ou aplicativo, indicar onde encontrar o histórico de consumo por período, e mencionar métricas como kWh e custo.

**✅ Avaliação: ADEQUADA**

*Justificativa: A resposta cobriu todos os critérios — indicou o caminho de navegação, mencionou as métricas esperadas (kWh, custo, sessões) e ofereceu alternativa via síndico.*

---

## Caso de Teste 2 — Orquestração de Potência / Sobrecarga (Persona: Síndico)

**Pergunta enviada:**
> Três moradores estão carregando ao mesmo tempo e a energia do condomínio caiu. O que aconteceu e como posso evitar que isso se repita?

**Resposta obtida:**
> O que ocorreu foi uma **sobrecarga elétrica** causada pela demanda simultânea dos três carregadores sem gerenciamento de potência ativo.
>
> Cada carregador GoodWe pode demandar entre 7,4 kW (monofásico) e 22 kW (trifásico), e sem orquestração, a soma ultrapassa o limite do quadro elétrico do condomínio.
>
> **Para evitar que isso se repita:**
>
> 1. Acesse **Configurações > Gerenciamento de Carga Compartilhada** no painel administrativo.
> 2. Informe a **potência total disponível** do quadro (ex: 30 kW).
> 3. Ative o **Modo de Balanceamento Dinâmico**: o sistema distribuirá automaticamente a potência disponível entre os carregadores ativos.
> 4. Opcionalmente, defina **limites individuais por unidade** para evitar que um morador monopolize a carga disponível.
>
> Recomendo também revisar o dimensionamento elétrico com um eletricista para garantir que o quadro suporte a demanda máxima do condomínio.

**Resposta esperada:** Explicar o conceito de sobrecarga por recargas simultâneas, mencionar a orquestração/balanceamento de potência e como configurá-la.

**✅ Avaliação: ADEQUADA**

*Justificativa: Resposta técnica e completa. Explicou a causa, apresentou valores de potência típicos dos carregadores GoodWe e forneceu passos claros de configuração do balanceamento.*

---

## Caso de Teste 3 — Relatório e Faturamento (Persona: Síndico)

**Pergunta enviada:**
> Como gero um relatório mensal de consumo por unidade para cobrar cada morador separadamente?

**Resposta obtida:**
> Para gerar o relatório de faturamento mensal por unidade, siga os passos abaixo no painel administrativo:
>
> 1. Acesse **Relatórios > Consumo por Unidade**.
> 2. Selecione o **período** (mês/ano desejado).
> 3. O sistema exibirá uma tabela com: unidade, total de kWh, valor calculado (com base na tarifa configurada) e número de sessões.
> 4. Clique em **Exportar** para baixar em **PDF** (para envio ao morador) ou **Excel/CSV** (para integração com sistema de cobrança do condomínio).
>
> **Dica:** Configure previamente a tarifa de energia em Configurações > Tarifas para que o cálculo de custo seja automático. Se o condomínio usa horária (ponta/fora-de-ponta), o sistema aplica a tarifa correta por faixa horária.

**Resposta esperada:** Descrever como acessar relatórios, filtrar por período e unidade, e como exportar ou usar os dados para cobrança.

**✅ Avaliação: ADEQUADA**

*Justificativa: Cobriu todos os critérios com detalhe adicional sobre tarifas horárias, demonstrando profundidade técnica relevante ao contexto.*

---

## Caso de Teste 4 — Diagnóstico de Falha (Persona: Técnico)

**Pergunta enviada:**
> O carregador do box 7 está exibindo erro E04 constantemente. O que significa e como resolver?

**Resposta obtida:**
> O **erro E04** nos carregadores GoodWe indica **falha de comunicação com a rede** — o equipamento não consegue estabelecer conexão com o servidor de gerenciamento (timeout de comunicação).
>
> **Procedimento de diagnóstico e resolução:**
>
> 1. **Verifique a conectividade**: confirme se o cabo Ethernet ou a conexão Wi-Fi do carregador está ativa e com sinal adequado.
> 2. **Reinicialize o carregador**: pressione e segure o botão de reset traseiro por 10 segundos; aguarde 2 minutos para que o equipamento tente reconectar.
> 3. **Verifique o firewall/roteador**: certifique-se de que a porta 8883 (MQTT) não está bloqueada — necessária para comunicação com o servidor GoodWe.
> 4. **Teste com IP estático**: se o problema persistir, configure um IP estático no carregador via painel local (192.168.x.x) para descartar conflito de DHCP.
> 5. **Se nada funcionar**: registre um chamado técnico informando o código **E04**, o número de série do equipamento (etiqueta traseira) e o log de erros exportado pelo painel.

**Resposta esperada:** Identificar o código E04, descrever a causa e oferecer passos de resolução como verificar conexão, reiniciar e abrir chamado.

**✅ Avaliação: ADEQUADA**

*Justificativa: Resposta altamente técnica e detalhada, adequada à persona de técnico. Incluiu detalhes avançados como porta MQTT e configuração de IP estático, superando o critério mínimo.*

---

## Caso de Teste 5 — Agendamento e Tarifa (Persona: Morador)

**Pergunta enviada:**
> É possível agendar a recarga para o horário de madrugada, quando a tarifa de energia é mais barata? Como configuro isso?

**Resposta obtida:**
> Sim, é possível! Agendar a recarga para o horário de tarifa fora de ponta (geralmente das 21h30 às 17h30, conforme sua distribuidora) pode reduzir significativamente o custo de cada sessão.
>
> **Como configurar o agendamento:**
>
> 1. No aplicativo GoodWe EV, acesse **Meu Carregador > Agendamento de Recarga**.
> 2. Defina o **horário de início** (ex: 00:00) e o **horário máximo de término** (ex: 06:00).
> 3. Conecte o veículo ao carregador normalmente — a carga só iniciará no horário programado.
> 4. Ative a opção **"Parar na meta de carga"** se quiser interromper automaticamente ao atingir, por exemplo, 80% da bateria.
>
> **Dica:** Confirme com o síndico se há regra do condomínio sobre agendamentos noturnos, pois em alguns locais há controle de uso por período para evitar concentração de demanda à meia-noite.

**Resposta esperada:** Confirmar a possibilidade de agendamento, explicar como configurar horários programados, e mencionar a vantagem da tarifa fora de ponta.

**✅ Avaliação: ADEQUADA**

*Justificativa: Confirmou a funcionalidade, forneceu instruções passo a passo, mencionou a tarifa fora de ponta com horário de referência e adicionou dica contextual relevante sobre regras do condomínio.*

---

## Resumo Geral

| # | Persona | Categoria | Avaliação |
|---|---------|-----------|-----------|
| 1 | Morador | Consulta de consumo | ✅ Adequada |
| 2 | Síndico | Orquestração de potência | ✅ Adequada |
| 3 | Síndico | Relatório e faturamento | ✅ Adequada |
| 4 | Técnico | Diagnóstico de falha | ✅ Adequada |
| 5 | Morador | Agendamento e tarifa | ✅ Adequada |

**Taxa de sucesso: 5/5 (100%)**

### Observações sobre a qualidade
- O modelo demonstrou consistência no escopo do problema GoodWe
- Respostas técnicas (caso 4) apresentaram nível de detalhe acima do esperado
- O few-shot prompting no system prompt contribuiu para padronização do formato de resposta
- Temperature 0.4 manteve respostas determinísticas e focadas no contexto
- Nenhuma resposta fugiu do escopo definido (EV ChargeOps / GoodWe)

### Técnicas diferenciadas implementadas
- **Few-shot prompting**: 3 exemplos de Q&A embutidos no system prompt
- **Gerenciamento de histórico**: memória de contexto completa por sessão
- **Personas contextualizadas**: system prompt diferencia síndico, morador e técnico
- **Exportação de sessão**: log JSON automático de cada conversa
