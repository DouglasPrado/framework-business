# Estrutura do Board / Planilha do MVP Manual

## Informações Gerais

- Ferramenta: (ex: Google Sheets, Notion, Trello) — confirmar aprovação em `tools/`
- Link do board/planilha:
- Owner pela manutenção:
- Frequência de revisão:

## Colunas / Campos Obrigatórios

1. `Cliente` – Nome ou identificador
2. `Oferta` – Produto/serviço adquirido
3. `Status` – Recebido / Onboarding / Produção / QA / Entrega / Follow-up / Concluído
4. `Responsável atual`
5. `Data de entrada`
6. `SLA previsto`
7. `Data limite da etapa corrente`
8. `Tempo gasto (hh:mm)` – atualize ao avançar de etapa
9. `Notas / Pendências`
10. `Prioridade` (Alta, Média, Baixa)

Campos adicionais (opcionais):
- `Segmento`
- `Ticket previsto`
- `Exceções registradas`
- `Feedback recebido`

## Convenções de Uso

- Atualize `Status` assim que concluir a etapa e registre notas relevantes.
- Utilize `Tempo gasto` com base nos registros do piloto e das execuções reais.
- Comentários ou anexos devem linkar para arquivos na pasta `_DATA/` ou outra fonte oficial.
- Quando houver exceções, marque o item com tag específica (`Exceção`) e detalhe na nota.
- Blocos diários de atualização: defina horário padrão (ex: 10h e 17h) para revisar itens em progresso.

## Visões Recomendadas

- **Pipeline Geral:** todos os itens por status, ordenados por prioridade.
- **SLA em risco:** filtro onde `Data limite da etapa` ≤ 24h ou status parado há mais de X horas.
- **Backlog de melhorias:** itens com tag `Exceção` ou `Melhoria` para discussão semanal.
- **Agenda da semana:** entregas com data limite nos próximos 7 dias.

## Checklist de Configuração

- [ ] Colunas criadas e formatadas (validação de dados quando aplicável)
- [ ] Exemplos preenchidos (pelo menos 1 item completo do início ao fim)
- [ ] Permissões concedidas a todos os operadores e stakeholders
- [ ] Links para templates e checklists adicionados nas notas ou colunas dedicadas
- [ ] Instruções de uso compartilhadas com a equipe (link para este documento)

## Rotina de Manutenção

- Segunda-feira: revisar pipeline, identificar gargalos, atualizar prioridades.
- Diariamente: registrar avanço, tempo gasto e pendências desde a última atualização.
- Sexta-feira: consolidar aprendizados e mover itens concluídos para histórico.
- Mensal (ou a cada ciclo): exportar dados para análise (tempo médio, gargalos, satisfação).
