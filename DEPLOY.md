# 🚀 Guia de Deploy - Sistema de Comparação de Políticas IPAJM

Este documento explica como fazer deploy da aplicação Streamlit em diferentes plataformas.

---

## ⭐ Opção 1: Streamlit Community Cloud (RECOMENDADO)

**Gratuito, fácil e feito especificamente para Streamlit!**

### Vantagens:
- ✅ Totalmente gratuito
- ✅ Deploy em 3 cliques
- ✅ Atualizações automáticas via GitHub
- ✅ HTTPS incluído
- ✅ Não precisa configurar nada

### Passo a Passo:

1. **Acesse**: https://share.streamlit.io/

2. **Faça login com GitHub** (use a mesma conta do repositório)

3. **Clique em "New app"**

4. **Preencha os dados**:
   - **Repository**: `albertjr99/comparativo-politica-ipajm`
   - **Branch**: `claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8`
   - **Main file path**: `app.py`

5. **Clique em "Deploy"**

6. **Aguarde 2-3 minutos** e pronto! 🎉

**URL final**: Será algo como `https://seu-usuario-comparativo-politica.streamlit.app`

### Limitações:
- Upload de arquivos até 200MB (já configurado em `.streamlit/config.toml`)
- Aplicação entra em "sleep" após inatividade (acorda ao acessar)
- Recursos limitados (geralmente suficiente)

---

## 🟢 Opção 2: Render

**Plano gratuito com algumas limitações, mas funciona bem!**

### Vantagens:
- ✅ Plano gratuito disponível
- ✅ Suporta Python/Streamlit perfeitamente
- ✅ Deploy automático via GitHub
- ✅ HTTPS incluído

### Passo a Passo:

1. **Acesse**: https://render.com/

2. **Faça login/cadastro**

3. **Clique em "New +" → "Web Service"**

4. **Conecte seu repositório GitHub**:
   - Selecione `albertjr99/comparativo-politica-ipajm`

5. **Configure o serviço**:
   ```
   Name: comparativo-politica-ipajm
   Region: Oregon (US West) ou mais próximo
   Branch: claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

6. **Selecione o plano**:
   - Free ($0/mês) - Aplicação dorme após 15min de inatividade
   - Starter ($7/mês) - Sempre ativa

7. **Clique em "Create Web Service"**

8. **Aguarde o deploy** (5-10 minutos)

**URL final**: `https://comparativo-politica-ipajm.onrender.com`

### Limitações do plano gratuito:
- Aplicação entra em "sleep" após 15min de inatividade
- Pode levar 30-60s para "acordar"
- 750 horas/mês grátis

### Arquivo de Configuração (Opcional):

Crie um arquivo `render.yaml` na raiz:

```yaml
services:
  - type: web
    name: comparativo-politica-ipajm
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
    plan: free
```

---

## 🔵 Opção 3: Railway

**Alternativa moderna e fácil de usar**

### Vantagens:
- ✅ $5 de crédito gratuito/mês
- ✅ Deploy super rápido
- ✅ Interface moderna
- ✅ Suporte excelente para Python

### Passo a Passo:

1. **Acesse**: https://railway.app/

2. **Faça login com GitHub**

3. **Clique em "New Project" → "Deploy from GitHub repo"**

4. **Selecione o repositório**: `albertjr99/comparativo-politica-ipajm`

5. **Configure as variáveis**:
   - Adicione em "Settings → Deploy":
   ```
   Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

6. **Deploy automático!**

**URL final**: `https://comparativo-politica-ipajm.up.railway.app`

### Limitações:
- $5 de crédito gratuito/mês (geralmente suficiente para uso leve)
- Depois dos créditos, precisa de cartão de crédito

---

## 🟣 Opção 4: Heroku

**Clássico, mas agora é pago**

### ⚠️ Aviso:
Heroku **removeu o plano gratuito** em novembro de 2022. Agora custa **$7/mês** mínimo.

### Se quiser usar:

1. **Crie arquivo `setup.sh`** na raiz:

```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"seu-email@exemplo.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

2. **Crie `Procfile`** na raiz:

```
web: sh setup.sh && streamlit run app.py
```

3. **Deploy via Heroku CLI ou GitHub**

---

## 🚫 Opção 5: Vercel (NÃO RECOMENDADO)

**Vercel é focado em Next.js/React e não suporta Streamlit nativamente.**

Streamlit precisa rodar como servidor Python persistente, e Vercel é otimizado para serverless functions (tempo de execução limitado).

---

## 📊 Comparação Rápida

| Plataforma | Gratuito? | Facilidade | Velocidade | Recomendado? |
|------------|-----------|------------|------------|--------------|
| **Streamlit Cloud** | ✅ Sim | ⭐⭐⭐⭐⭐ | ⚡ Rápido | ✅ **SIM** |
| **Render** | ✅ Sim* | ⭐⭐⭐⭐ | ⚡ Rápido | ✅ Sim |
| **Railway** | ⚠️ $5/mês | ⭐⭐⭐⭐ | ⚡⚡ Muito Rápido | ⚠️ OK |
| **Heroku** | ❌ Não | ⭐⭐⭐ | ⚡ Rápido | ❌ Não |
| **Vercel** | ❌ Não suporta | ⭐ | - | ❌ **NÃO** |

*Com limitações (sleep após inatividade)

---

## 🎯 Recomendação Final

### Para uso pessoal/interno:
**Use Streamlit Community Cloud** - É perfeito, gratuito e sem complicações!

### Para uso profissional/produção:
**Use Render (plano pago $7/mês)** ou **Railway** - Sempre ativo, mais recursos, SLA garantido.

---

## 🔧 Configurações Importantes

Todos os arquivos necessários já estão configurados:

- ✅ `requirements.txt` - Dependências Python
- ✅ `.streamlit/config.toml` - Configurações do Streamlit
- ✅ `.gitignore` - Arquivos ignorados
- ✅ `app.py` - Aplicação principal

---

## 🆘 Problemas Comuns

### Erro: "Port already in use"
**Solução**: Use a variável de ambiente `$PORT` fornecida pela plataforma

### Erro: "Module not found"
**Solução**: Verifique se todas as dependências estão em `requirements.txt`

### Upload de PDF não funciona
**Solução**: Verifique o limite de upload em `.streamlit/config.toml` (maxUploadSize = 200MB)

### Aplicação muito lenta
**Solução**:
- No Streamlit Cloud: Normal, plano gratuito tem recursos limitados
- No Render: Ative o plano pago para mais recursos
- Otimize: Use `@st.cache_data` para cachear processamento de PDFs

---

## 📞 Suporte

Para mais informações:
- **Streamlit Cloud**: https://docs.streamlit.io/streamlit-community-cloud
- **Render**: https://render.com/docs
- **Railway**: https://docs.railway.app/

---

**Desenvolvido com ❤️ em Python + Streamlit**
