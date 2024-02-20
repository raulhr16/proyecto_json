import json
ruta_archivo="nba.json"
with open(ruta_archivo,'r') as archivo:
    datos_json = json.load(archivo)

def listajson(ruta_archivo):
    try:
        fecha=int(input("Introduce el año que quieras listar: "))
    except ValueError:
        print("Has introducido un valor no valido.")
    else:
        jugadores=datos_json.get("players",[])
        validacion=0
        repetidos=[]
        for datos in jugadores:
            if "name" in datos:
                nombre=datos["name"]
                if "stats" in datos:
                    for estadisticas in datos["stats"]:
                        ano = estadisticas["season"]
                        if fecha==ano:
                            if "jerseyNumber" in estadisticas:
                                if nombre not in repetidos:
                                    repetidos.append(nombre)
                                    dorsal = estadisticas["jerseyNumber"]
                                    print(f"En el año {ano}, el jugador {nombre} tiene el dorsal {dorsal}")
                                    validacion=1
        if validacion==0:
            print("No hay datos para el año que has introducido")
                                
def contarjson(ruta_archivo):
    jugadores=datos_json.get("players",[])
    mvp="Most Valuable Player"
    contador_mvp=0
    nombre=[]
    for datos in jugadores:
        if "awards" in datos:
            premios=datos["awards"]
            for cosas in premios:
                if "type" in cosas:
                    trofeos=cosas["type"]
                    if mvp==trofeos:
                        if datos["name"] not in nombre:
                            nombre.append(datos["name"])
                            contador_mvp=contador_mvp+1
                            print("El jugador",datos["name"],"ha sido un MVP")
    print(f"En total, han habido {contador_mvp} mvp's")

def buscarinfo(ruta_archivo):
    try:
        num_victorias=int(input("Introduce el numero de victorias sobre el que quieras realizar la busqueda: "))
    except ValueError:
        print("Has introducido un valor no valido.")
    else:
        equipos=datos_json.get("teams",[])
        validacion=0
        for datos in equipos:
            equipo=datos["name"]
            temporadas=datos["seasons"]
            for anos in temporadas:
                ano_ganado=anos["season"]
                if "won" in anos:
                    if num_victorias==anos["won"]:
                        print(f"El equipo {equipo}, en el año {ano_ganado} logro las {num_victorias} victorias")
                        validacion=1
        if validacion==0:
            print("Para las victorias introducidas no hay datos ")

def inforelacionada(ruta_archivo):
    ciudad=input("Introduce el nombre de la ciudad que quieras buscar: ")
    while not ciudad.replace(" ","").isalpha():
        ciudad=input("Introduce bien el nombre de la ciudad que quieras buscar: ")
    validacion=0
    equipos=datos_json.get("teams",[])
    for datos in equipos:
        nombre=datos["name"]
        capacidad=datos["stadiumCapacity"]
        if ciudad==datos["region"]:
            print(f"Para la ciudad {ciudad} el nombre del equipo es {nombre} y la capacidad de su estadio es {capacidad}")
            validacion=1
    if validacion==0:
        print("Para la ciudad introducida no hay datos")

def ejlibre(ruta_archivo):
    try:
        fecha=int(input("Introduce un año de nacimiento "))
    except ValueError:
        print("Has introducido un valor no valido.")
    else:
        jugadores=datos_json.get("players",[])
        validacion=0
        for datos in jugadores:
            if "name" in datos:
                nombre=datos["name"]
            nacimiento=datos["born"]
            ano=nacimiento["year"]
            if fecha==ano:
                validacion=1
                print(f"El jugador {nombre} ha nacido en el año {ano}")
                if "relatives" in datos:
                    for familia in datos["relatives"]:
                        tipo=familia["type"]
                        nombre_familiar=familia["name"]
                        print(f"El jugador {nombre} tiene o ha tenido familiares jugando, ese familiar es su {tipo} y su nombre es {nombre_familiar}")
                else:
                    print(f"El jugador {nombre} no ha tenido familiares jugando ")
        if validacion==0:
            print("No hay ningun jugador que haya nacido en ese año")
