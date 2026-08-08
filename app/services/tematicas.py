TEMATICAS = [

    {
        "nombre": "Granja de Zenón",
        "keywords": [
            "granja de zenon",
            "granja de zenón",
            "zenon",
            "zenón"
        ],
        "disponible": True,
        "link": "LINK_GRANJA_ZENON"
    },

    {
        "nombre": "Abejita",
        "keywords": [
            "abejita",
            "abeja"
        ],
        "disponible": True,
        "link": "LINK_ABEJITA"
    },

    {
        "nombre": "Pokemon",
        "keywords": [
            "pokemon",
            "pokémon",
            "pikachu"
        ],
        "disponible": True,
        "link": "LINK_POKEMON"
    },

]

def buscar_tematica(nombre: str):

    nombre = nombre.lower().strip()

    for tematica in TEMATICAS:

        # Buscar coincidencia por nombre
        if nombre == tematica["nombre"].lower():
            return tematica

        # Buscar coincidencia por keywords
        for keyword in tematica["keywords"]:

            if keyword.lower() in nombre:
                return tematica

    return None

def buscar_tematicas(nombres: list[str]):

    resultados = []

    for nombre in nombres:

        tematica = buscar_tematica(nombre)

        if tematica:
            resultados.append(tematica)

    return resultados