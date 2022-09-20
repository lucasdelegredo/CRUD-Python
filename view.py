import sqlite3 as sqlite

#conexao
conexao = sqlite.connect('equipamentos.db')

#CRUD
#C - CREATE
#R - READ
#U - UPDATE
#D - DELETE

lista = ['EG008','Empilhadeira Combustao','TOYOTA','8FG25','01/01/2011',180000.00,'3241','Manutencao','']

#inserir informações
def insert_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO TB_EQUIPAMENTOS(TAG,TIPO,MARCA,MODELO,DTA_FABR,VALOR,CC,AREA,OBS) VALUES (?,?,?,?,?,?,?,?,?)"
        cursor.execute(query,i)


#acessar informações
def view_info():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM TB_EQUIPAMENTOS"
        cursor.execute(query)
        eqpto = cursor.fetchall() #pega tudo oq estiver no cursor
        
        for i in eqpto:
            lista.append(i)
    return lista

#lista = ['Teste','EG005']

#atualizar informações
#with conexao:
    #cursor = conexao.cursor()
    #query = "UPDATE TB_EQUIPAMENTOS SET TIPO=? WHERE TAG=?"
    #cursor.execute(query,lista)

#lista = ['EG005']
#Deletar informacoes 
def delete_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM TB_EQUIPAMENTOS WHERE TAG=?"
        cursor.execute(query,i)