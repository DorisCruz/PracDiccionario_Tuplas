# -*- coding: utf-8 -*-


# Diccionario
animales = {
    "guepardo": {
        "tiene_pelo": True,
        "come_carne": True,
        "leonado": True,
        "manchas_oscuras": True
    },


    "tigre": {
        "tiene_pelo": True,
        "come_carne": True,
        "leonado": True,
        "rayas_negras": True
    },

    "jirafa": {
        "tiene_pelo": True,
        "tiene_pezuñas": True,
        "cuello_largo": True,
        "manchas_oscuras": True
    },

    "cebra": {
        "tiene_pelo": True,
        "tiene_pezuñas": True,
        "rayas_negras": True
    },

    "pinguino": {
        "tiene_plumas": True,
        "nada": True,
        "blanco_y_negro": True,
        "pone_huevos": True
    },

    "albatros": {
        "tiene_plumas": True,
        "vuela": True,
        "pone_huevos": True,
        "vuela_muy_bien": True
    },

    "elefante": {
        "tiene_pelo": True,
        "da_leche": True,
        "tiene_trompa": True,
        "orejas_grandes": True,
        "gran_altura": True
    }
}


# Base de hechos

hechos = set()

for animal, caracteristicas in animales.items():
    for propiedad, valor in caracteristicas.items():
        hechos.add((animal, propiedad, valor))


# Reglas

reglas = [
    # R1: Si tiene pelo es mamifero
    ("R1",
     (("tiene_pelo", True),),
     ("es_un", "mamifero")),

    # R2: Si da leche a sus crias es mamifero
    ("R2",
     (("da_leche", True),),
     ("es_un", "mamifero")),

    # R3: Si vuela y pone huevos es un ave
    ("R3",
     (("vuela", True), ("pone_huevos", True)),
     ("es_un", "ave")),

    # R4: Si tiene plumas es un ave
    ("R4",
     (("tiene_plumas", True),),
     ("es_un", "ave")),

    # R5: Si es mamifero y come carne es carnivoro
    ("R5",
     (("es_un", "mamifero"), ("come_carne", True)),
     ("es_un", "carnivoro")),

    # R6: Si es mamifero y tiene pezuñas es ungulado
    ("R6",
     (("es_un", "mamifero"), ("tiene_pezuñas", True)),
     ("es_un", "ungulado")),

    # R7: Carnivoro leonado con manchas oscuras es un guepardo
    ("R7",
     (("es_un", "carnivoro"),
      ("leonado", True),
      ("manchas_oscuras", True)),
     ("es_un", "guepardo")),

    # R8: Carnivoro leonado con rayas negras es un tigre
    ("R8",
     (("es_un", "carnivoro"),
      ("leonado", True),
      ("rayas_negras", True)),
     ("es_un", "tigre")),

    # R9: Ungulado con cuello largo y manchas es una jirafa.
    ("R9",
     (("es_un", "ungulado"),
      ("cuello_largo", True),
      ("manchas_oscuras", True)),
     ("es_un", "jirafa")),

    # R10: Ungulado con rayas negras es una cebra
    ("R10",
     (("es_un", "ungulado"), ("rayas_negras", True)),
     ("es_un", "cebra")),

    # R11: Ave que nada y es blanca y negra es un pinguino
    ("R11",
     (("es_un", "ave"),
      ("nada", True),
      ("blanco_y_negro", True)),
     ("es_un", "pinguino")),

    # R12: Ave que vuela muy bien es albatros
    ("R12",
     (("es_un", "ave"), ("vuela_muy_bien", True)),
     ("es_un", "albatros")),

    # R13: Mamifero con trompa es elefante
    ("R13",
     (("es_un", "mamifero"), ("tiene_trompa", True)),
     ("es_un", "elefante")),

    # R14: Trompa, orejas grandes y gran altura es un elefante
    ("R14",
     (("tiene_trompa", True),
      ("orejas_grandes", True),
      ("gran_altura", True)),
     ("es_un", "elefante"))
]

# Consulta de hechos
def consultar(s=None, r=None, o=None):
  
    return [
        hecho for hecho in hechos
        if (s is None or hecho[0] == s)
        and (r is None or hecho[1] == r)
        and (o is None or hecho[2] == o)
    ]


def aplicar_reglas():
    
    nuevas_deducciones = []
    hubo_cambios = True

    while hubo_cambios:
        hubo_cambios = False

        for animal in animales:

            for nombre, condiciones, conclusion in reglas:

                cumple = all(
                    (animal, propiedad, valor) in hechos
                    for propiedad, valor in condiciones
                )

                if cumple:
                    propiedad, valor = conclusion
                    nuevo_hecho = (animal, propiedad, valor)

                    if nuevo_hecho not in hechos:
                        hechos.add(nuevo_hecho)
                        nuevas_deducciones.append(
                            (nombre, nuevo_hecho)
                        )
                        hubo_cambios = True

    return nuevas_deducciones


# Resukltados

def mostrar_hechos():
    print("\n BASE DE HECHOS ")

    for hecho in sorted(hechos, key=str):
        print(hecho)


def mostrar_clasificaciones():
    print("\n CLASIFICACION DE LOS ANIMALES ")

    for animal in sorted(animales):
        clasificaciones = consultar(s=animal, r="es_un")

        nombres = [objeto for _, _, objeto in clasificaciones]
        print(f"{animal}: {', '.join(sorted(nombres))}")


def menu():

    while True:
        print("\n CONSULTA DE ANIMALES ")
        print("1. Todos los hechos")
        print("2. Clasificaciones")
        print("3. Consultar un animal")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_hechos()

        elif opcion == "2":
            mostrar_clasificaciones()

        elif opcion == "3":
            animal = input(
                "Escribe el nombre del animal: "
            ).strip().lower()

            if animal in animales:
                resultados = consultar(s=animal)

                print(f"\nHechos de {animal}:")
                for hecho in sorted(resultados, key=str):
                    print(hecho)
            else:
                print("Ese animal no esta")

        elif opcion == "4":
            print("Programa terminado.")
            break

        else:
            print("Opcion no valida. Intenta de nuevo.")



if __name__ == "__main__":
    deducciones = aplicar_reglas()

    print("BASE DE CONOCIMIENTO DE ANIMALES")
    print("Reglas aplicadas:", len(deducciones))

    mostrar_clasificaciones()
    menu()

