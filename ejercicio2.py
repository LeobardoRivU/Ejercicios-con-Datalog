from pyDatalog import pyDatalog
from pyDatalog import create_terms

pyDatalog.clear()
create_terms('N, D, es_primo, divisor_existe, X')

# 1. Definir operador Python personalizado: divisible por
@pyDatalog.program()
def _():
    es_divisible_por(N, D) <= (N % D == 0)

# 2. Un número tiene divisor si existe D en [2, N-1] tal que N % D == 0
@pyDatalog.program()
def _():
    divisor_existe(N) <= (D in range(2, N)) & es_divisible_por(N, D)

# 3. Es primo si es > 1 y NO tiene ningún divisor en [2, N-1]
@pyDatalog.program()
def _():
    es_primo(N) <= (N > 1) & ~divisor_existe(N)

# --- Pruebas ---
print("Número → ¿Es primo?")
print("-" * 25)

numeros = [1, 2, 3, 4, 5, 15, 17, 19, 23, 97, 100]

for n in numeros:
    # Consulta correcta en la versión actual
    resultado = es_primo(n)
    print(f"{n:3d} → {'Primo' if resultado else 'No primo'}")