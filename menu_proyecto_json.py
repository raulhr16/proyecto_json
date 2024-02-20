#Menu proyecto JSON
import json
ruta_archivo="nba.json"
with open(ruta_archivo,'r') as archivo:
    datos_json = json.load(archivo)
from programas_json import listajson, contarjson, buscarinfo, inforelacionada, ejlibre

eleccion=0
texto=''
def EscribirCentrado(texto):
    anchura=80
    longitud=len(texto)
    texto=("MENU\n1.Listar información\n2.Contar MVPs\n3.Filtrar información\n4.Búsqueda relacionada\n5.Ejercicio libre\n6.Salir")
    centrado=(' '*36 + texto)
    print("-"*anchura)
    print(centrado)
    print("-"*anchura)
    

while eleccion!=6:
    if eleccion==1:
        listajson(ruta_archivo)
    elif eleccion==2:
        contarjson(ruta_archivo)
    elif eleccion==3:
        buscarinfo(ruta_archivo)
    elif eleccion==4:
        inforelacionada(ruta_archivo)
    elif eleccion==5:
        ejlibre(ruta_archivo)
    elif eleccion==6:
        print("Muchas gracias por comprar!! ")
    EscribirCentrado(texto)
    eleccion=int(input("Introduce lo que quieras hacer "))
    while not (eleccion==1 or eleccion==2 or eleccion==3 or eleccion==4 or eleccion==5 or eleccion==6):
        eleccion=int(input("No has introducido un numero valido, introduce lo que quieras hacer "))
print("Muchas gracias por tu tiempo!")