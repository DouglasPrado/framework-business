# Configuração de Variáveis para Execução de Agentes LLM

Este guia consolida como preparar o ambiente local para executar os agentes descritos em `LANGCHAIN.MD`. Ele complementa as instruções existentes no repositório e foca apenas em variáveis de ambiente e política de segredos.

## Variáveis sensíveis obrigatórias

Configure as variáveis abaixo antes de rodar qualquer agente LLM:

- `OPENAI_API_KEY`
- `LANGCHAIN_TRACING_V2` (use `true` ou `false` explicitamente)
- `LANGCHAIN_ENDPOINT`
- `LANGCHAIN_API_KEY`
- `LANGCHAIN_PROJECT`

Quando estiver sem as credenciais de LangSmith, defina `LANGCHAIN_TRACING_V2=false` para desativar o envio de traces, mantendo o checklist automático satisfeito.

## Export no Linux ou macOS

Execute os comandos no terminal antes de iniciar o agente:

- `export OPENAI_API_KEY="sk-..."`
- `export LANGCHAIN_TRACING_V2=true`
- `export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"`
- `export LANGCHAIN_API_KEY="lsm-..."`
- `export LANGCHAIN_PROJECT="framework-business"`

Grave esses valores no `~/.bash_profile`, `~/.zshenv` ou arquivo equivalente caso queira carregá-los automaticamente nas sessões futuras.

## Configuração no Windows (PowerShell)

Defina as variáveis dentro da janela do PowerShell antes de rodar scripts Python:

- `$Env:OPENAI_API_KEY = "sk-..."`
- `$Env:LANGCHAIN_TRACING_V2 = "true"`
- `$Env:LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"`
- `$Env:LANGCHAIN_API_KEY = "lsm-..."`
- `$Env:LANGCHAIN_PROJECT = "framework-business"`

Para persistir os valores, adicione-os ao perfil com `notepad $PROFILE` e insira os mesmos comandos.

## Política de segredos

- Nunca versione chaves reais em arquivos `.env`, commits ou pull requests.
- Use somente `dotenv` locais (por exemplo, `.env.local`) que estejam no `.gitignore`.
- Compartilhe credenciais via cofre corporativo ou gerenciador aprovado; não envie por e-mail ou chat aberto.
- Revogue imediatamente qualquer chave exposta publicamente e gere uma nova.
- Utilize o flag `AGENTS_SKIP_SECRET_CHECK=1` apenas em ambientes de desenvolvimento isolados e sem acesso a dados reais.

## Verificação automática

- Antes de iniciar, execute `python -m agents.scripts.check_env` para verificar se todas as variáveis estão definidas.
- O script `agents/scripts/run_strategy_agent.py` chama essa verificação automaticamente; a execução é interrompida quando algum segredo estiver ausente.
- Pipelines de CI devem incluir o comando de verificação no estágio de preparação para garantir conformidade antes de acionar agentes LLM.
