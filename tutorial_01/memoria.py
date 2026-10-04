import time
import os

print("Reservando memoria...")

datos = [0] * 50_000_000

print("Memoria reservada.")
print("PID:", os.getpid())

time.sleep(60)