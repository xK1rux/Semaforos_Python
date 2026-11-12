import multiprocessing
import time
import random

chegada: int = 0
passou: int = 0
sema: None

def init(c, p, sem):
    global chegada, passou, sema
    chegada = c
    passou = p
    sema = sem
    
def pessoas(id):
    global sema
    
    pessoa_andando(id)
    with sema:
        pessoa_passando(id)
    pessoa_passou(id)
    
def pessoa_andando(id):
    global chegada
    dist_perc: float = 0.0
    dist_total: int = 0
    dist_andar: float = 0.0
    
    dist_total = 200
    while dist_perc < dist_total:
        dist_andar = random.randint(400, 600)
        dist_andar = dist_andar / 100
        dist_perc += dist_andar
        print(f"A pessoa #{id} andou {dist_andar:.2f} metros e percorreu {dist_perc:.2f} metros")
        time.sleep(1)
    chegada.value += 1
    print(f"A pessoa #{id} foi o {chegada.value}º a chegar na porta.")
    
def pessoa_passando(id):
    global passou
    tempo: float = 0.0
    
    tempo = random.randint(1000, 2000)
    tempo = tempo / 1000
    passou.value += 1
    print(f"A pessoa #{id} foi a {passou.value}º a passar pela porta.")
    time.sleep(tempo)
    
def pessoa_passou(id):
    print(f"A pessoa #{id} passou pela porta.")
    
def main():
    params: int = [0]*4
    pos_chegada: int = 0
    pos_passou: int = 0
    semaforo = None
    
    pos_chegada = multiprocessing.Value('i', 0)
    pos_passou = multiprocessing.Value('i', 0)
    
    for i in range(4):
        params[i] = (i + 1)
        
    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(pos_chegada, pos_passou, semaforo)) as threads:
            threads.map(pessoas, params)

if __name__ == '__main__':
    main()