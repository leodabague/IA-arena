# OpenAI GPT-o1 | 2ª iteração
# Script criado consultando o modelo lançado no dia 05/12

import streamlit as st
import ollama

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="OLLAMA + Streamlit Chat",
    page_icon="🤖",
    layout="centered"
)

# Title and instructions
st.title("🤖 OLLAMA Chat Interface")
st.markdown("""
Welcome! Ask any question, and I'll respond using the OLLAMA model.
- Type your query below and press "Submit".
- If you'd like to refine or change the response, press "Regenerate".
""")

# Initialize session state for conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input area
with st.form(key='query_form'):
    user_input = st.text_area("Your question:", placeholder="e.g., 'Me dê 5 ideias de projetos úteis usando Streamlit e OLLAMA'")
    submitted = st.form_submit_button("Submit")

# Handle user submission
if submitted and user_input.strip():
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show a spinner while waiting for the response
    with st.spinner("Estou pensando..."):
        response = ollama.chat(
            "llama3.1",
            messages=st.session_state.messages
        )
    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": response.message.content})

# Display the conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Assistant:** {msg['content']}")

# Regenerate Button
if st.session_state.messages:
    if st.button("Regenerate"):
        # Remove the last assistant message and resend the last user message
        # to produce a new response
        if st.session_state.messages[-1]["role"] == "assistant":
            st.session_state.messages.pop()

        with st.spinner("Gerando uma nova resposta..."):
            response = ollama.chat(
                "llama3.1",
                messages=st.session_state.messages
            )
        st.session_state.messages.append({"role": "assistant", "content": response.message.content})
        st.experimental_rerun()
