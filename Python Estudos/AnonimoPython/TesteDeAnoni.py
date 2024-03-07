import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DF05175208D\SQLEXPRESS;"
    "Database=DnitHML;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")