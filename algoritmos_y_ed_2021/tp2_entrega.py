from pila import Pila
pila_aux=Pila()

def invertir_pila(pila,pila_invertida):
    while(not pila.pila_vacia()):
        x = pila.desapilar()
        pila_invertida.apilar(x)

def mostrar_pila (pila):
    while(not pila.pila_vacia()):
        x= pila.desapilar()
        print (x)
        pila_aux.apilar(x)
    invertir_pila (pila_aux,pila)


"""# 14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. 
# Solo puede utilizar una pila auxiliar como estructura extra –no se pueden utilizar métodos de ordenamiento–.
pila_elem =Pila()

opc="si"
while (opc=="si"):
    numero = int(input('ingrese un numero: '))
    if (pila_elem.pila_vacia())or (numero >= pila_elem.elemento_cima()):
        pila_elem.apilar(numero)
    else:
        while((not pila_elem.pila_vacia()) and(numero <= pila_elem.elemento_cima())):
            x=pila_elem.desapilar()
            pila_aux.apilar(x)
        pila_elem.apilar(numero)
        while (not pila_aux.pila_vacia()):
            x=pila_aux.desapilar()
            pila_elem.apilar(x)
    opc=input ("desea ingresar otro elemento: ")
    opc.lower() 

    
print ("los elementos ordenados:")
mostrar_pila(pila_elem)


# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

pila_aux5=Pila()
pila_aux7=Pila()
pila_resultado=Pila()

pila_starw5 = Pila()
pila_starw5.apilar("Luke Skywalker")
pila_starw5.apilar("Leia Organa")
pila_starw5.apilar("Han Solo")
pila_starw5.apilar("Lando Calrissian")
pila_starw5.apilar("Obi Wan Kenobi")
pila_starw5.apilar("Chewbacca")
pila_starw5.apilar("Yoda")
pila_starw5.apilar("Darth Vader")
pila_starw5.apilar("Boba Fett")
pila_starw5.apilar("Palpatine")

pila_starw7 = Pila()
pila_starw7.apilar("Luke Skywalker")
pila_starw7.apilar("Han Solo")
pila_starw7.apilar("Kylo Ren")
pila_starw7.apilar("Rey")
pila_starw7.apilar("Leia Organa")
pila_starw7.apilar("Poe Dameron")
pila_starw7.apilar("BB-8")
pila_starw7.apilar("Finn")
pila_starw7.apilar("Lider Supremo Snoke")
pila_starw7.apilar("Lor San Tekka")
def comparar_stw5_y_stw7(pila_starw5, pila_starw7, pila_aux5, pila_aux7, pila_resultado):
    while (not pila_starw5.pila_vacia()):
        x = pila_starw5.desapilar()
        pila_aux5.apilar(x)
        encontrado=False
        while (not pila_starw7.pila_vacia())and (encontrado==False):
            y = pila_starw7.desapilar()
            if (x==y):
                pila_resultado.apilar(x)
                encontrado=True
            pila_aux7.apilar(y)
        while (not pila_aux7.pila_vacia()):
            y = pila_aux7.desapilar ()
            pila_starw7.apilar(y)

comparar_stw5_y_stw7(pila_starw5, pila_starw7, pila_aux5, pila_aux7, pila_resultado)
print ("los personajes que se repiten son:")
mostrar_pila(pila_resultado)

# 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The Mandalorian), las cuales 
# se almacenaban en una pila (en su correspondiente nave) en cada misión de caza que emprendió, con la siguiente información: 
# planeta visitado, a quien capturó, costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo a Han Solo, 
# suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

money_boba=0
money_din=0
pila_aux2=Pila()

pila_boba=Pila()
pila_boba.apilar({"planeta_visitado":"planeta1","nombre_del_prisionero":"personaje1","costo_de_la_recompensa":123})
pila_boba.apilar({"planeta_visitado":"planeta2","nombre_del_prisionero":"Han Solo","costo_de_la_recompensa":354})
pila_boba.apilar({"planeta_visitado":"planeta3","nombre_del_prisionero":"personaje3","costo_de_la_recompensa":534})
pila_boba.apilar({"planeta_visitado":"planeta4","nombre_del_prisionero":"personaje4","costo_de_la_recompensa":432})

pila_din=Pila()
pila_din.apilar({"planeta_visitado":"planeta5","nombre_del_prisionero":"personaje5","costo_de_la_recompensa":79})
pila_din.apilar({"planeta_visitado":"planeta6","nombre_del_prisionero":"personaje6","costo_de_la_recompensa":123})
pila_din.apilar({"planeta_visitado":"planeta7","nombre_del_prisionero":"personaje7","costo_de_la_recompensa":265})
pila_din.apilar({"planeta_visitado":"planeta8","nombre_del_prisionero":"personaje8","costo_de_la_recompensa":435})
pila_din.apilar({"planeta_visitado":"planeta9","nombre_del_prisionero":"personaje9","costo_de_la_recompensa":321})

print ("los planetas visitados por Boba Fett: ")
while (not pila_boba.pila_vacia()):
    x= pila_boba.desapilar()
    print (x["planeta_visitado"])
    money_boba+= x["costo_de_la_recompensa"]
    pila_aux.apilar(x)

print ("los planetas visitados por Din Djarin: ")
while (not pila_din.pila_vacia()):
    x= pila_din.desapilar()
    print (x["planeta_visitado"])
    money_din+= x["costo_de_la_recompensa"]
    pila_aux2.apilar(x)

if (money_boba < money_din):
    print ("Din Djarin recolecto mayor fortuna con un total de: ",money_din)
    print ("Boba Fett recolecto menor fortuna con un total de: ",money_boba)
elif (money_boba > money_din):
    print ("Boba Fett recolecto mayor fortuna con un total de: ",money_boba)
    print ("Din Djarin recolecto menor fortuna con un total de: ",money_din)
elif(money_boba==money_din):
    print ("Boba Fett y Din Djarin recolectaron la misma cantidad de fortuna, con un total de: ",money_boba)
c=1
while (not pila_aux.pila_vacia()):
    x=pila_aux.desapilar()
    if(x["nombre_del_prisionero"]== "Han Solo"):
        cont=c
    c+=1
    pila_boba.apilar(x)

print ("Han Solo fue capturado en la mision numero ",cont," de Boba Fett")

print("Boba Fett cumplio ",pila_boba.tamanio()," misiones")
print("Din Djarin cumplio ",pila_aux2.tamanio()," misiones")

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pila_personajes=Pila()

pila_personajes.apilar ({"nombre": "Rocket Raccoon","cantidad":4})
pila_personajes.apilar({"nombre": "Groot","cantidad":4})
pila_personajes.apilar({"nombre":"Viuda Negra","cantidad":8})
pila_personajes.apilar({"nombre":"Spiderman","cantidad":6})
pila_personajes.apilar({"nombre":"Iron man","cantidad":11})
pila_personajes.apilar({"nombre":"Hulk","cantidad":12})
pila_personajes.apilar({"nombre":"Deadpool","cantidad":3})
pila_personajes.apilar({"nombre":"Wolverine","cantidad":4})

pila_aux=Pila()
pila_masde5=Pila()
cont=1
while (not pila_personajes.pila_vacia()):
    x=pila_personajes.desapilar()
    pila_aux.apilar(x)
    if (x["nombre"] =="Rocket Raccoon"):
        pos_raccoon=cont
    if (x["nombre"] == "Groot"):
        pos_groot=cont
    if (x["cantidad"] >= 5):
        pila_masde5.apilar(x)
    if (x["nombre"]== "Viuda Negra"):
        cant_bw = x["cantidad"]
    cont+=1

while (not pila_aux.pila_vacia()):
            y = pila_aux.desapilar()
            pila_personajes.apilar(y)

print ("el personaje Rocket Raccoon fue encontrado despues de ",pos_raccoon," personajes" )
print ("el personaje groot fue encontrado despues de ",pos_groot," personajes" )

print ()
print ("los personajes que participaron en mas de 5 peliculas: ")
while (not pila_masde5.pila_vacia()):
    x=pila_masde5.desapilar()
    print ("el personaje ",x["nombre"]," participo de ",x["cantidad"]," peliculas")
print ("la viuda negra (black widow) participo de ",cant_bw,"peliculas")

print ("los personajes cuyos nombres comienzan con c, d y g son: ")
while (not pila_personajes.pila_vacia()):
    x=pila_personajes.desapilar()
    if (x["nombre"][0]=="C")or(x["nombre"][0]=="D")or(x["nombre"][0]=="G"):
        print (x["nombre"])"""