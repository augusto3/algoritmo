from pila import Pila
from cola import Cola
from lista import Lista

# 1. Dado un vector con personaje de las películas de la saga de Star Wars resolver las
# siguientes actividades:
# a. Realizar un barrido recursivo del vector. 
# b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el vector y en que posición. 

vector =["Luke Skywalker","Chewbacca","Obi Wan Kenobi","Yoda","Han Solo","Darth Vader","Boba Fett","Leia Organa"]

def barrido_rec(vector,pos):
    if (pos == 0):
        return print ("personaje: ",vector[pos])
    else:
        print ("personaje: ",vector[pos])
        return barrido_rec(vector,pos-1)

def busqueda(vector,buscado,pos):
    if (vector[pos]== buscado):
        return True
    elif(pos==0):
        return False
    else:
        return busqueda(vector,buscado,pos-1)

buscado="Yoda"
pos= len(vector)-1
barrido_rec(vector,pos)
pos= len(vector)-1
if (busqueda(vector,buscado,pos)):
    print ("yoda ha sido encontrado")
else:
    print ("yoda no ha sido encontrado")



# 2. Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone, de las cual 
# se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
# c. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# d. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
# e. utilizar una pila para almacenar temporalmente las notificaciones de Instagram y mostrar el contenido de dicha pila. 
pila_notificacion=Pila()
cola_notificacion=Cola()
cola_notificacion.add({"app":"Facebook","mensaje":"has recibido una nueva solicitud de amistad","hora":"16:30"})
cola_notificacion.add({"app":"Facebook","mensaje":"rocio agrego un artivo en venta en 'mercado libre'","hora":"11:50"})
cola_notificacion.add({"app":"Facebook","mensaje":"tienes una nueva sugerencia de amistad","hora":"14:20"})
cola_notificacion.add({"app":"Twitter","mensaje":"nuevo curso python para principiantes","hora":"20:15"})
cola_notificacion.add({"app":"Twitter","mensaje":"aprende java gratis con estos cursos","hora":"23:20"})
cola_notificacion.add({"app":"Twitter","mensaje":"python el mejor lenguaje de programacion","hora":"13:00"})
cola_notificacion.add({"app":"Instagram","mensaje":"jonas ha iniciado una llamada en directo","hora":"12:23"})
cola_notificacion.add({"app":"Instagram","mensaje":"karen ha comenzado a seguirte","hora":"18:20"})


def mostrar_pila (pila):
    while(not pila.pila_vacia()):
        notificacion = pila.desapilar()
        print ("notificacion: ",notificacion["app"],"--",notificacion["mensaje"],"--",notificacion["hora"])

def eliminar_elementos(cola,campo,a_eliminar):
    i=0
    tamanio = cola.tamanio()-1
    while (tamanio>=i):
        elemento = cola.delete()
        if (elemento[campo]!=a_eliminar):
            cola.add(elemento)
        i+=1

def busqueda_caracteres(texto,buscado):
    for i in range(0,len(texto)):
        if (texto[i]==buscado[0]):
            c=1
            for j in range (1,len(buscado)):
                if (texto[i+j]==buscado[j]):
                    c+=1
                    if c==len(buscado)-1:
                        return True

def mostrar_twiter(cola,mensaje):
    i=0
    while (cola.tamanio()-1>=i):
        notificacion=cola.mover_final()
        if (notificacion["app"]=="Twitter"):
            if(busqueda_caracteres(notificacion["mensaje"],mensaje)):
                print ("notificacion: ",notificacion["app"],"--",notificacion["mensaje"],"--",notificacion["hora"])
        i+=1

def copia_elementos(cola,campo,a_copiar,copia):
    i=0
    tamanio = cola.tamanio()-1
    while (tamanio>=i):
        elemento = cola.delete()
        if (elemento[campo]==a_copiar):
            copia.apilar(elemento)
        cola.add(elemento)
        i+=1

mensaje="python"
eliminar_elementos(cola_notificacion,"app","Facebook")
mostrar_twiter(cola_notificacion,mensaje)
copia_elementos(cola_notificacion,"app","Instagram",pila_notificacion)
mostrar_pila(pila_notificacion)

# 3. Dada una lista con nombres de personajes de la saga de Avengers, resolver las siguientes tareas:
# a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la
# misma;
# b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
# c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
# ‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
# cargados. 
# d. Realizar un barrido ascendente y descendente de la lista. 
# e. Mostrar la información del personaje en la posición 7. 
# f. Mostrar todos los personajes que comienzan con C o S. 
# g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo booleano que indica si es 
# héroe True villano False), luego realizar un barrido ordenado por nombre y otro por año de aparición. 
# Deberá cargar toda la información de nuevo.
lista_personajes=Lista()
lista_aux=Lista()
lista=Lista()
lista_personajes.insertar("Iron Man")
lista_personajes.insertar("Capitan America")
lista_personajes.insertar("Thor")
lista_personajes.insertar("Scalet Witch")
lista_personajes.insertar("Ojo de Halcon")

lista_aux.insertar("Black Widow")
lista_aux.insertar("Rocket Racoonn")
lista_aux.insertar("Hulk")
lista_aux.insertar("Loki")


def busqueda_thor(buscado,lista):
    for i in range (0,lista.tamanio()):
        personaje = lista.obtener_elemento(i)
        if (personaje==buscado):
            print (personaje,"esta en la posicion ",i)

def modificar(buscado,lista):
    for i in range (0,lista.tamanio()):
        personaje = lista.obtener_elemento(i)
        if (personaje==buscado):
            lista.modificar_elemento(i,"Scarlet Witch")

def combinar_listas(lista,lista_aux):
    i=0
    for i in range (0,lista_aux.tamanio()):
        personaje=lista_aux.obtener_elemento(i)
        cargar=True
        for i in range (0,lista.tamanio()):
            if (personaje == lista.obtener_elemento(i)):
                cargar=False
        if (cargar==True):
            lista.insertar(personaje)
        i+=1

def barrido_c_o_s(lista):
    for i in range (0,lista.tamanio()):
        personaje = lista.obtener_elemento(i)
        if ((personaje[0]=="S") or (personaje[0]=="C")):
            print (personaje)


# busqueda_thor("Thor",lista_personajes)
# modificar("Scalet Witch",lista_personajes)
# combinar_listas(lista_personajes,lista_aux)
# lista_personajes.barrido()

# print ("el elemento que esta en la 7ma pocision es: ",lista_personajes.obtener_elemento(6))
# lista_personajes.barrido()
# print()
# lista_personajes.barrido_desc()
# print ()
# barrido_c_o_s(lista_personajes)
