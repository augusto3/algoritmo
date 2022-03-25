from cola import Cola
"""# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta 
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

cola_starw=Cola()
cola_starw.add({"nombre":"Luke Skywoker","planeta":"Tatooine"})
cola_starw.add({"nombre":"Han Solo","planeta":"Endor"})
cola_starw.add({"nombre":"maestro Yoda","planeta":"Alderaan"})
cola_starw.add({"nombre":"Anakin Skywoker","planeta":"Tatooine"})
cola_starw.add({"nombre":"Obi Wan Kenobi","planeta":"Endor"})
cola_starw.add({"nombre":"Jar Jar Binks","planeta":"Alderaan"})
cola_starw.add({"nombre":"Leia Organa","planeta":"planeta desconocido"})
cola_starw.add({"nombre":"Chewbacca","planeta":"planeta desconocido"})
i=0
print ()
while (cola_starw.tamanio() > i):
    x=cola_starw.mover_final()
    if (x["planeta"]=="Alderaan"):  
        print ("el personaje: ",x["nombre"]," nacio en Alderaan")
    if (x["planeta"]=="Endor"):
        print ("el personaje: ",x["nombre"]," nacio en Endor")
    if (x["planeta"]=="Tatooine"):
        print ("el personaje: ",x["nombre"]," nacio en Tatooine")
    i+=1

i=0
print ()
while (cola_starw.tamanio() > i):
    x=cola_starw.mover_final()
    if (x["nombre"]=="Luke Skywoker"):
        print ("el planeta natal de ", x["nombre"]," es ",x["planeta"])        
    if (x["nombre"]=="Han Solo"):
        print ("el planeta natal de ", x["nombre"]," es ",x["planeta"]) 
    i+=1

i=0
print ()
while (cola_starw.tamanio()>i):
    x=cola_starw.mover_final()
    if (cola_starw.mostrar_indice()["nombre"]=="maestro Yoda"):
        nombre= input ("ingrese el nombre del personaje: ")
        planeta= input ("ingrese el nombre de su planeta natal: ")
        cola_starw.add({"nombre":nombre,"planeta":planeta})
    i+=1

print ()
encontrado= False
while (encontrado == False):
    if (cola_starw.mover_final()["nombre"]=="Jar Jar Binks"):
        encontrado=True
cola_starw.delete()


i=0
while (cola_starw.tamanio() > i):
    x=cola_starw.mover_final()
    print (x)
    i+=1

# 12. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una 
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, 
# ni métodos de ordenamiento.

cola1 =Cola()
cola2 =Cola()

cola1.add("a")
cola1.add("d")
cola1.add("e")
cola1.add("f")

cola2.add("b")
cola2.add("c")
cola2.add("f")
cola2.add("g")

i = 0
cargado=True
tamanio = cola2.tamanio() 
while (tamanio >i):
    if (cargado==True):
        x = cola2.delete()
    if (cola1.mostrar_indice() <= x):
        cola1.mover_final()
        cargado=False
    if ((cola1.mostrar_indice() >= x) or (cola2.cola_vacia())):
        cola1.add(x)
        i+=1
        cargado=True
    if (tamanio == i):
        while (cola1.mover_final()<=cola1.mostrar_indice()):
            None
i=0
while (cola1.tamanio() > i):
    i+=1
    x=cola1.mover_final()
    print (x)

# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre
# del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo 
# {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

cola_marvel =Cola()

cola_marvel.add({"personaje":"Tony Stark", "superheroe":"Iron Man", "genero":"M"})
cola_marvel.add({"personaje":"Steve Rogers", "superheroe":"Capitán America", "genero":"M"})
cola_marvel.add({"personaje":"Natasha Romanof f", "superheroe":"Black Widow", "genero":"F"})
cola_marvel.add({"personaje":"Bruce Banner","superheroe":"hulk","genero":"M"})
cola_marvel.add({"personaje":"Wade Winston Wilson","superheroe":"Deadpool","genero":"M"})
cola_marvel.add({"personaje":"Peter Parker","superheroe":"Spider Man","genero":"M"})
cola_marvel.add({"personaje":"James Logan","superheroe":"Wolverine","genero":"M"})
cola_marvel.add({"personaje":"Carol Danvers","superheroe":"Capitana Marvel","genero":"F"})
cola_marvel.add({"personaje":"Scott Lang","superheroe":"Ant-Man","genero":"M"})
cola_marvel.add({"personaje":"Jean Grey ","superheroe":"Phoenix","genero":"F"})

i=0
while (cola_marvel.tamanio()>i):
    marvel=cola_marvel.mover_final()
    if (marvel["superheroe"] =="Capitana Marvel"):
        print ("el nombre de la superheroina ",marvel["superheroe"]," es ",marvel["personaje"])
    i+=1

i=0
print()
print ("las superheroes de genero femenino son: ")
while (cola_marvel.tamanio()>i):
    marvel=cola_marvel.mover_final()
    if (marvel["genero"] =="F"):
        print (marvel["superheroe"])
    i+=1
print()
i=0
print ("los superheroes de genero masculino son: ")
while (cola_marvel.tamanio()>i):
    marvel=cola_marvel.mover_final()
    if (marvel["genero"] =="M"):
        print (marvel["superheroe"])
    i+=1
print()
i=0
while (cola_marvel.tamanio()>i):
    marvel=cola_marvel.mover_final()
    if (marvel["personaje"] =="Scott Lang"):
        print ("el nombre del personaje  ",marvel["personaje"]," es ",marvel["superheroe"])
    i+=1
print()
i=0
print ("los personajes que tienen su nombre de su personaje o superheroe con s es:  ")
while (cola_marvel.tamanio()>i):
    marvel=cola_marvel.mover_final()
    if (marvel["personaje"][0] =="S") or (marvel["superheroe"][0] =="S"):
        print (marvel["personaje"]," es el superheroe ",marvel["superheroe"],", su genero es ",marvel["genero"])
    i+=1

print()
i=0
while (cola_marvel.tamanio()>i):
    marvel=cola_marvel.mover_final()
    if (marvel["personaje"] =="Carol Danvers"):
        print ("se encontro el personaje ",marvel["personaje"]," que es el superheroe ",marvel["superheroe"])
    i+=1"""