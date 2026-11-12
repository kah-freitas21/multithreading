import multiprocessing
import time
import random

semaforo = None

def init(sema):
    global semaforo
    semaforo = sema

def carro(id):
    global semaforo

    if id == 1:
        sentido = 'Norte'
    elif id == 2:
        sentido = 'Sul'
    elif id == 3:
        sentido = 'Leste'
    else:
        sentido = 'Oeste'

    carro_andando(id) 
    with semaforo:
        carro_passando(id, sentido)  

    carro_saindo(id)  

def carro_andando(id):
    print('Carro #', id, 'está se aproximando do cruzamento')
    time.sleep(random.uniform(0.5, 2))

def carro_passando(id, sentido):
    print('Carro #', id, 'está passando no sentido', sentido)
    time.sleep(2)

def carro_saindo(id):
    print('Carro #', id, 'saiu do cruzamento')

def main():
    parametros = [0]*4
    i = 0

    for i in range(0, 4, 1):
        parametros[i] = i + 1

    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)

        with multiprocessing.Pool(
            processes=4,
            initializer=init,initargs=(sem,)) as threads:threads.map(carro, parametros)

if (__name__ == '__main__'):
    main()
