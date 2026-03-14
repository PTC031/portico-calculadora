import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="PÓRTICO | Diagnóstico de Rentabilidade",
    page_icon="🌊",
    layout="centered"
)

# 2. UX/UI DESIGN SYSTEM (Padrão Airbnb / High-End SaaS)
st.markdown("""
    <style>
    /* Fundo Off-White Suave (Clean Coastal) */
    .stApp {
        background-color: #F7F9FC;
    }
    
    /* Tipografia de Alto Contraste e Sofisticação */
    h1, h2, h3, h4, p, span, div {
        color: #0F293E; 
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
    }
    
    /* Título Principal */
    .main-title {
        text-align: center; 
        font-size: 38px; 
        font-weight: 800; 
        color: #0F293E;
        margin-bottom: 5px;
        letter-spacing: -0.5px;
    }
    
    /* Subtítulo */
    .sub-title {
        text-align: center; 
        color: #5C6A79; 
        font-size: 16px; 
        margin-bottom: 40px;
    }
    
    /* Estilização das Métricas (Cards Brancos com Sombra Suave) */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 20px rgba(15, 41, 62, 0.05);
        border: 1px solid #E2E8F0;
    }
    div[data-testid="metric-container"] label {
        color: #5C6A79 !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #0F293E !important;
        font-weight: 800 !important;
    }
    
    /* Botão de Conversão (Dourado Solar) */
    .stButton>button {
        background-color: #B8922A;
        color: #FFFFFF !important;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        width: 100%;
        padding: 16px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0px 8px 15px rgba(184, 146, 42, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #9A7920;
        transform: translateY(-2px);
        box-shadow: 0px 12px 20px rgba(184, 146, 42, 0.4);
    }
    
    /* Aviso de Prejuízo (Coral Suave) */
    .loss-alert {
        text-align: center; 
        color: #E63946; 
        font-size: 28px; 
        font-weight: 800; 
        margin-top: 30px;
        background-color: #FFF0F1;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #FAD2D5;
    }
    </style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO DA MARCA
st.markdown("<p style='text-align: center; font-size: 12px; font-weight: 700; letter-spacing: 6px; color: #B8922A; text-transform: uppercase;'>P Ó R T I C O</p>", unsafe_allow_html=True)
st.markdown("<h1 class='main-title'>Calculadora de Rentabilidade</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Descubra o vazamento financeiro do seu ativo imobiliário e quanto você está deixando na mesa das OTAs.</p>", unsafe_allow_html=True)

# 4. INPUTS DO CLIENTE (Design Limpo)
st.markdown("<h3 style='font-size: 18px; margin-bottom: 20px;'>1. Dados da Operação Atual</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    qtd_imoveis = st.number_input("Quantidade de Imóveis (Unidades)", min_value=1, value=2, step=1)
    diaria_media = st.number_input("Diária Média (R$ / ADR)", min_value=50.0, value=450.0, step=50.0)

with col2:
    ocupacao_atual = st.slider("Taxa de Ocupação Média (%)", min_value=10, max_value=100, value=55, step=5)
    dependencia_ota = st.slider("Dependência de Plataformas (%)", min_value=0, max_value=100, value=90, step=5, help="Qual porcentagem das suas reservas vem do Airbnb/Booking?")

# 5. O MOTOR FINANCEIRO
dias_ano = 365
taxa_ota_media = 0.18 
ocupacao_alvo_portico = 80 

receita_potencial_bruta = qtd_imoveis * diaria_media * dias_ano
receita_bruta_atual = receita_potencial_bruta * (ocupacao_atual / 100)

vazamento_comissao = receita_bruta_atual * (dependencia_ota / 100) * taxa_ota_media
receita_alvo = receita_potencial_bruta * (ocupacao_alvo_portico / 100)
vazamento_vacancia = max(0, receita_alvo - receita_bruta_atual)

dinheiro_na_mesa = vazamento_comissao + vazamento_vacancia
receita_liquida_estimada = receita_bruta_atual - vazamento_comissao

st.markdown("<br><h3 style='font-size: 18px; margin-bottom: 20px;'>2. O Raio-X do seu Patrimônio (Anual)</h3>", unsafe_allow_html=True)

# 6. EXIBIÇÃO DE RESULTADOS (Cards)
col_res1, col_res2, col_res3 = st.columns(3)

col_res1.metric("Receita Bruta Estimada", f"R$ {receita_bruta_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col_res2.metric("Comissões Pagas (OTAs)", f"R$ {vazamento_comissao:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col_res3.metric("Lucro Líquido (NOI Base)", f"R$ {receita_liquida_estimada:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.markdown(f"<div class='loss-alert'>⚠️ Prejuízo Invisível: R$ {dinheiro_na_mesa:,.2f} / ano</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5C6A79; font-size: 14px; margin-top: 10px;'>Esta é a soma das taxas abusivas com a vacância que a infraestrutura PÓRTICO pode recuperar para você.</p>", unsafe_allow_html=True)

# 7. GRÁFICO VISUAL (Nova Paleta Coastal)
labels = ['Lucro Retido', 'Comissões OTAs', 'Vacância Evitável']
values = [receita_liquida_estimada, vazamento_comissao, vazamento_vacancia]
colors = ['#0F293E', '#E63946', '#B8922A'] 

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.55)])
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=14,
                  marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#0F293E', family="Inter"),
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
    margin=dict(t=10, b=10, l=10, r=10)
)
st.plotly_chart(fig, use_container_width=True)

# 8. CALL TO ACTION 
st.markdown("<br>", unsafe_allow_html=True)
whatsapp_link = "https://wa.me/5531999999999?text=Ol%C3%A1%2C%20fiz%20o%20diagn%C3%B3stico%20na%20calculadora%20P%C3%B3rtico%20e%20vi%20o%20tamanho%20do%20meu%20vazamento%20financeiro.%20Gostaria%20de%20ajuda."

st.markdown(f"""
<a href="{whatsapp_link}" target="_blank" style="text-decoration: none;">
    <div style="background-color: #B8922A; color: #FFFFFF; text-align: center; padding: 18px; border-radius: 8px; font-weight: 800; font-family: 'Inter', sans-serif; letter-spacing: 1px; text-transform: uppercase; box-shadow: 0px 8px 15px rgba(184, 146, 42, 0.3);">
        RECUPERAR MEU LUCRO AGORA
    </div>
</a>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 11px; margin-top: 30px; color: #A0AAB5;'>PÓRTICO © 2025 | Engenharia de Rentabilidade</p>", unsafe_allow_html=True)