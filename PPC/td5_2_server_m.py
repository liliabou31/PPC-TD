import sysv_ipc
import datetime
import time
from concurrent.futures import ThreadPoolExecutor

# Clé de la file de messages
KEY = 666

# Création ou récupération de la queue
mq = sysv_ipc.MessageQueue(KEY, sysv_ipc.IPC_CREAT)

# Fonction qui traite une requête client
def handle_client(message):
    try:
        pid = int(message.decode())
        dt = str(datetime.datetime.now())
        time.sleep(0.5)  # simule un traitement
        mq.send(dt.encode(), type=pid+3)
        print(f"Served client {pid} with date/time {dt}")
    except Exception as e:
        print("Error handling client:", e)

print("Server started...")

# Thread pool avec un nombre fixe de threads
MAX_WORKERS = 8
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

try:
    while True:
        message, msg_type = mq.receive()  # bloque jusqu'à un message
        if msg_type == 2:  # signal d'arrêt
            print("Termination signal received, shutting down.")
            break
        # Soumettre la tâche au pool de threads
        executor.submit(handle_client, message)
finally:
    mq.remove()
    executor.shutdown(wait=True)
