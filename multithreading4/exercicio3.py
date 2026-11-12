import threading
import random
import time

def sapo(id):
    distancia = 0

    while distancia < 30:
        salto = random.randint(0, 5)

        distancia = distancia + salto

        if distancia > 30:
            distancia = 30

        print('Sapo #', id, 'pulou', salto, 'cm. Percorreu:', distancia, 'cm.')

        time.sleep(0.5)

    print('Sapo #', id, 'chegou na posição', distancia, 'cm!')

def main():
    threads = [None]*5
    i = 0

    for i in range(0, 5):
        threads[i] = threading.Thread(target=sapo, args=(i+1,))
        threads[i].start()

    for i in range(0, 5):
        threads[i].join()

    print('Corrida finalizada!')

if (__name__ == '__main__'):
    main()
