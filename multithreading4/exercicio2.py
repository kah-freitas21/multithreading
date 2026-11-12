import multiprocessing
import time
import random

porta = None

def init(sema):
    global porta
    porta = sema

def pessoa(id):
    global porta

    pessoa_andando(id)  

    with porta:
        pessoa_passando(id) 

    pessoa_saindo(id)  

def pessoa_andando(id):
    velocidade = random.uniform(4, 6)

    distancia = 200
    tempo = distancia / velocidade

    print('Pessoa #', id, 'está caminhando.')
    print('Pessoa #', id, 'velocidade:', round(velocidade, 2), 'm/s')

    time.sleep(tempo)

    print('Pessoa #', id, 'chegou na porta.')

def pessoa_passando(id):
    print('Pessoa #', id, 'está abrindo e atravessando a porta.')

    tempo = random.uniform(1, 2)
    time.sleep(tempo)

    print('Pessoa #', id, 'atravessou a porta.')

def pessoa_saindo(id):
    print('Pessoa #', id, 'saiu.')

def main():
    parametros = [0]*4
    i = 0

    for i in range(0, 4, 1):
        parametros[i] = i + 1

    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)

        with multiprocessing.Pool(processes=4,initializer=init,initargs=(sem,)) as threads:
            threads.map(pessoa, parametros)

if (__name__ == '__main__'):
    main()