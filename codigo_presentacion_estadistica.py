import random

print(f"Hola, bienvenido. Por favor elija una regla del 0-255.")
regla = int(input("Regla: "))

# Regla en binario
def binRegla(numRegla):
    numRegla = int(numRegla)
    stringBinario = bin(numRegla)[2:].zfill(8)
    patrones = [(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)]
    reglaDic = {}
    for i, patron in enumerate(patrones):
        reglaDic[patron] = int(stringBinario[i])
    return reglaDic, stringBinario

reglaDic, stringBinario = binRegla(regla)

# Fila inicial
largoInicial = int(input("¿Qué tan larga va a ser la primera fila?: "))
fila1 = [0 for _ in range(largoInicial)]

for i in range(random.randrange(largoInicial)):
    fila1[random.randrange(largoInicial)] = 1

print(f"Así se ve tu primera generación: \n{fila1}")

# Número de generaciones
numGeneraciones = int(input("¿Cuántas generaciones van a ser?: "))

# Función siguiente fila
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

# Función para visualizar (MEJORADA)
def visualizarFila(fila):
    return ''.join('■' if celda == 1 else '·' for celda in fila)


# calculo y impresion de datos 
def estadisticas(datos):
    total_1 = sum(f.count(1) for f in datos)
    total_0 = sum(f.count(0) for f in datos)
    total = total_1 + total_0
    
    max_1 = max(datos, key=lambda x: x.count(1))
    gen_max_1 = datos.index(max_1)

    print("\n============= ESTADÍSTICAS =============")
    print(f"Total de generaciones analizadas: {len(datos)}")
    print(f"Total de 1s: {total_1}")
    print(f"Total de 0s: {total_0}")
    print(f"Porcentaje de 1s: {100 * total_1 / total:.2f}%")
    print(f"Porcentaje de 0s: {100 * total_0 / total:.2f}%")
    print(f"Generación con más 1s: Gen {gen_max_1} ({max_1.count(1)} unos)")
    print(f"Promedio de 1s por generación: {total_1/len(datos):.2f}")
    print("=========================================\n")

# Simulacion
print("\nEvolución:")
fila_actual = fila1
fila_anterior = None
historial = {}

todas_las_filas = [fila1]

for gen in range(numGeneraciones):
    print(f"Gen {gen}: {visualizarFila(fila_actual)}")

    clave = (tuple(fila_anterior) if fila_anterior else None, tuple(fila_actual))

    if clave in historial:
        print(f"\n Patrón repetido detectado en la generación {gen}.")
        print(f"El patrón ya había aparecido en la generación {historial[clave]}.")
        break
    else:
        historial[clave] = gen

    fila_anterior = fila_actual
    fila_actual = siguienteFila(fila_actual, reglaDic)

    todas_las_filas.append(fila_actual)

else:
    print("\n No se detectaron repeticiones en las generaciones indicadas.")

estadisticas(todas_las_filas)
