#from langchain import LLM
from langchain.llms import LLM

# Carrega o modelo de linguagem
llm = LLM("gpt-3")

# Gera texto
texto = llm.generate("Olá, mundo!")

# Imprime o texto gerado
print(texto)