# Estrutura do Board Operacional – LucroSeparado MVP Manual

## Ferramenta Selecionada

- Google Sheets (arquivo `LucroSeparado - Operação Manual`)
- Abas principais: `Pipeline`, `Resumo Semana`, `Feedbacks`, `Logs Tempo`
- Acesso compartilhado com: Douglas (editor), Ana Luiza (editor), Carla (visualização)

## Colunas da Aba Pipeline

1. `ID` – formato `LS-YYYYMM-###`
2. `Cliente` – nome completo
3. `Canal de entrada` – Landing / WhatsApp / Indicação
4. `Status` – dropdown com os valores abaixo
5. `Data de entrada`
6. `Deadline SLA` – data/hora limite para entrega do diagnóstico
7. `Responsável atual`
8. `Tempo estimado restante (min)`
9. `Checklist link` – link para checklist individual duplicado
10. `Observações / riscos`
11. `Feedback Cliente` – campo preenchido após follow-up
12. `Data conclusão ciclo`

### Status Disponíveis

- `Aguardando dados`
- `Em triagem`
- `Onboarding em andamento`
- `Produção`
- `QA`
- `Pronto para entregar`
- `Entregue`
- `Follow-up agendado`
- `Em acompanhamento semanal`
- `Concluído`
- `Pausado (cliente)`
- `Cancelado`

## Vistas Auxiliares

- **Filtro “Hoje”**: exibe itens com `Deadline SLA` até 18h.
- **Filtro “QA Pendentes”**: status `QA` ou `Pronto para entregar` com tempo > 30 min.
- **Resumo Semana**: tabela dinâmica com total de entregas, tempos médios por etapa e número de exceções.
- **Feedbacks**: coleta consolidada (escala 1-3 + comentários).

## Convenções de Uso

- Cada novo cliente recebe um ID incremental e um link próprio de checklist (duplicar modelo).
- Atualizações de status devem ocorrer imediatamente após concluir a etapa (máximo 15 min de atraso).
- `Tempo estimado restante` atualizado manualmente ao iniciar cada etapa.
- Comentários críticos registrados na coluna `Observações` e detalhados na aba `Logs Tempo`.
- Cores condicionais: laranja para status sem atualização > 4h, vermelho para SLA vencido.

## Permissões e Segurança

- Compartilhamento restrito ao domínio @lucroseparado.com.
- Guia `Config` protegida contendo fórmulas e listas suspensas.
- Backups automáticos semanais via Google Drive (versões).

## Próximos Ajustes Sugeridos

- Após o piloto, avaliar migração para Notion ou Airtable caso a equipe cresça.
- Integrar planilha ao Zapier para criar cards automaticamente quando o checkout confirmar pagamento.
