# LLM: gpt4o-mini | running in the cloud
# Script gerado com o modelo mais barato da OpenAI

import ollama
import json

def main():
    pergunta = 'Me dê 5 ideias de projetos uteis usando streamlit e ollama'
    response = ollama.chat(
        'llama3.1',
        messages=[{'role': 'user', 'content': pergunta}]
    )
    
    if hasattr(response, 'message'):
        content = response.message.content
        print("\n=== Resposta do Assistente ===\n")
        print(content)
    else:
        print("Resposta inesperada do modelo:")
        print(response)

if __name__ == "__main__":
    main()

    print("No response content found!")
