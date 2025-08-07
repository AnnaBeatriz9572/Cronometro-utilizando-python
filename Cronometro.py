import time
import os #usado para interagir com o sistema operacional

class Cronometro:
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1
    def start(self):
        while True:
            os.system('cls') #utilizado para limpar o terminal toda vez que atualizar o cronometro
            print(self)
            self.incremento()
            time.sleep(1) #biblioteca time, pausa a execução por 1 segundo

cronometro1 = Cronometro()
cronometro1.start()
