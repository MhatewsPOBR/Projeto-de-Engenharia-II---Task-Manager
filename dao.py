import sqlite3

from colorama import Cursor

from models import Tarefa, Usuario

# SQL

# Criação
SQL_CRIA_TAREFA = 'INSERT into TAREFA (NOME, DESCRICAO, TIPO, STATUS, PRIORIDADE) values (?, ?, ?, ?, ?)'

SQL_CRIA_USUARIO = 'INSERT into USUARIO (USERNAME, EMAIL, SENHA) values (?, ?, ?)'

# Atualização
SQL_ATUALIZA_TAREFA = 'UPDATE TAREFA SET NOME = ?, DESCRICAO = ?, TIPO = ?, STATUS = ?, PRIORIDADE = ? where ID = ?'

SQL_ATUALIZA_USUARIO = 'UPDATE USUARIO SET USERNAME = ?, EMAIL = ?, SENHA = ? where ID = ?'


class TarefaDao:
    def __init__(self, db) -> None:
        self.__db = db

    def salvar(self, tarefa):
        cursor = self.__db.cursor()

        if (tarefa._id):
            cursor.execute(SQL_ATUALIZA_TAREFA, (tarefa._nome, tarefa._descricao, tarefa._tipo, tarefa._status, tarefa._prioridade))

        else:
            cursor.execute(SQL_CRIA_TAREFA, (tarefa._nome, tarefa._descricao, tarefa._tipo, tarefa._status, tarefa._prioridade))

        self.__db.commit()
        return tarefa
    

class UsuarioDao:
    def __init__(self, db) -> None:
        self.__db = db
        
    def salvar_usuario(self, usuario):
        cursor = self.__db.cursor()
        
        if (usuario._id):
            cursor.execute(SQL_ATUALIZA_USUARIO, (usuario._nome, usuario._email, usuario._senha, usuario._id))
            
        else:
            cursor.execute(SQL_CRIA_USUARIO, (usuario._nome, usuario._email, usuario._senha))
            
        self.__db.commit()
        return usuario