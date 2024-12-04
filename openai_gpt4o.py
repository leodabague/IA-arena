# LLM: gpt4o | running in the cloud
# Rodando o modelo flagship da OpenAI na nuvem
import ollama

pergunta = 'Me dê 5 ideias de projetos uteis usando streamlit e ollama'

response = ollama.chat(
    'llama3.1',
    messages=[{'role': 'user', 'content': pergunta}]
)

if response.message and response.message.content:
    formatted_response = response.message.content.strip()
    print("\n--- Formatted Response ---\n")
    print(formatted_response)
else:
    print("No response content found!")
