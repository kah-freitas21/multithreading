import multiprocessing
import time
import random

pista = None
equipes = None

def init(p, e):
    global pista
    global equipes
    pista = p
    equipes = e


def carro(parametro):
    global pista
    global equipes

    equipe = parametro[0]
    numero = parametro[1]

    with equipes[equipe-1]:

        with pista:
            carro_correndo(equipe, numero)

def carro_correndo(equipe, numero):

    print('Equipe #', equipe, '- Carro #', numero, 'entrou na pista.')

    for volta in range(1, 4, 1):

        tempo = random.uniform(1, 3)

        time.sleep(tempo)

        print('Equipe #', equipe, '- Carro #', numero,
              '- Volta #', volta, '- Tempo:', round(tempo, 2), 'segundos')

    print('Equipe #', equipe, '- Carro #', numero, 'terminou a corrida.')

def main():
    parametros = [0]*14
    i = 0
    equipe = 0
    carro_numero = 0

    for i in range(0, 14, 1):
        equipe = (i // 2) + 1
        carro_numero = (i % 2) + 1

        parametros[i] = (equipe, carro_numero)

    with multiprocessing.Manager() as gerenciador:

        sem_pista = gerenciador.Semaphore(5)

        sem_equipes = []

        for i in range(0, 7, 1):
            sem_equipes.append(gerenciador.Semaphore(1))

        with multiprocessing.Pool(processes=14,initializer=init,initargs=(sem_pista, sem_equipes)) as threads:
            threads.map(carro, parametros)

if (__name__ == '__main__'):
    main()