# LLM: Gemma2 | running locally ** o Claude teve que corrigir, porque o Gemma estava dando erro **
# Script gerado pelo Google Gemma2 e corrigido pelo Claude rodando localmente com uma GPU (RTX 3060)
# mesmo após 3 iterações o google não tinha conseguido produzir um script funcional

import streamlit as st
import ollama  

st.title("Streamlit and Ollama Project Ideas")

pergunta = 'Me dê 5 ideias de projetos úteis usando streamlit e ollama'  
response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': pergunta}])

message_content = response['message']['content']

projects = message_content.split("\n\n")[1:] 

for i, project in enumerate(projects):
    st.header(f"Project {i+1}")
    st.markdown(project)
