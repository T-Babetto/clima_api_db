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
    noite_dia = str(dados['currently'])
    nascer_do_sol = str(dados['sunrise'])
    por_do_sol = str(dados['sunset'])
    min_temperatura = float(dados['forecast'][4]['min'])
    max_temperatura = float(dados['forecast'][3]['max'])
    data_hora = str(datetime.now())
    media_temperatura = (min_temperatura + max_temperatura) / 10
    return Clima(temperatura=temperatura, umidade=umidade, condicao_tempo=condicao_tempo,
                 velocidade_vento_km=velocidade_vento_km, noite_dia=noite_dia, nascer_do_sol=nascer_do_sol,
                 por_do_sol=por_do_sol, min_temperatura=min_temperatura, max_temperatura=max_temperatura,
                 media_temperatura=media_temperatura, data_hora=data_hora)


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
    print(f'Condição do tempo: {clima_hoje.condicao_tempo}')
    print(f'Período: {clima_hoje.noite_dia}')
    print(f'Umidade: {clima_hoje.umidade}')
    print(f'Velocidade do vento: {clima_hoje.velocidade_vento_km}')
    print(f'Nascer do Sol: {clima_hoje.nascer_do_sol}')
    print(f'Pôr do Sol: {clima_hoje.por_do_sol}')
    print(f'Média de temperaturas: {clima_hoje.media_temperatura}')
    print('Digite o UF do estado ou nome da cidade ou sair para SAIR:')

    resultado_clima = str(input('UF ou Cidade:'))

    if resultado_clima != 'sair':
        print(f'\n Temperatura: {clima_hoje.temperatura}')
        print(f'\n Umidade {clima_hoje.umidade}')
        print(f'\n Condição do tempo: {clima_hoje.condicao_tempo}')
        print(f'\n Velocidade do vento: {clima_hoje.velocidade_vento_km}')
        print('\n')
        mostrar_menu()
    else:
        sys.exit('Encerrando o programa...')


if __name__ == '__main__':
    sqliteFactory = SqliteDAOFactory()
    climaDAO = sqliteFactory.clima_dao
    clima_hoje = carregar_clima_hoje()
    mostrar_menu()
