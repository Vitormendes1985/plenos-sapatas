
import streamlit as st

def calcular_area(largura, comprimento):
    return largura * comprimento

def obter_preco(tipo, area):
    precos = {
        'pleno': {
            'Normal': 10,
            'Normal com patilhas de suporte': 12,
            'Pleno irregular': 15,
            'Todo Fechado': 20,
        },
        'sapata': {
            'Normal': 8,
            'Irregular': 14,
        }
    }
    return area * precos[tipo_base][tipo_escolhido]

st.title("Cálculo de Plenos e Sapatas")

# Escolher o tipo de elemento
col1, col2 = st.columns(2)
with col1:
    tipo_base = st.selectbox("Escolhe o tipo de elemento:", ["pleno", "sapata"])

# Opções dependentes do tipo
tipos_disponiveis = {
    "pleno": ["Normal", "Normal com patilhas de suporte", "Pleno irregular", "Todo Fechado"],
    "sapata": ["Normal", "Irregular"]
}

with col2:
    tipo_escolhido = st.selectbox("Escolhe o subtipo:", tipos_disponiveis[tipo_base])

# Inputs
largura = st.number_input("Largura (A) [m]", min_value=0.0, step=0.1)
comprimento = st.number_input("Comprimento (B) [m]", min_value=0.0, step=0.1)
altura = st.number_input("Altura (C) [m]", min_value=0.0, step=0.1)

if st.button("Calcular"):
    area = calcular_area(largura, comprimento)
    preco = obter_preco(tipo_base, area)

    st.success(f"Área: {area:.2f} m²")
    st.info(f"Preço estimado: € {preco:.2f}")
