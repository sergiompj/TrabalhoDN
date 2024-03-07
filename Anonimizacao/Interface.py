import requests
from tkinter import *

janela = Tk()
janela.title("Teste de Janela")

texto_orientacao = Label(janela, text="clique no botao para executar a ação")
texto_orientacao.grid(column=0, row=0)


janela.mainloop()