import sqlite3
from dao.dao_factory import DAOFactory

from dao.sqlite_clima_dao import SqliteClimaDao


class SqliteDAOFactory(DAOFactory):
    URL_BD = 'data/clima_api.db'

    @staticmethod
    def criar_conexao():

        conexao = None

        try:
            conexao = sqlite3.connect(SqliteDAOFactory.URL_BD)
        except sqlite3.Error as err:
            raise Exception(err)

        return conexao

    @property
    def dao_factory(self) -> DAOFactory:
        return SqliteDAOFactory()

    @property
    def clima_dao(self):
        return SqliteClimaDao()
