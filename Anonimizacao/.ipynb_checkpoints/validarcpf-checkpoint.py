import pyodbc
from CondicaoCPF import Cpf

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DF05175208D\SQLEXPRESS;"
    "Database=DnitHML;"
)
conexao = pyodbc.connect(dados_conexao)

def consulta(conexao, sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado


ssql = "SELECT Cpf FROM Pessoa WHERE IdPessoa = 1"
resultado = consulta(conexao, ssql)

str_resultado = str(resultado)
cpf_ponto = str_resultado.replace(".","")
cpf_traco = cpf_ponto.replace("-","")
cpf_aspas = cpf_traco.replace("'", "")
cpf_parentese_esquerdo = cpf_aspas.replace("(", "")
cpf_parentese_direito = cpf_parentese_esquerdo.replace(")", "")
cpf_chaves_esquerda = cpf_parentese_direito.replace("[", "")
cpf_chaves_direita = cpf_chaves_esquerda.replace("]", "")
cpf = cpf_chaves_direita.replace(",", "")

objeto_cpf = Cpf(cpf)
