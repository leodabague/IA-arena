# OpenAI GPT-o1 | 1ª iteração
# Script criado consultando o modelo lançado no dia 05/12

import ollama

pergunta = 'Me dê 5 ideias de projetos uteis usando streamlit e ollama'
response = ollama.chat(
    'llama3.1',
    messages=[{'role': 'user', 'content': pergunta}]
)

# Print only the assistant's content
print(response.message.content)
