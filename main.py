import locale
import sys
from datetime import datetime
import config
import requests
from dao.sqlite_dao_factory import SqliteDAOFactory

from models.clima import Clima

URL_BASE = f'https://api.hgbrasil.com/weather?key={config.api_key}'

locale.setlocale(locale.LC_ALL, '')
data_hora_hoje = str(datetime.today().date().strftime('%A, %x'))
climaDAO = None
clima_hoje = None


def consultar_dados_climaticos() -> Clima:
    requisicao = requests.get(URL_BASE)
    dados = requisicao.json()['results']

    temperatura = float(dados['temp'])
    umidade = float(dados['humidity'])
    condicao_tempo = str(dados['description'])
    velocidade_vento_km = str(dados['wind_speedy'])
    data_hora = str(datetime.now())
    return Clima(temperatura=temperatura, umidade=umidade, condicao_tempo=condicao_tempo,
                 velocidade_vento_km=velocidade_vento_km, data_hora=data_hora)


def salvar_clima(clima) -> None:
    climaDAO.adicionar(clima)


def carregar_clima_hoje() -> Clima:
    registro_clima_hoje = climaDAO.buscar_clima_hoje()

    if registro_clima_hoje is None:
        clima = consultar_dados_climaticos()
        salvar_clima(clima)
        return clima
    else:
        registro_clima_hoje = climaDAO.buscar_clima_hoje()
        return Clima(registro_clima_hoje[0], registro_clima_hoje[1],
                       registro_clima_hoje[2], registro_clima_hoje[3])


def mostrar_menu():
    print(f'Clima - {data_hora_hoje}')
    print(f'Temperatura: {clima_hoje.temperatura}')
    print(f'Umidade: {clima_hoje.umidade}')
    print(f'Condição do tempo: {clima_hoje.condicao_tempo}')
    print(f'Vento: {clima_hoje.velocidade_vento_km}')
    print('Digite o UF do estado ou nome da cidade ou sair para SAIR:')

    resultado_clima = str(input('UF ou Cidade:'))

    if resultado_clima != 'sair':
        print(f'\n {clima_hoje.temperatura}')
        print(f'\n {clima_hoje.umidade}')
        print(f'\n {clima_hoje.condicao_tempo}')
        print(f'\n {clima_hoje.velocidade_vento_km}')
        print('\n')
        mostrar_menu()
    else:
        sys.exit('Encerrando o programa...')


if __name__ == '__main__':
    sqliteFactory = SqliteDAOFactory()
    climaDAO = sqliteFactory.clima_dao
    clima_hoje = carregar_clima_hoje()
    mostrar_menu()