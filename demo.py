import random
import threading
import time

def worker(name):
    for i in range(5):
        print(f"{name} - Contador: {i + 1}")
        time.sleep(random.randint(1, 3))
    print(f"{name} - Completado")

def main():
    # Crear hilos
    t1 = threading.Thread(target=worker, args=("Hilo 1",))
    t2 = threading.Thread(target=worker, args=("Hilo 2",))
    t3 = threading.Thread(target=worker, args=("Hilo 3",))

    # Iniciar hilos
    t1.start()
    t2.start()
    t3.start()

    # Esperar a que los hilos terminen
    t1.join()
    t2.join()
    t3.join()

    print("Hilos completados")

if __name__ == "__main__":
    main()