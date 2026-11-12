from mimetypes import init
import multiprocessing
import time
import random

chegada: int = 0

def init(c):
    global chegada
    chegada = c

def sapos(id, dist_percorrida):
    dist_percurso: int = 30
    dist_salto: float = 0.0
    dist_maxsalto: int = 0

    while dist_percorrida < dist_percurso:
        dist_maxsalto = random.randint(10, 50)
        dist_salto = random.randint(0, dist_maxsalto)
        dist_salto = dist_salto / 10
        dist_percorrida += dist_salto
        print(f"O sapo #{id} saltou {dist_salto:.1f} metros e percorreu {dist_percorrida:.1f} metros")
        time.sleep(0.5)
    chegada.value += 1
    print(f" O sapo #{id} foi o {chegada.value}º a chegar ao final do percurso!")
    
def main():
    params = [(0, 0)] * 5
    distancia: int = 0
    pos_chegada: int = 0
    
    pos_chegada = multiprocessing.Value('i', 0)

    for i in range(5):
        params[i] = (i + 1, distancia)
        
    with multiprocessing.Pool(processes=5, initializer=init, initargs=(pos_chegada, )) as threads:
        threads.starmap(sapos, params)


if __name__ == "__main__":
    main()