class Clima:

    def __init__(self, id: int = -1, temperatura: complex = 0.0, umidade: complex = 0.0, condicao_tempo: str = "", velocidade_vento_km: complex = 0.0, data_hora: str = "") -> None:
        super().__init__()
        self.__id = id
        self.__temperatura = temperatura
        self.__umidade = umidade
        self.__condicao_tempo = condicao_tempo
        self.__velocidade_vento_km = velocidade_vento_km
        self.__data_hora = data_hora

    @property
    def id(self):
        return self.__id

    @property
    def temperatura(self):
        return self.__temperatura

    @property
    def umidade(self):
        return self.__umidade

    @property
    def condicao_tempo(self):
        return self.__condicao_tempo

    @property
    def velocidade_vento_km(self):
        return self.__velocidade_vento_km

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def clima(self) -> dict:
        return {
            'temperatura': self.__temperatura,
            'umidade': self.__umidade,
            'condicao_tempo': self.__condicao_tempo,
            'velocidade_vento_km': self.__velocidade_vento_km,
            'data_hora': self.__data_hora
        }

    def __str__(self) -> str:
        return f'{self.__data_hora}, {self.__temperatura} °C,  {self.__umidade} %, {self.__condicao_tempo}, {self.__velocidade_vento_km} '

