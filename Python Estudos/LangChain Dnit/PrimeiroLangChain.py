from langchain import LLM

# Carregar o modelo de linguagem
llm = LLM("bard-base")

# Gerar texto
texto = llm.generate("Escreva um poema sobre a natureza.")

# Imprimir o texto gerado
print(texto)
