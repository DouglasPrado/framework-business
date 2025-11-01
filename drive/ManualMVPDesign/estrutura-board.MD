# Estrutura do Board / Planilha do MVP Manual

## Informações Gerais

- Ferramenta: Google Sheets (aprovada em tools como solução de planilhas)
- Link do board/planilha: `drive/manual-mvp/controle-diario-varejo.xlsx` (pasta compartilhada com permissões de edição para equipe)
- Owner pela manutenção: Ana Souza
- Frequência de revisão: Reunião rápida diária às 17h e revisão estendida às segundas-feiras às 9h

## Colunas / Campos Obrigatórios

1. `Cliente` – Nome ou identificador
2. `Oferta` – Produto/serviço adquirido (Controle Diário de Caixa Manual)
3. `Status` – Recebido / Onboarding / Produção / QA / Entrega / Follow-up / Concluído
4. `Responsável atual`
5. `Data de entrada`
6. `SLA previsto`
7. `Data limite da etapa corrente`
8. `Tempo gasto (hh:mm)` – atualize ao avançar de etapa
9. `Notas / Pendências`
10. `Prioridade` (Alta, Média, Baixa)

Campos adicionais (opcionais):
- `Canal de origem`
- `Ticket previsto`
- `Envios do cliente (status)`
- `Feedback recebido`

## Convenções de Uso

- Atualize `Status` imediatamente após concluir a etapa e registre comentários objetivos usando linguagem validada das entrevistas (ex: "segurar compra de frios").
- Utilize `Tempo gasto` com base nos registros cronometrados; se a etapa exceder 20% do planejado, adicionar etiqueta `Gargalo`.
- Documentos e links devem apontar para a pasta do cliente dentro de `drive/manual-mvp/clientes/{nome}` com subpastas para relatórios, evidências e feedbacks.
- Exceções devem ser marcadas com a tag `Exceção` no campo de notas, detalhadas no backlog semanal.
- Haverá dois horários fixos de atualização (10h e 17h); caso ocorra envio fora da janela, registrar observação e reagendar bloco de produção.

## Visões Recomendadas

- **Pipeline Geral:** todas as cards por status, ordenados por SLA previsto.
- **SLA em risco:** filtro onde `Data limite da etapa` ≤ 24h ou card está há mais de 1 dia útil no mesmo status.
- **Backlog de melhorias:** cards com tag `Exceção` ou `Melhoria` para revisão na retrospectiva semanal.
- **Agenda da semana:** cards com entregas programadas nos próximos 7 dias e respectivos responsáveis.

## Checklist de Configuração

- [x] Colunas criadas e formatadas (validação de dados para Status, Prioridade e Responsável)
- [x] Exemplos preenchidos (card "Mercearia São Lucas" com histórico completo)
- [x] Permissões concedidas a todos os operadores e stakeholder decisor
- [ ] Links para templates e checklists adicionados nas notas ou colunas dedicadas (em andamento, finalização até 06/11)
- [ ] Instruções de uso compartilhadas com a equipe (agendar treinamento em 06/11)

## Rotina de Manutenção

- Segunda-feira: Revisar pipeline completo, alinhar prioridades e atualizar previsão de capacidade.
- Terça a sexta: Registrar avanço após bloco de produção matinal (10h) e vespertino (17h), sinalizar bloqueios no Slack interno.
- Quarta-feira: Consolidar aprendizados parciais para discussão no follow-up com stakeholder.
- Sexta-feira: Exportar dados da semana (tempo por etapa, exceções, satisfação) e arquivar cards concluídos.
- Mensal (ou após cada ciclo piloto): Atualizar indicadores agregados e revisar necessidade de automação.
