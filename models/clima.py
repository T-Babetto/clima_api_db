class Clima:

    def __init__(self, id: int = -1, temperatura: float = 0.0, umidade: float = 0.0,
                 condicao_tempo: str = "", noite_dia: str = "", nascer_do_sol: str = "",
                 por_do_sol: str = "", min_temperatura: float = 0.0, max_temperatura: float = 0.0,
                 media_temperatura:float = 0.0, velocidade_vento_km: str = "",
                 data_hora: str = "") -> None:
        super().__init__()
        self.__id = id
        self.__temperatura = temperatura
        self.__umidade = umidade
        self.__condicao_tempo = condicao_tempo
        self.__noite_dia = noite_dia
        self.__nascer_do_sol = nascer_do_sol
        self.__por_do_sol = por_do_sol
        self.__min_temperatura = min_temperatura
        self.__max_temperatura = max_temperatura
        self.__media_temperatura = media_temperatura
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
    def noite_dia(self):
        return self.__noite_dia

    @property
    def nascer_do_sol(self):
        return self.__nascer_do_sol

    @property
    def por_do_sol(self):
        return self.__por_do_sol

    @property
    def min_temperatura(self):
        return self.__min_temperatura

    @property
    def max_temperatura(self):
        return self.__max_temperatura

    @property
    def media_temperatura(self):
        return self.__media_temperatura

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
            'noite_dia': self.__noite_dia,
            'nascer_do_sol': self.__nascer_do_sol,
            'por_do_sol': self.__por_do_sol,
            'min_temperatura': self.__min_temperatura,
            'max_temperatura': self.__max_temperatura,
            'media_temperatura': self.__media_temperatura,
            'velocidade_vento_km': self.__velocidade_vento_km,
            'data_hora': self.__data_hora
        }

    def __str__(self) -> str:
        return f'{self.__data_hora}, {self.__temperatura} °C,  {self.__umidade} %, {self.__condicao_tempo}, {self.__velocidade_vento_km} '

