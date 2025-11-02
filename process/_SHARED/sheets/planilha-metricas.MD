# Planilha Compartilhada de Métricas – Estrutura Base

Use esta estrutura para criar ou atualizar a planilha oficial de métricas da ZeroUm. Importe para Google Sheets ou ferramenta aprovada e mantenha as colunas exatamente como descritas para garantir integração entre processos.

## Aba 1 – Entrevistas (UserInterviewValidation)

Colunas obrigatórias:
- Data
- Nome do entrevistado
- Persona / perfil
- Canal de aquisição
- Problema principal (citação curta)
- Solução atual
- Objeções registradas
- Status da hipótese (Validada, Refutada, Inconclusiva)
- Follow-up agendado? (Sim/Não + data)
- Responsável

## Aba 2 – Landing e Tráfego (LandingPageCreation)

Colunas obrigatórias:
- Data
- Fonte / campanha
- Visitas
- Cliques no CTA
- Conversões (leads ou pré-vendas)
- Taxa de conversão (%)
- Observações (copy testada, mudanças, provas sociais)
- Responsável pela análise

## Aba 3 – Outreach e Leads (OutreachCampaign)

Colunas obrigatórias:
- Data
- Canal (Rede direta, Comunidade, Frio)
- Volume de abordagens
- Respostas recebidas
- Conversas qualificadas
- Calls agendadas
- Principais objeções encontradas
- Próxima ação (follow-up, enviar material, call agendada)
- Owner

## Aba 4 – Pagamentos (CheckoutSetup)

Colunas obrigatórias:
- Data da transação
- Cliente
- Valor
- Método (PIX, Cartão, Boleto)
- Parcelas
- Status (Aprovado, Pendente, Estornado)
- Recibo enviado? (Sim/Não + data)
- Nota fiscal emitida? (Sim/Não + número)
- Link do comprovante / evidência
- Responsável pelo acompanhamento

## Aba 5 – Entregas (ClientDelivery / ManualMVPDesign)

Colunas obrigatórias:
- Cliente
- Data de início
- Data de conclusão prevista
- Data de conclusão real
- Owner da entrega
- Tempo total (dias)
- Nível de satisfação (texto curto ou escala)
- Depoimento coletado? (Sim/Não + link)
- Pendências pós-entrega

## Aba 6 – Retrospectivas (RetrospectiveAnalysis)

Colunas obrigatórias:
- Data da retrospectiva
- Principais métricas tratadas
- Ações priorizadas (até 3)
- Owners
- Prazo
- Status (Em andamento, Concluída, Atrasada)
- Observações / riscos

## Boas Práticas

- Padronize datas em formato ISO (AAAA-MM-DD).
- Utilize validação de dados para campos com opções fixas.
- Registre autores das atualizações na coluna “Responsável”.
- Faça backup semanal em PDF ou CSV e armazene em `_DATA/`.
- Atualize links de evidências (gravações, prints, relatórios) para consulta rápida.
