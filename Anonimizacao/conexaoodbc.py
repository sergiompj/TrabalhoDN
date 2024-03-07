import pyodbc

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

for r in resultado:
    print(r)

#comando = """INSERT INTO Pessoa(IdPessoa, Nome, Sexo ,Cpf, Rg, Tel_cel, Tel_res, Email ,dt_nascimento)
#VALUES
#	(3, 'Bruno Santos', 'M', '698.548.541-74', '3.568.598', '61984575884', '6140028922', 'bruno.santos@gmail.com', '05/04/2000')"""
#cursor.execute(comando)
#cursor.commit()