import sqlite3

from models import Tarefa, Usuario


# SQL

# Criação
SQL_CRIA_TAREFA = 'INSERT into TAREFA (NOME, DESCRICAO, TIPO, STATUS, PRIORIDADE) values (?, ?, ?, ?, ?)'

# Atualização
SQL_ATUALIZA_TAREFA = 'UPDATE TAREFA SET NOME = ?, DESCRICAO = ?, TIPO = ?, STATUS = ?, PRIORIDADE = ? where ID = ?'


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