# LLM: sonnet | running in the cloud
# Script gerado pelo modelo top de linha da Anthropic

import ollama
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

def get_ai_response(prompt):
    response = ollama.chat(
        'llama3.1',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.message.content

def format_response(text):
    console = Console()
    md = Markdown(text)
    panel = Panel(
        md,
        title="AI Response",
        border_style="blue",
        padding=(1, 2)
    )
    console.print(panel)

def main():
    # Your prompt
    prompt = 'Me dê 5 ideias de projetos uteis usando streamlit e ollama'
    response = get_ai_response(prompt)
    format_response(response)

if __name__ == "__main__":
    main()
