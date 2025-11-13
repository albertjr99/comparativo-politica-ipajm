@echo off
REM Script para iniciar o Sistema de Comparação de Políticas IPAJM no Windows

echo 🚀 Iniciando Sistema de Comparação de Políticas IPAJM...
echo.

REM Ativar ambiente virtual
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo ❌ Ambiente virtual não encontrado!
    echo Execute: python -m venv venv
    echo Depois: venv\Scripts\activate.bat
    echo E então: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Verificar se as dependências estão instaladas
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo 📦 Instalando dependências...
    pip install -r requirements.txt
)

REM Iniciar aplicação
echo ✨ Abrindo aplicação no navegador...
echo.
streamlit run app.py
