# 🚀 Deploy via GitHub - Streamlit Community Cloud

## Passo a Passo Completo para Rodar pelo GitHub

### 1️⃣ **Fazer Merge do Branch (Opcional mas Recomendado)**

Primeiro, vamos fazer merge do seu branch para a main para ficar mais organizado:

```bash
# Ir para a branch main
git checkout main

# Fazer merge do branch claude
git merge claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8

# Enviar para o GitHub
git push origin main
```

**OU** você pode usar direto o branch `claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8` no deploy.

---

### 2️⃣ **Acessar Streamlit Community Cloud**

1. Vá para: **https://share.streamlit.io/**

2. **Faça login com sua conta GitHub** (use a mesma conta do repositório `albertjr99`)
   - Clique em "Continue with GitHub"
   - Autorize o acesso quando solicitado

---

### 3️⃣ **Criar Nova Aplicação**

1. Na tela inicial, clique no botão **"New app"** (canto superior direito)

2. Você verá 3 opções de deploy. Escolha: **"From existing repo"**

---

### 4️⃣ **Configurar a Aplicação**

Preencha os campos:

```
Repository: albertjr99/comparativo-politica-ipajm
Branch: claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8
  (ou "main" se você fez o merge)
Main file path: app.py
```

**App URL (opcional)**: Você pode personalizar a URL
- Exemplo: `comparativo-ipajm`
- Ficará: `https://comparativo-ipajm.streamlit.app`

---

### 5️⃣ **Configurações Avançadas (Opcional)**

Clique em "Advanced settings" se quiser:

- **Python version**: 3.11 (já configurado em `runtime.txt`)
- **Secrets**: Não precisa por enquanto
- **Environment variables**: Não precisa

---

### 6️⃣ **Deploy!**

1. Clique no botão **"Deploy!"**

2. Aguarde 2-5 minutos enquanto:
   - ✅ Streamlit clona seu repositório
   - ✅ Instala as dependências do `requirements.txt`
   - ✅ Inicia a aplicação

3. Você verá logs em tempo real do processo

---

### 7️⃣ **Aplicação no Ar! 🎉**

Quando terminar, você terá:

- ✅ URL pública: `https://[seu-nome]-comparativo-politica.streamlit.app`
- ✅ HTTPS automático
- ✅ Atualização automática a cada `git push`
- ✅ 100% gratuito

---

## 🔄 Atualizações Automáticas

**IMPORTANTE**: Toda vez que você fizer alterações no código:

```bash
# 1. Fazer suas alterações
# 2. Commitar
git add .
git commit -m "Suas alterações"

# 3. Push para o GitHub
git push origin claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8

# 4. Streamlit detecta e atualiza automaticamente! 🚀
```

Você verá o ícone de "reloading" no Streamlit Cloud e em ~1 minuto a nova versão estará no ar!

---

## 📱 Gerenciar Aplicação

No painel do Streamlit Cloud você pode:

- 🔍 **Ver logs** em tempo real
- 📊 **Monitorar uso** (CPU, memória)
- 🔄 **Reiniciar** a aplicação
- ⚙️ **Editar configurações**
- 🗑️ **Deletar** a aplicação
- 📈 **Ver analytics** (visitantes, uso)

---

## ⚠️ GitHub Pages NÃO Funciona

**Atenção**: GitHub Pages (github.io) **NÃO funciona** para Streamlit porque:
- GitHub Pages só serve arquivos estáticos (HTML/CSS/JS)
- Streamlit precisa de um servidor Python rodando

Por isso usamos **Streamlit Community Cloud** que:
- ✅ Se conecta ao GitHub
- ✅ Roda o servidor Python
- ✅ Mantém a aplicação no ar 24/7

---

## 🎯 Resumo Visual

```
┌─────────────────┐
│   Seu GitHub    │  (albertjr99/comparativo-politica-ipajm)
│   Repositório   │
└────────┬────────┘
         │
         │ Streamlit Cloud lê daqui
         ↓
┌─────────────────┐
│  Streamlit      │  (conecta ao GitHub)
│  Community      │
│  Cloud          │
└────────┬────────┘
         │
         │ Hospeda e roda
         ↓
┌─────────────────┐
│   Aplicação     │  https://seu-app.streamlit.app
│   Online! 🚀    │
└─────────────────┘
```

---

## 🔧 Solução de Problemas

### Erro: "Repository not found"
**Solução**: Verifique se você autorizou o Streamlit a acessar seus repositórios no GitHub

### Erro: "requirements.txt not found"
**Solução**: Certifique-se que o arquivo está na raiz do repositório (está ✅)

### Erro: "Module not found"
**Solução**: Verifique se todas as dependências estão no `requirements.txt` (estão ✅)

### App muito lento
**Solução**: Normal no plano gratuito. Para mais performance, considere o plano pago

### App mostra erro ao fazer upload
**Solução**: Verifique o tamanho do PDF (limite: 200MB configurado em `.streamlit/config.toml`)

---

## 💡 Dicas Pro

### 1. **Secrets (Senhas/APIs)**
Se precisar de senhas ou chaves API no futuro:
- No Streamlit Cloud → Settings → Secrets
- Adicione em formato TOML
- Acesse no código com `st.secrets["chave"]`

### 2. **Monitoramento**
- Ative notificações por email em caso de erro
- Settings → Email notifications → ON

### 3. **Domínio Customizado** (Opcional)
- Você pode usar seu próprio domínio
- Settings → Custom domain → Adicionar

### 4. **Analytics**
- Veja quantas pessoas estão usando
- Streamlit Cloud Dashboard → Analytics

---

## 📞 Links Úteis

- **Streamlit Cloud**: https://share.streamlit.io/
- **Documentação**: https://docs.streamlit.io/streamlit-community-cloud
- **Seu Repositório**: https://github.com/albertjr99/comparativo-politica-ipajm

---

## ✅ Checklist Final

Antes de fazer deploy, confirme:

- [x] Repositório no GitHub: `albertjr99/comparativo-politica-ipajm`
- [x] Branch: `claude/python-modernize-ui-016g5o2dVekXyyBeYxDQQ3j8`
- [x] Arquivo `app.py` na raiz
- [x] Arquivo `requirements.txt` na raiz
- [x] Arquivo `.streamlit/config.toml` configurado
- [x] Conta no Streamlit Cloud (criar em share.streamlit.io)

**Tudo pronto! Basta seguir os passos acima! 🚀**

---

**Desenvolvido com ❤️ em Python + Streamlit**
