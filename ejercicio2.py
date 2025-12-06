from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms('N, es_primo, no_primo')

def es_primo_logica(n):
    if n <= 1:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


numeros = [1, 2, 3, 4, 5, 15, 17]
for n in numeros:
    if es_primo_logica(n):
        pyDatalog.assert_fact('es_primo', n)
    else:
        pyDatalog.assert_fact('no_primo', n)

es_primo(N) <= es_primo(N)
no_primo(N) <= no_primo(N)

print("Número → ¿Es primo?")
print("-" * 25)
for n in numeros:
    resultado = pyDatalog.ask(f'es_primo({n})')
    print(f"{n:4d} → {'Primo' if resultado else 'No primo'}")

# Bonus: todos los primos hasta 100 (mezcla lógica + hechos)
print("\nPrimos del 2 al 100:")
primos = [n for n in range(2, 101) if es_primo_logica(n)]
print(primos)