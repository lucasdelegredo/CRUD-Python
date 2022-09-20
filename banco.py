import sqlite3 as sqlite

conexao = sqlite.connect('equipamentos.db')

with conexao: #abre e fecha dados automaticamente
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE TB_EQUIPAMENTOS(TAG TEXT PRIMARY KEY, TIPO TEXT, MARCA TEXT, MODELO TEXT, DTA_FABR DATE, VALOR DECIMAL, CC TEXT, AREA TEXT, OBS TEXT)")