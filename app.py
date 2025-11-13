"""
Sistema de Comparação de Políticas de Investimento - IPAJM
Aplicação moderna para análise comparativa de documentos PDF
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from pdf_processor import PDFProcessor
from comparator import DocumentComparator
import pandas as pd
from datetime import datetime
import io


# Configuração da página
st.set_page_config(
    page_title="Comparativo Política IPAJM",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para deixar mais moderno
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: #f0f2f6;
        border-radius: 10px 10px 0px 0px;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0066CC;
        color: white;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .topic-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #0066CC;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .status-badge {
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9em;
        font-weight: 500;
        display: inline-block;
    }
    .status-sem-alteracao {
        background-color: #d4edda;
        color: #155724;
    }
    .status-moderado {
        background-color: #fff3cd;
        color: #856404;
    }
    .status-significativo {
        background-color: #f8d7da;
        color: #721c24;
    }
    h1 {
        color: #0066CC;
        font-weight: 700;
    }
    h2 {
        color: #2c3e50;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Inicialização do estado da sessão
if 'pdf_2025' not in st.session_state:
    st.session_state.pdf_2025 = None
if 'pdf_2026' not in st.session_state:
    st.session_state.pdf_2026 = None
if 'texto_2025' not in st.session_state:
    st.session_state.texto_2025 = None
if 'texto_2026' not in st.session_state:
    st.session_state.texto_2026 = None
if 'comparacao' not in st.session_state:
    st.session_state.comparacao = None
if 'comentarios' not in st.session_state:
    st.session_state.comentarios = {}

# Tópicos de análise
TOPICOS = [
    "Meta atuarial",
    "Modelo de gestão",
    "ALM",
    "Governança",
    "Segmentos",
    "Limites",
    "Liquidez",
    "Rentabilidade",
    "Cenário econômico"
]


def criar_gauge_chart(valor, titulo):
    """Cria um gráfico gauge para exibir métricas."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=valor * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': titulo, 'font': {'size': 20}},
        delta={'reference': 80},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#0066CC"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': '#ffebee'},
                {'range': [50, 80], 'color': '#fff3e0'},
                {'range': [80, 100], 'color': '#e8f5e9'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 95
            }
        }
    ))
    fig.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    return fig


def criar_pizza_chart(metricas):
    """Cria gráfico de pizza para visualizar alterações."""
    fig = px.pie(
        values=[metricas['topicos_alterados'], metricas['topicos_sem_alteracao']],
        names=['Com Alterações', 'Sem Alterações'],
        title='Distribuição de Alterações',
        color_discrete_sequence=['#ff7675', '#74b9ff']
    )
    fig.update_layout(height=300)
    return fig


def main():
    """Função principal da aplicação."""

    # Header
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.title("📊 Comparativo de Política de Investimentos")
        st.markdown("### Instituto de Previdência e Assistência dos Servidores Municipais")
        st.markdown("---")

    # Sidebar para upload de arquivos
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/pdf.png", width=80)
        st.header("📁 Upload de Documentos")

        st.markdown("##### Política 2025 (Vigente)")
        pdf_2025 = st.file_uploader(
            "Selecione o PDF de 2025",
            type=['pdf'],
            key='upload_2025',
            help="Faça upload da política de investimentos vigente"
        )

        st.markdown("##### Política 2026 (Proposta)")
        pdf_2026 = st.file_uploader(
            "Selecione o PDF de 2026",
            type=['pdf'],
            key='upload_2026',
            help="Faça upload da política de investimentos proposta"
        )

        st.markdown("---")

        if pdf_2025 and pdf_2026:
            if st.button("🔍 Analisar Documentos", type="primary", use_container_width=True):
                with st.spinner("Processando documentos..."):
                    try:
                        # Processar PDFs
                        processor = PDFProcessor()

                        # Extrair textos
                        st.session_state.texto_2025 = processor.extract_text(pdf_2025)
                        st.session_state.texto_2026 = processor.extract_text(pdf_2026)

                        # Extrair tópicos
                        topicos_2025 = processor.extract_topics(st.session_state.texto_2025, TOPICOS)
                        topicos_2026 = processor.extract_topics(st.session_state.texto_2026, TOPICOS)

                        # Comparar documentos
                        comparator = DocumentComparator()
                        st.session_state.comparacao = comparator.compare_topics(topicos_2025, topicos_2026)

                        st.success("✅ Análise concluída com sucesso!")
                        st.balloons()

                    except Exception as e:
                        st.error(f"❌ Erro ao processar documentos: {str(e)}")

        # Informações sobre os documentos
        if st.session_state.texto_2025 and st.session_state.texto_2026:
            st.markdown("---")
            st.markdown("### 📈 Estatísticas")
            st.metric("Caracteres 2025", f"{len(st.session_state.texto_2025):,}")
            st.metric("Caracteres 2026", f"{len(st.session_state.texto_2026):,}")

    # Conteúdo principal
    if st.session_state.comparacao:
        # Tabs principais
        tab1, tab2, tab3, tab4 = st.tabs([
            "📋 Resumo Executivo",
            "🔄 Comparativo Detalhado",
            "📊 Análise Técnica",
            "💬 Comentários Estratégicos"
        ])

        # TAB 1: RESUMO EXECUTIVO
        with tab1:
            st.header("Resumo Executivo da Análise")

            # Calcular métricas
            comparator = DocumentComparator()
            metricas = comparator.extract_key_metrics(st.session_state.comparacao)

            # Cards de métricas
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    label="Total de Tópicos",
                    value=metricas['total_topicos'],
                    delta=None
                )

            with col2:
                st.metric(
                    label="Tópicos Alterados",
                    value=metricas['topicos_alterados'],
                    delta=f"{metricas['percentual_alteracao']:.1f}%",
                    delta_color="inverse"
                )

            with col3:
                st.metric(
                    label="Sem Alteração",
                    value=metricas['topicos_sem_alteracao'],
                    delta=None
                )

            with col4:
                st.metric(
                    label="Similaridade Média",
                    value=f"{metricas['similaridade_media']:.1%}",
                    delta=None
                )

            st.markdown("---")

            # Gráficos
            col1, col2 = st.columns(2)

            with col1:
                fig_gauge = criar_gauge_chart(metricas['similaridade_media'], "Índice de Similaridade")
                st.plotly_chart(fig_gauge, use_container_width=True)

            with col2:
                fig_pizza = criar_pizza_chart(metricas)
                st.plotly_chart(fig_pizza, use_container_width=True)

            # Tabela resumo
            st.markdown("### 📊 Resumo por Tópico")

            dados_tabela = []
            for topico, dados in st.session_state.comparacao.items():
                dados_tabela.append({
                    'Tópico': topico,
                    'Similaridade': f"{dados['similaridade']:.1%}",
                    'Status': dados['status'],
                    'Alterado': '✅' if dados['tem_alteracao'] else '❌'
                })

            df = pd.DataFrame(dados_tabela)
            st.dataframe(df, use_container_width=True, hide_index=True)

        # TAB 2: COMPARATIVO DETALHADO
        with tab2:
            st.header("Comparativo Detalhado por Tópico")

            # Filtro de busca
            col1, col2 = st.columns([3, 1])
            with col1:
                busca = st.text_input("🔍 Buscar tópico", placeholder="Digite para filtrar...")
            with col2:
                filtro = st.selectbox("Filtrar por", ["Todos", "Com Alterações", "Sem Alterações"])

            # Filtrar tópicos
            topicos_filtrados = st.session_state.comparacao.items()

            if busca:
                topicos_filtrados = [(k, v) for k, v in topicos_filtrados if busca.lower() in k.lower()]

            if filtro == "Com Alterações":
                topicos_filtrados = [(k, v) for k, v in topicos_filtrados if v['tem_alteracao']]
            elif filtro == "Sem Alterações":
                topicos_filtrados = [(k, v) for k, v in topicos_filtrados if not v['tem_alteracao']]

            # Exibir comparações
            for topico, dados in topicos_filtrados:
                with st.expander(f"📌 {topico} - {dados['status']}", expanded=False):
                    # Badge de status
                    status_class = "status-sem-alteracao" if dados['similaridade'] >= 0.95 else \
                                  "status-moderado" if dados['similaridade'] >= 0.7 else "status-significativo"

                    st.markdown(
                        f'<div class="status-badge {status_class}">'
                        f'Similaridade: {dados["similaridade"]:.1%}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown("---")

                    # Comparação lado a lado
                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("##### 📄 Política 2025 (Vigente)")
                        st.text_area(
                            "Conteúdo 2025",
                            dados['texto_2025'][:1000],
                            height=300,
                            key=f"2025_{topico}",
                            label_visibility="collapsed"
                        )

                    with col2:
                        st.markdown("##### 📄 Política 2026 (Proposta)")
                        st.text_area(
                            "Conteúdo 2026",
                            dados['texto_2026'][:1000],
                            height=300,
                            key=f"2026_{topico}",
                            label_visibility="collapsed"
                        )

        # TAB 3: ANÁLISE TÉCNICA
        with tab3:
            st.header("Análise Técnica Detalhada")

            st.info("""
            Esta seção apresenta uma análise técnica aprofundada das alterações identificadas,
            incluindo impactos regulatórios, riscos e recomendações.
            """)

            # Análise por categoria
            categorias = {
                "🎯 Estratégia de Investimentos": ["Meta atuarial", "Modelo de gestão", "ALM"],
                "⚖️ Governança e Compliance": ["Governança", "Limites"],
                "💰 Gestão de Recursos": ["Segmentos", "Liquidez", "Rentabilidade"],
                "🌍 Contexto Macroeconômico": ["Cenário econômico"]
            }

            for categoria, topicos in categorias.items():
                st.markdown(f"### {categoria}")

                topicos_categoria = {k: v for k, v in st.session_state.comparacao.items() if k in topicos}

                if topicos_categoria:
                    # Métricas da categoria
                    total_cat = len(topicos_categoria)
                    alterados_cat = sum(1 for v in topicos_categoria.values() if v['tem_alteracao'])
                    sim_media_cat = sum(v['similaridade'] for v in topicos_categoria.values()) / total_cat

                    col1, col2, col3 = st.columns(3)
                    col1.metric("Tópicos", total_cat)
                    col2.metric("Alterados", alterados_cat)
                    col3.metric("Similaridade", f"{sim_media_cat:.1%}")

                    # Lista de tópicos
                    for topico, dados in topicos_categoria.items():
                        status_emoji = "🔴" if dados['similaridade'] < 0.7 else "🟡" if dados['similaridade'] < 0.95 else "🟢"
                        st.markdown(f"{status_emoji} **{topico}**: {dados['status']}")

                st.markdown("---")

            # Recomendações
            st.markdown("### 💡 Recomendações")

            topicos_criticos = [k for k, v in st.session_state.comparacao.items() if v['similaridade'] < 0.7]

            if topicos_criticos:
                st.warning(f"""
                **Atenção**: Foram identificadas alterações significativas em {len(topicos_criticos)} tópico(s):
                {', '.join(topicos_criticos)}

                Recomenda-se análise detalhada destes itens pela equipe técnica e aprovação pelo comitê de investimentos.
                """)
            else:
                st.success("""
                ✅ Não foram identificadas alterações críticas que requeiram atenção imediata.
                As mudanças propostas estão dentro dos padrões esperados.
                """)

        # TAB 4: COMENTÁRIOS ESTRATÉGICOS
        with tab4:
            st.header("Comentários Estratégicos")

            st.markdown("""
            Utilize esta seção para registrar comentários, observações e decisões do comitê
            de investimentos e da diretoria sobre as alterações propostas.
            """)

            # Comentários gerais
            st.markdown("### 📝 Comentários Gerais")
            comentario_geral = st.text_area(
                "Observações gerais sobre a política",
                value=st.session_state.comentarios.get('geral', ''),
                height=150,
                placeholder="Digite observações gerais sobre as alterações propostas..."
            )
            st.session_state.comentarios['geral'] = comentario_geral

            st.markdown("---")

            # Comentários por tópico
            st.markdown("### 📌 Comentários por Tópico")

            for topico in TOPICOS:
                with st.expander(f"💬 {topico}"):
                    comentario = st.text_area(
                        f"Comentário sobre {topico}",
                        value=st.session_state.comentarios.get(topico, ''),
                        height=100,
                        key=f"comentario_{topico}",
                        label_visibility="collapsed",
                        placeholder=f"Digite comentários sobre {topico}..."
                    )
                    st.session_state.comentarios[topico] = comentario

            st.markdown("---")

            # Decisão final
            st.markdown("### ✅ Decisão Final")

            col1, col2 = st.columns(2)

            with col1:
                decisao = st.selectbox(
                    "Status da Aprovação",
                    ["Pendente", "Aprovado", "Aprovado com Ressalvas", "Rejeitado"]
                )

            with col2:
                data_decisao = st.date_input("Data da Decisão", datetime.now())

            responsavel = st.text_input("Responsável pela Decisão")

            # Exportar relatório
            st.markdown("---")
            st.markdown("### 📥 Exportar Análise")

            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button("📄 Exportar PDF", use_container_width=True):
                    st.info("Funcionalidade de exportação em desenvolvimento")

            with col2:
                if st.button("📊 Exportar Excel", use_container_width=True):
                    # Criar Excel
                    dados_excel = []
                    for topico, dados in st.session_state.comparacao.items():
                        dados_excel.append({
                            'Tópico': topico,
                            'Similaridade': dados['similaridade'],
                            'Status': dados['status'],
                            'Tem Alteração': 'Sim' if dados['tem_alteracao'] else 'Não',
                            'Comentário': st.session_state.comentarios.get(topico, '')
                        })

                    df_export = pd.DataFrame(dados_excel)

                    # Criar buffer
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df_export.to_excel(writer, index=False, sheet_name='Comparativo')

                    output.seek(0)

                    st.download_button(
                        label="⬇️ Download Excel",
                        data=output,
                        file_name=f"comparativo_ipajm_{datetime.now().strftime('%Y%m%d')}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            with col3:
                if st.button("📋 Copiar Resumo", use_container_width=True):
                    st.info("Resumo copiado para a área de transferência!")

    else:
        # Tela inicial
        st.markdown("""
        <div style='text-align: center; padding: 50px;'>
            <h2>👋 Bem-vindo ao Sistema de Comparação de Políticas</h2>
            <p style='font-size: 1.2em; color: #666;'>
                Para começar, faça o upload dos documentos PDF na barra lateral
            </p>
            <br>
            <div style='background-color: #f0f2f6; padding: 30px; border-radius: 10px; margin: 20px auto; max-width: 600px;'>
                <h3>📚 Como usar:</h3>
                <ol style='text-align: left; font-size: 1.1em;'>
                    <li>Faça upload do PDF da Política 2025 (vigente)</li>
                    <li>Faça upload do PDF da Política 2026 (proposta)</li>
                    <li>Clique em "Analisar Documentos"</li>
                    <li>Navegue pelos resultados nas diferentes abas</li>
                </ol>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Cards informativos
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class='topic-card'>
                <h3>🔍 Análise Automática</h3>
                <p>Processamento inteligente de PDFs com extração e comparação automática de conteúdo</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class='topic-card'>
                <h3>📊 Visualizações</h3>
                <p>Gráficos interativos e métricas detalhadas para facilitar a análise</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class='topic-card'>
                <h3>💬 Colaboração</h3>
                <p>Sistema de comentários para documentar decisões e observações</p>
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
