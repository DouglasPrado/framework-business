#!/bin/bash
# Script para refatorar todos os subagentes removendo código duplicado

echo "🔄 Refatorando subagentes para usar métodos da SubagentBase..."
echo ""

SUBAGENTS=(
    "landing_page_creation.py"
    "problem_hypothesis_definition.py"
    "target_user_identification.py"
    "user_interview_validation.py"
    "client_delivery.py"
    "problem_hypothesis_express.py"
)

BASE_DIR="business/strategies/zeroum/subagents"

for file in "${SUBAGENTS[@]}"; do
    filepath="$BASE_DIR/$file"

    if [ ! -f "$filepath" ]; then
        echo "⚠️  Arquivo não encontrado: $filepath"
        continue
    fi

    echo "📝 Processando $file..."

    # 1. Substituir _invoke_llm por invoke_llm
    sed -i '' 's/self\._invoke_llm(/self.invoke_llm(/g' "$filepath"

    # 2. Substituir _save_document por save_document
    sed -i '' 's/self\._save_document(/self.save_document(/g' "$filepath"

    # 3. Substituir _format_list por format_list
    sed -i '' 's/self\._format_list(/self.format_list(/g' "$filepath"

    # 4. Substituir _setup_directories por setup_directories
    # Nota: precisa de análise manual para passar os diretórios corretos

    echo "   ✅ Substituições de chamadas concluídas"
done

echo ""
echo "="*80
echo "✅ Refatoração de chamadas concluída!"
echo "="*80
echo ""
echo "⚠️  ATENÇÃO: Você ainda precisa:"
echo "   1. Remover manualmente os métodos _setup_directories, _invoke_llm, _save_document, _format_list"
echo "   2. Atualizar _setup_directories() para self.setup_directories([lista de dirs])"
echo "   3. Validar que todas as chamadas foram substituídas corretamente"
echo ""
