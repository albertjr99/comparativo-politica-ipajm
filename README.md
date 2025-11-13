# 📊 Sistema de Comparação de Políticas de Investimento - IPAJM

Sistema moderno e interativo desenvolvido em **Python** para análise comparativa de documentos PDF de políticas de investimento do Instituto de Previdência e Assistência dos Servidores Municipais.

## ✨ Características

### 🎯 Funcionalidades Principais

- **Upload de PDFs**: Interface intuitiva para carregar documentos de políticas
- **Extração Automática**: Processamento inteligente de texto usando `pdfplumber`
- **Análise Comparativa**: Comparação detalhada entre versões 2025 e 2026
- **Visualizações Interativas**: Gráficos e métricas em tempo real
- **Sistema de Comentários**: Documentação de decisões e observações
- **Exportação de Dados**: Geração de relatórios em Excel

### 📋 Tópicos Analisados

1. Meta atuarial
2. Modelo de gestão
3. ALM (Asset-Liability Management)
4. Governança
5. Segmentos
6. Limites
7. Liquidez
8. Rentabilidade
9. Cenário econômico

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório** (ou navegue até a pasta do projeto):

```bash
cd comparativo-politica-ipajm
```

2. **Crie um ambiente virtual** (recomendado):

```bash
python -m venv venv
```

3. **Ative o ambiente virtual**:

- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

4. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

## 🎮 Como Usar

### Iniciar a Aplicação

Execute o comando:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador em `http://localhost:8501`

### Fluxo de Trabalho

1. **Upload dos Documentos**:
   - Na barra lateral, faça upload do PDF da Política 2025 (vigente)
   - Faça upload do PDF da Política 2026 (proposta)

2. **Análise**:
   - Clique no botão "🔍 Analisar Documentos"
   - Aguarde o processamento (alguns segundos)

3. **Navegação**:
   - **Resumo Executivo**: Visão geral com métricas e gráficos
   - **Comparativo Detalhado**: Comparação lado a lado de cada tópico
   - **Análise Técnica**: Análise aprofundada por categoria
   - **Comentários Estratégicos**: Documentação de decisões

4. **Exportação**:
   - Exporte os resultados em formato Excel
   - Salve comentários e decisões

## 📁 Estrutura do Projeto

```
comparativo-politica-ipajm/
├── app.py                  # Aplicação principal Streamlit
├── pdf_processor.py        # Módulo de processamento de PDFs
├── comparator.py           # Módulo de comparação de documentos
├── requirements.txt        # Dependências do projeto
├── README.md              # Documentação
├── .streamlit/
│   └── config.toml        # Configurações do Streamlit
└── venv/                  # Ambiente virtual (não versionado)
```

## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para aplicações web em Python
- **[pdfplumber](https://github.com/jsvine/pdfplumber)**: Extração de texto de PDFs
- **[Plotly](https://plotly.com/)**: Gráficos interativos
- **[Pandas](https://pandas.pydata.org/)**: Manipulação de dados
- **[openpyxl](https://openpyxl.readthedocs.io/)**: Exportação para Excel

## 🎨 Design e Interface

A aplicação conta com:

- **Design Moderno**: Interface limpa e profissional
- **Cores Institucionais**: Paleta azul (#0066CC) alinhada com padrões corporativos
- **Responsividade**: Layout adaptável a diferentes tamanhos de tela
- **Interatividade**: Gráficos, filtros e buscas em tempo real
- **Acessibilidade**: Cores contrastantes e boa legibilidade

## 📊 Métricas e Análises

O sistema calcula automaticamente:

- **Índice de Similaridade**: Percentual de similaridade entre documentos
- **Tópicos Alterados**: Quantidade de tópicos com mudanças
- **Status por Tópico**: Classificação em sem alteração, moderado ou significativo
- **Distribuição Visual**: Gráficos de gauge e pizza

## 💡 Dicas de Uso

1. **PDFs com Texto**: Certifique-se de que os PDFs contêm texto extraível (não imagens)
2. **Qualidade dos Documentos**: PDFs bem formatados geram melhores resultados
3. **Salvamento de Comentários**: Os comentários são mantidos durante a sessão
4. **Exportação Regular**: Exporte os dados antes de fechar a aplicação

## 🔧 Personalização

### Alterar Tópicos Analisados

Edite a lista `TOPICOS` em `app.py`:

```python
TOPICOS = [
    "Seu Tópico 1",
    "Seu Tópico 2",
    # ... adicione mais tópicos
]
```

### Modificar Cores e Tema

Edite o arquivo `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#0066CC"  # Cor principal
backgroundColor = "#FFFFFF"  # Cor de fundo
secondaryBackgroundColor = "#F0F2F6"  # Cor secundária
textColor = "#262730"  # Cor do texto
```

## 🌐 Deploy em Produção

### Opção Recomendada: Streamlit Community Cloud (Gratuito)

1. Acesse: https://share.streamlit.io/
2. Faça login com GitHub
3. Clique em "New app"
4. Configure:
   - Repository: `albertjr99/comparativo-politica-ipajm`
   - Branch: `claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8`
   - Main file: `app.py`
5. Clique em "Deploy"

**URL final**: `https://seu-usuario-comparativo-politica.streamlit.app`

### Outras Opções:

- **Render**: Deploy automático com plano gratuito (arquivo `render.yaml` incluído)
- **Railway**: $5 de crédito/mês (arquivo `railway.json` incluído)
- **Heroku**: Pago ($7/mês) (arquivo `Procfile` incluído)

📖 **Guia completo de deploy**: Veja o arquivo `DEPLOY.md` para instruções detalhadas de cada plataforma.

## 🐛 Solução de Problemas

### Erro ao instalar dependências

```bash
# Atualize o pip
pip install --upgrade pip

# Instale novamente
pip install -r requirements.txt
```

### Erro ao processar PDF

- Verifique se o PDF não está protegido por senha
- Certifique-se de que o PDF contém texto extraível
- Tente converter o PDF para um formato mais recente

### Aplicação não inicia

```bash
# Verifique se o Streamlit está instalado
streamlit --version

# Reinstale se necessário
pip install streamlit --upgrade
```

## 📝 Licença

Este projeto foi desenvolvido para uso interno do IPAJM.

## 👥 Suporte

Para dúvidas ou problemas:
- Abra uma issue no repositório
- Entre em contato com a equipe de TI

## 🚀 Próximas Melhorias

- [ ] Exportação em PDF
- [ ] Histórico de análises
- [ ] Comparação de múltiplas versões
- [ ] Dashboard executivo
- [ ] Notificações por email
- [ ] Integração com banco de dados

---

**Desenvolvido com ❤️ em Python + Streamlit**
