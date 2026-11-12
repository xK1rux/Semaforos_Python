import multiprocessing
import time

sentido: int = 0
sema: None 

def init(sen, sem):
    global sentido
    global sema
    sentido = sen
    sema = sem

def carros(id):
    global sentido
    global sema
    senti: str = ''
    sentidos: str = ['Baixo', 'Esquerda', 'Cima', 'Direita']
    
    with sema:
        sentido.value = id
        for i in range(sentido.value):
            senti = sentidos[i]
        print(f"O carro #{id} está indo para o sentido {senti}")
        time.sleep(0.5)
        print(f"Passagem liberada para o próximo carro.")
    
def main():
    params: int = [0]*4
    sent: int = 0
    semaforo = None
    sent = multiprocessing.Value('i', 0)
    
    for i in range(4):
        params[i] = (i + 1)
    
    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sent, semaforo)) as threads:
            threads.map(carros, params)
    
    

if __name__ == "__main__":
    main()