
import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Demo: Chat de 1 página", page_icon="🤖", layout="centered")
st.title("🤖 Demo de Modelo – 1 página")
st.write("App mínima con Streamlit. Escribe un mensaje y el modelo responde.")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.info("No encuentro OPENAI_API_KEY. Si estás en local, define la variable de entorno o usa 'Run → Set Secrets' en Streamlit Cloud.")
client = OpenAI(api_key=api_key) if api_key else None

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Escribe tu pregunta…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if not client:
            st.error("Falta la API key. Configúrala y vuelve a intentar.")
        else:
            with st.spinner("Pensando…"):
                resp = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    temperature=0.2,
                )
                output = resp.choices[0].message.content
                st.markdown(output)
            st.session_state.messages.append({"role": "assistant", "content": output})

st.caption("Ejemplo simple con Streamlit. Una sola página, sin backend adicional.")
