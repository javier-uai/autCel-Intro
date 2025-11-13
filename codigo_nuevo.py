import random

### Bienvenida
print(f"Hola, bienvenido. Por favor elija una regla del 0-255.") ### 0 al 255 -> 1 al 256
regla = int(input("Regla: "))

### Regla en binario
def binRegla(numRegla):
    numRegla = int(numRegla)
    stringBinario = bin(numRegla)[2:].zfill(8)
    patrones = [(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)]
    reglaDic = {}
    for i, patron in enumerate(patrones):
        reglaDic[patron] = int(stringBinario[i])
    return reglaDic, stringBinario

reglaDic, stringBinario = binRegla(regla)

### Fila inicial
largoInicial = int(input("¿Qué tan larga va a ser la primera fila?: "))
fila1 = [0 for _ in range(largoInicial)]

# Genera algunos 1 al azar
for i in range(random.randrange(largoInicial)):
    fila1[random.randrange(largoInicial)] = 1

print(f"Así se ve tu primera generación: \n{fila1}")

### Número de generaciones
numGeneraciones = int(input("¿Cuántas generaciones van a ser?: "))

### Función para calcular la siguiente fila
def siguienteFila(fila_actual, reglaDic):
    nueva_fila = []
    n = len(fila_actual)
    
    for i in range(n):
        izquierda = fila_actual[i-1] if i > 0 else 0
        centro = fila_actual[i]
        derecha = fila_actual[i+1] if i < n-1 else 0
        patron = (izquierda, centro, derecha)
        nuevo_valor = reglaDic[patron]
        nueva_fila.append(nuevo_valor)
    return nueva_fila

### Función para mostrar filas
def visualizarFila(fila):
    return ''.join('1' if celda == 1 else '0' for celda in fila)

### SIMULACIÓN
print("\nEvolución:")
fila_actual = fila1
fila_anterior = None

# Aquí almacenaremos los pares (fila_anterior, fila_actual) vistos
historial = {}

for gen in range(numGeneraciones):
    print(f"Gen {gen}: {visualizarFila(fila_actual)}")

    # Crear la tupla de comparación, incluyendo la fila anterior
    clave = (tuple(fila_anterior) if fila_anterior else None, tuple(fila_actual))

    # Verificar si el patrón ya ocurrió
    if clave in historial:
        print(f"\n Patrón repetido detectado en la generación {gen}.")
        print(f"El patrón ya había aparecido en la generación {historial[clave]}.")
        break
    else:
        historial[clave] = gen

    # Avanzar a la siguiente generación
    fila_anterior = fila_actual
    fila_actual = siguienteFila(fila_actual, reglaDic)

else:
    print("\n No se detectaron repeticiones en las generaciones indicadas.")
