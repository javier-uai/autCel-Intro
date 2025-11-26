import random

# ==========================
# Generar diccionario de una regla (0-255)
# ==========================
def binRegla(numRegla):
    stringBin = bin(numRegla)[2:].zfill(8)
    patrones = [(1,1,1),(1,1,0),(1,0,1),(1,0,0),
                (0,1,1),(0,1,0),(0,0,1),(0,0,0)]
    reglaDic = {patrones[i]: int(stringBin[i]) for i in range(8)}
    return reglaDic

# ==========================
# Siguiente generación
# ==========================
def siguienteFila(fila, reglaDic):
    n = len(fila)
    nueva = []
    for i in range(n):
        izquierda = fila[i-1] if i > 0 else 0
        centro = fila[i]
        derecha = fila[i+1] if i < n-1 else 0
        nueva.append(reglaDic[(izquierda, centro, derecha)])
    return nueva

# ==========================
# Ejecutar una regla completa
# ==========================
def ejecutarRegla(numRegla, largo=100, genIniciales=100, genExtraMax=5000):
    reglaDic = binRegla(numRegla)

    # Fila 1 aleatoria
    fila = [random.choice([0, 1]) for _ in range(largo)]
    historial = {}

    fila_anterior = None
    gen = 0
    generaciones_max = genIniciales

    while True:
        clave = (tuple(fila_anterior) if fila_anterior else None, tuple(fila))

        if clave in historial:
            return {
                "regla": numRegla,
                "repite": True,
                "desde": historial[clave],
                "hasta": gen
            }

        historial[clave] = gen

        fila_anterior = fila
        fila = siguienteFila(fila, reglaDic)
        gen += 1

        # Si llegamos al límite y no se repite, aumentamos
        if gen >= generaciones_max:
            if generaciones_max >= genExtraMax:
                return {
                    "regla": numRegla,
                    "repite": False,
                    "hasta": generaciones_max
                }
            generaciones_max += 200  # Aumenta dinámicamente

# ==========================
# Ejecutar TODAS las reglas
# ==========================
resultados = []

for regla in range(256):
    print(f"\n===== Ejecutando regla {regla} =====")
    info = ejecutarRegla(regla)
    resultados.append(info)

    if info["repite"]:
        print(f"✔ Regla {regla}: patrón repetido desde gen {info['desde']} hasta {info['hasta']}")
    else:
        print(f"✖ Regla {regla}: no repite patrón hasta {info['hasta']} generaciones")

# ==========================
# Resumen final
# ==========================
print("\n\n========== RESUMEN GENERAL ==========")
for r in resultados:
    if r["repite"]:
        print(f"Regla {r['regla']} → Repite entre gen {r['desde']} y {r['hasta']}")
    else:
        print(f"Regla {r['regla']} → No repite (límite alcanzado)")
