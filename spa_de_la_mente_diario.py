import streamlit as st
import openai

st.set_page_config(page_title="Diario Emocional | Spa de la Mente", layout="centered")

st.title("🧘‍♂️ Diario Emocional - Spa de la Mente")
st.markdown("Escribí cómo te sentís hoy y recibí una devolución íntima, terapéutica y espiritual...")

openai.api_key = st.secrets["OPENAI_API_KEY"]

entrada_usuario = st.text_area("🪷 ¿Qué te gustaría expresar hoy?", height=200)

if st.button("Enviar"):
    if not entrada_usuario.strip():
        st.warning("Por favor, escribí algo.")
    else:
        with st.spinner("Conectando con el Spa de la Mente..."):
            prompt = f"""
Eres un terapeuta empático, espiritual y cálido. Mezclas psicología clínica, sabiduría oriental y contención emocional. 
Responde como si fueras el creador de Spa de la Mente. El usuario te comparte lo siguiente:

"{entrada_usuario}"

Ofrece una devolución corta, amorosa, introspectiva y transformadora. No des consejos directos. Usá frases suaves, metafóricas o simbólicas.
"""

            try:
                respuesta = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8,
                    max_tokens=300
                )
                texto_ia = respuesta["choices"][0]["message"]["content"].strip()
                st.markdown("### 🌸 Devolución del Spa de la Mente")
                st.success(texto_ia)
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
