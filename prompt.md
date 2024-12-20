# Usando um mesmo prompt com várias LLMs e comparando o resultado

## Prompt utlizado:

### I’m using the new ollama python integration.
    
Script python utilizado:
```
    import ollama
    pergunta = 'Me dê 5 ideias de projetos uteis usando streamlit e ollama'
    response = ollama.chat(
        'llama3.1',
        messages=[{'role': 'user', 'content': pergunta}]
    )
    print(response)
```

### This is the result:
(venv) PS G:\leo\python\nfe> python test.py
model='llama3.1' created_at='2024-12-02T13:38:09.7207759Z' done=True done_reason='stop' total_duration=38908693200 load_duration=20523722100 prompt_eval_count=31 prompt_eval_duration=167000000 eval_count=1056 eval_duration=18215000000 message=Message(role='assistant', content=
```
Aqui estão 5 ideias de projetos úteis que você pode criar utilizando Streamlit e OLLAMA (ou qualquer outra biblioteca de IA ou modelo de aprendizado de máquina):\n\n1. Recomendação de Produtos :\n - Descrição : Desenvolva uma aplicação que utilize o poder da IA para recomendar produtos baseados nas preferências do usuário.\n - Ferramentas Utilizadas :\n - Streamlit: Para criar a interface do usuário e renderizar os resultados dos modelos de aprendizado de máquina.\n - OLLAMA ou outro modelo de classificação (por exemplo, sklearn): Para treinar um modelo que faça predições sobre as preferências do usuário com base em suas interações.\n - Funcionalidades :\n - Permitir aos usuários fornecer informações sobre seus gostos e histórico de compras.\n - Utilizar o modelo de aprendizado de máquina para fornecer recomendações personalizadas dos produtos.\n\n2. Análise de Sentimentos em Texto :\n - Descrição : Desenvolva uma ferramenta que analisa o tom e a opinião expressa em textos, como artigos, revisões ou comunicações sociais.\n - Ferramentas Utilizadas :\n - Streamlit: Para criar um interface amigável para que os usuários possam inserir o texto e visualizar os resultados.\n - OLLAMA ou outro modelo de NLP (por exemplo, NLTK, spaCy): Para analisar sentimentos nos textos e fornecer uma pontuação (positiva, negativa ou neutra).\n - Funcionalidades :\n - Permitir que os usuários insiram um texto para ser avaliado.\n - Mostrar a análise de sentimento com base no conteúdo do texto.\n\n3. Previsão do Preço de Imóveis :\n - Descrição : Desenvolva uma ferramenta que utiliza técnicas de aprendizado de máquina para prever o preço de imóveis com base em características como número de quartos, metros quadrados, localização e outros fatores.\n - Ferramentas Utilizadas :\n - Streamlit: Para criar a interface do usuário para inserir os dados dos imóveis e visualizar as previsões.\n - OLLAMA ou outro modelo regressor (por exemplo, scikit-learn): Para treinar um modelo que faça predições sobre o preço de imóveis com base nos dados inseridos.\n - Funcionalidades :\n - Permitir aos usuários fornecer os detalhes dos imóveis (características e localização).\n - Utilizar o modelo para prever os preços dos imóveis.\n\n4. Classificação de Músicas :\n - Descrição : Desenvolva uma aplicação que utilize técnicas de aprendizado de máquina para classificar músicas em categorias como gêneros, ritmos ou tempos.\n - Ferramentas Utilizadas :\n - Streamlit: Para criar a interface do usuário e permitir aos usuários carregar ou inserir nomes de músicas para serem classificadas.\n - OLLAMA ou outro modelo de classificação (por exemplo, scikit-learn): Para treinar um modelo que faça predições sobre as categorias das músicas com base em suas características (gênero, estilo, tempo, etc.).\n - Funcionalidades :\n - Permitir aos usuários inserirem nomes de músicas para serem classificadas.\n - Mostrar a classificação feita pelo modelo.\n\n5. Previsão do Tempo :\n - Descrição : Desenvolva uma aplicação que utilize dados meteorológicos e modelos de aprendizado de máquina para prever o tempo futuro em uma região específica ou cidade.\n - Ferramentas Utilizadas :\n - Streamlit: Para criar a interface do usuário e permitir aos usuários selecionarem locais para obter previsões.\n - OLLAMA ou outro modelo de regressão (por exemplo, scikit-learn): Para treinar um modelo que faça predições sobre as condições climáticas futuras com base em dados históricos e/ou informações meteorológicas atuais.\n - Funcionalidades :\n - Permitir aos usuários selecionarem locais para obter previsões de tempo.\n - Mostrar as previsões do modelo.\n\nLembre-se, cada projeto pode requerer ajustes significativos dependendo da complexidade dos dados e das tarefas a serem realizadas. Além disso, é sempre uma boa ideia testar seus modelos com diferentes conjuntos de dados para avaliar seu desempenho em condições reais.
```
, images=None, tool_calls=None)

### And the response is not pretty.
`How can I optimize the script to have a pretty / normalized response?`
