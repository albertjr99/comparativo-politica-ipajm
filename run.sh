#!/bin/bash

# Script para iniciar o Sistema de Comparação de Políticas IPAJM

echo "🚀 Iniciando Sistema de Comparação de Políticas IPAJM..."
echo ""

# Ativar ambiente virtual
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Ambiente virtual não encontrado!"
    echo "Execute: python -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Verificar se as dependências estão instaladas
python -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Instalando dependências..."
    pip install -r requirements.txt
fi

# Iniciar aplicação
echo "✨ Abrindo aplicação no navegador..."
echo ""
streamlit run app.py
