import sqlite3
import dao.sqlite_dao_factory as dao

from dao.clima_dao import ClimaDao


class SqliteClimaDao(ClimaDao):

    def adicionar(self, clima):
        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        query = 'INSERT INTO Clima VALUES (null,?,?,?,?)'
        registro = (clima.temperatura, clima.umidade, clima.condicao_tempo, clima.velocidade_vento_km, clima.data_hora)

        try:
            cursor.execute(query, registro)
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

    def selecionar_clima(self, limit=10) -> list:
        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        query = 'SELECT * FROM Clima ORDER BY data_hora LIMIT ?'

        try:
            dados = cursor.execute(query, (limit, )).fetchall()
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

    def excluir(self, id):
        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        query = 'DELETE FROM Clima WHERE id_clima = ?'

        try:
            cursor.execute(query, (id, ))
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

    def buscar_clima_hoje(self):
        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        query = 'SELECT * FROM Clima WHERE DATE(data_hora) = DATE()'

        try:
            dados = cursor.execute(query).fetchone()
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

        return dados