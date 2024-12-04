# LLM: qwen2.5-coder | running locally
# Usando o modelo do Alibaba rodando localmente na minha GPU (RTX 3060)
import ollama

pergunta = 'Me dê 5 ideias de projetos uteis usando streamlit e ollama'

response = ollama.chat(
    'llama3.1',
    messages=[{'role': 'user', 'content': pergunta}]
)

content = response.message.content
lines = content.split('\n')

for line in lines:
    print(line.strip())
