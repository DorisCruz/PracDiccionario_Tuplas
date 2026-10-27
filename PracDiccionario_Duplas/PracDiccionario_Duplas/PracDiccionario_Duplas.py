
# Practica de diccionarios y tuplas
# Identificacion de animales

# Caracteristicas de los animales
ANIMALES = {
    "guepardo": [
        ("pelo", True),
        ("carne", True),
        ("leonado", True),
        ("manchas", True)
    ],
    "tigre": [
        ("pelo", True),
        ("carne", True),
        ("leonado", True),
        ("rayas", True)
    ],
    "jirafa": [
        ("pelo", True),
        ("pezuñas", True),
        ("cuello_largo", True),
        ("manchas", True)
    ],
    "cebra": [
        ("pelo", True),
        ("pezuñas", True),
        ("rayas", True)
    ],
    "pinguino": [
        ("plumas", True),
        ("nada", True),
        ("blanco_negro", True),
        ("huevos", True)
    ],
    "albatros": [
        ("plumas", True),
        ("vuela", True),
        ("huevos", True),
        ("vuela_bien", True)
    ],
    "elefante": [
        ("pelo", True),
        ("leche", True),
        ("trompa", True),
        ("orejas_grandes", True),
        ("altura", True)
    ]
}

# Reglas de clasificacion
REGLAS = {
    1: ([("pelo", True)], ("clase", "mamifero")),
    2: ([("leche", True)], ("clase", "mamifero")),
    3: ([("vuela", True), ("huevos", True)], ("clase", "ave")),
    4: ([("plumas", True)], ("clase", "ave")),
    5: ([("clase", "mamifero"), ("carne", True)],
        ("clase", "carnivoro")),
    6: ([("clase", "mamifero"), ("pezuñas", True)],
        ("clase", "ungulado")),
    7: ([("clase", "carnivoro"), ("leonado", True),
         ("manchas", True)], ("especie", "guepardo")),
    8: ([("clase", "carnivoro"), ("leonado", True),
         ("rayas", True)], ("especie", "tigre")),
    9: ([("clase", "ungulado"), ("cuello_largo", True),
         ("manchas", True)], ("especie", "jirafa")),
    10: ([("clase", "ungulado"), ("rayas", True)],
         ("especie", "cebra")),
    11: ([("clase", "ave"), ("nada", True),
          ("blanco_negro", True)], ("especie", "pinguino")),
    12: ([("clase", "ave"), ("vuela_bien", True)],
         ("especie", "albatros")),
    13: ([("clase", "mamifero"), ("trompa", True)],
         ("especie", "elefante")),
    14: ([("trompa", True), ("orejas_grandes", True),
          ("altura", True)], ("especie", "elefante"))
}


# Funcion para aplicar las reglas
def identificar(hechos):
    cambio = True

    while cambio:
        cambio = False

        for condiciones, conclusion in REGLAS.values():
            cumple = True

            for condicion in condiciones:
                if condicion not in hechos:
                    cumple = False
                    break

            if cumple and conclusion not in hechos:
                hechos.append(conclusion)
                cambio = True

    return hechos


# Mostrar las clasificaciones
print("IDENTIFICACION DE ANIMALES")

for animal, caracteristicas in ANIMALES.items():
    hechos = identificar(caracteristicas.copy())

    clases = [
        valor for tipo, valor in hechos
        if tipo == "clase"
    ]

    especies = [
        valor for tipo, valor in hechos
        if tipo == "especie"
    ]

    print(f"\nAnimal: {animal}")
    print("Clasificaciones:", clases)
    print("Identificacion:", especies)
