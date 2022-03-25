# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.
from pila import Pila
from random import *
pila_num = Pila()
pila_aux = Pila()

def rellenar_pila(pila_aux,pila):
    while (not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

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

def numero_random (pila_num):
    for n in range(0, 5):
        num = randint(1, 10)
        pila_num.apilar(num)

def contar (pila, numero):
    cantidad=0
    while(not pila_num.pila_vacia()):
        x = pila_num.desapilar()
        pila_aux.apilar(x)
        if(x == numero):
            cantidad += 1
    return cantidad

# numero_random(pila_num)
# numero = int(input('ingrese el numero que desea contar '))
# print ("la cantidad de elementos ",numero," en la pila es de ",contar(pila_num, numero))

# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.
def par_e_impar (pila, pila_impar, pila_par):
    while(not pila.pila_vacia()):
        x = pila.desapilar()
        if (x % 2 ==0):
            pila_par.apilar(x)
        elif(x % 2 != 0):
            pila_impar.apilar(x)
        pila_aux.apilar(x)

# pila_par = Pila()
# pila_impar = Pila()
# par_e_impar (pila_num, pila_impar,pila_par)
# mostrar_pila (pila_par)

# 3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.
def reemplazar(pila, numero, reemplazo):
    pila_aux =Pila()
    while(not pila.pila_vacia()):
        x = pila.desapilar()
        if (x != numero):
            pila_aux.apilar(x)
        elif (x == numero):
            pila_aux.apilar(reemplazo)
    return pila_aux

# mostrar_pila(pila_num)
# numero = int(input('ingrese el numero que deseas reemplazar '))
# reemplazo = int(input('ingrese el numero a reemplazar '))
# mostrar_pila(reemplazar(pila_num, numero, reemplazo))

# 4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

# mostrar_pila(pila_num,pila_aux)
# print ()
# invertir_pila(pila_aux, pila_num)
# mostrar_pila(pila_aux,pila_num)

# 5. Determinar si una cadena de caracteres es un palíndromo.
# pila_letra = Pila()
# pila_invertida =Pila()

def cadena_a_pilas (pila,palabra):
    for i in range(0,len(palabra)):
        pila.apilar(palabra[i])
    return pila

def comparar_pila(pila1, pila2):
    cont=0
    while(not pila1.pila_vacia()):
        if (pila1.desapilar()!=pila2.desapilar()):
            return False
    return True

# palabra = input('ingrese una palabra para saber si es un palindromo ')
# cadena_a_pilas(pila_aux,palabra)
# invertir_pila(pila_aux,pila_invertida)
# cadena_a_pilas(pila_letra,palabra)
# if (comparar_pila(pila_invertida, pila_letra)==True):
#     print ("la palabra es un palindromo ")
# else:
#     print ("la palabra no es un palindromo")

# 6. Leer una palabra y visualizarla en forma inversa.
# cadena = input('ingrese una palabra para invertir: ')
# cadena_a_pilas (pila_letra,cadena)

def invertir_palabra(pila):
    palabra=""
    while (not pila.pila_vacia()):
        x = pila.desapilar()
        palabra = palabra + x
    return palabra
# print (invertir_palabra(pila_letra))

# 7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.
# pila_palabras=Pila()
# pila_palabras.apilar("vacuna")
# pila_palabras.apilar("covid.19")
# pila_palabras.apilar("cuarentena")
# pila_palabras.apilar("encierro")
# pila_palabras.apilar("aislado")
# pila_palabras.apilar("palabra")
# pila_palabras.apilar("cima")

# mostrar_pila(pila_palabras)
# cadena = input('ingrese una palabra para buscarla: ')

def busqueda_pila (objeto,pila):
    cont=0
    bool=False
    while (not pila.pila_vacia()):
        x=pila.desapilar()
        pila_aux.apilar(x)
        if (x==objeto):
            pos=cont
        cont+=1
    invertir_pila(pila_aux,pila)
    return pos

def eliminar_elemento(pila,pos):
    cont=0
    while (not pila.pila_vacia()):
        if (cont == pos):
            pila.desapilar()
        if (not pila.pila_vacia()):
            pila_aux.apilar(pila.desapilar())
        cont+= 1
    invertir_pila(pila_aux,pila)

# pos=busqueda_pila(cadena,pila_palabras)
# print (pos)
# eliminar_elemento(pila_palabras,pos)
# mostrar_pila(pila_palabras)

# 8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
# cartas de baraja española–,resolver las siguientes actividades:
# a. generar las cartas del mazo de forma aleatoria;
# b. separar la pila mazo en cuatro pilas una por cada palo;
# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
mazo=Pila()
mazo_aux=Pila()
pila_oro=Pila()
pila_espada=Pila()
pila_copa=Pila()
pila_basto=Pila()

def carga_aleatoria_de_mazo(mazo):
    while (not mazo.tamanio()==40):
        cargar=True
        numero= choice([1,2,3,4,5,6,7,10,11,12])
        palo= choice(["oro","basto","espada","copa"])
        naipe= ({"numero":numero,"palo":palo})
        while (not mazo.pila_vacia()and cargar==True):
            naipe2=mazo.desapilar()
            mazo_aux.apilar(naipe2)
            if ((naipe["numero"] == naipe2["numero"])and(naipe["palo"] == naipe2["palo"])):
                cargar=False
        if (cargar==True):
            mazo.apilar(naipe)
        rellenar_pila(mazo_aux,mazo)

# def cargar_mazo(mazo):
#     for i in range (1,8):
#         mazo.apilar({"numero":i,"palo":"oro"})
#         mazo.apilar({"numero":i,"palo":"espada"})
#         mazo.apilar({"numero":i,"palo":"basto"})
#         mazo.apilar({"numero":i,"palo":"copa"})
#     for i in range (10,13):
#         mazo.apilar({"numero":i,"palo":"oro"})
#         mazo.apilar({"numero":i,"palo":"espada"})
#         mazo.apilar({"numero":i,"palo":"basto"})
#         mazo.apilar({"numero":i,"palo":"copa"})

def por_palo(mazo, pila_oro, pila_espada, pila_copa, pila_basto):
    while (not mazo.pila_vacia()):
        naipe = mazo.desapilar()
        if (naipe["palo"] == "oro"):
            pila_oro.apilar(naipe)
        elif (naipe["palo"] == "copa"):
            pila_copa.apilar(naipe)
        elif (naipe["palo"] == "espada"):
            pila_espada.apilar(naipe)
        elif (naipe["palo"] == "basto"):
            pila_basto.apilar(naipe)

def ordenamiento (pila,campo):
    for i in range (1,pila.tamanio()):
        while (not pila.pila_vacia()):
            elemento=pila.desapilar()
            if (pila.pila_vacia()):
                pila_aux.apilar(elemento) 
            elif (not pila.pila_vacia()):
                elemento2=pila.desapilar()
                if ((elemento[campo] >= elemento2[campo])):
                    pila_aux.apilar(elemento)
                    pila.apilar(elemento2)
                else:
                    pila_aux.apilar(elemento2)
                    pila.apilar(elemento)
        invertir_pila(pila_aux,pila)

def mostrar_carta (mazo):
    while (not mazo.pila_vacia()):
        naipe = mazo.desapilar()
        print("[", naipe["numero"] ,"-",naipe["palo"],"]") 
        mazo_aux.apilar(naipe)

# carga_aleatoria_de_mazo(mazo)
# por_palo(mazo,pila_oro,pila_espada,pila_copa,pila_basto)
# print(pila_oro.tamanio())
# ordenamiento(pila_oro,"numero")
# print(pila_oro.tamanio())
# mostrar_carta(pila_oro)

# 9. Resolver el problema del factorial de un número utilizando una pila.

# numero= int(input ("ingrese un numero: "))
# pila_factorial=Pila()

# factorial=1
# for i in range (1,numero+1):
#     pila_factorial.apilar(i)
# for i in range (0,numero):
#     factorial = factorial * pila_factorial.desapilar()

# print (factorial)

# 10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
# pila con nombres de dioses griegos.
# pila_dioses=Pila()
# pila_dioses.apilar("zeus")
# pila_dioses.apilar("ares")
# pila_dioses.apilar("poseidon")
# pila_dioses.apilar("hades")
# pila_dioses.apilar("hermes")
# pila_dioses.apilar("dionisio")
# pila_dioses.apilar("apolo")

# mostrar_pila(pila_dioses)
# nombre="atenea"
# pos=3

def insertar_en_posicion(objeto,pos,pila):
    i=0
    while (not pila.pila_vacia()):
        i+=1
        if (i==pos):
            pila_aux.apilar(objeto)
        else:
            pila_aux.apilar(pila.desapilar())
    invertir_pila(pila_aux,pila)


# print()
# insertar_en_posicion(nombre,pos,pila_dioses)
# mostrar_pila(pila_dioses)


# 11. Dada una pila de letras determinar cuántas vocales contiene.
# pila_letras=Pila()
# pila_letras.apilar("a")
# pila_letras.apilar("b")
# pila_letras.apilar("e")
# pila_letras.apilar("c")
# pila_letras.apilar("g")
# pila_letras.apilar("i")
# pila_letras.apilar("k")
# pila_letras.apilar("h")
# pila_letras.apilar("l")
# pila_letras.apilar("o")
# pila_letras.apilar("q")
# pila_letras.apilar("u")

def cont_vocales (pila):
    cont=0
    while (not pila.pila_vacia()):
        letra = pila.desapilar()
        pila_aux.apilar(letra)
        if (letra=="a"):
            cont+=1
        if (letra=="e"):
            cont+=1
        if (letra=="i"):
            cont+=1
        if (letra=="o"):
            cont+=1
        if (letra=="u"):
            cont+=1
    invertir_pila(pila_aux,pila)
    return cont

# print("la cantidad de vicales es de: ",cont_vocales(pila_letras))
# mostrar_pila(pila_letras)

# 12. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

# pila_personajesstw=Pila()
# pila_personajesstw.apilar("Anakin Skywalker")
# pila_personajesstw.apilar("Luke Skywalker")
# pila_personajesstw.apilar("Leia Organa")
# pila_personajesstw.apilar("Obi Wan Kenobi")
# pila_personajesstw.apilar("Han Solo")
# pila_personajesstw.apilar("Boba Fett")
# pila_personajesstw.apilar("Darth Vader")
# pila_personajesstw.apilar("Palpatine")
# pila_personajesstw.apilar("yoda")

def busqueda_pila(busqueda,pila):
    encontrado=False
    while (not pila.pila_vacia()):
        buscado=pila.desapilar()
        if (buscado==busqueda):
            encontrado=True
        pila_aux.apilar(buscado)
    invertir_pila(pila_aux,pila)
    return encontrado


# buscar = "Leia Organa"
# if (busqueda_pila(buscar,pila_personajesstw)==True):
#     print("Leia Organa fue encontrada en la pila ")
# else:
#     print("Leia Organa no fue encontrada en la pila ")

# buscar = "Boba Fett"
# if (busqueda_pila(buscar,pila_personajesstw)==True):
#     print("Boba Fett fue encontrada en la pila ")
# else:
#     print("Boba Fett no fue encontrada en la pila ")

# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU) de los cuales se conoce el nombre
# del modelo, nombre de la película en la que se usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
# las siguientes actividades:
# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
# además mostrar el nombre de dichas películas;
# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado;
# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
# repetidos en una misma película;
# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.
# 14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. 
# Solo puede utilizar una pila auxiliar como estructura extra –no se pueden utilizar métodos de ordenamiento–.
# 15. Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente.
# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.
# 17. Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonantes y otros caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego
# utilizando las operaciones de pila resolver las siguientes consignas:
# a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
# b. cantidad de espacios en blanco;
# c. porcentaje que representan las vocales respecto de las consonantes sobre el total de caracteres del párrafo;
# d. cantidad de números;
# e. determinar si la cantidad de vocales y otros caracteres son iguales;
# f. determinar si existe al menos una z en la pila de consonantes.
# 18. Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejemplo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del
# objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras extras, no se pueden utilizar métodos de ordenamiento.
# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.
# 21. Realizar un algoritmo que ingrese en una pila los dos valores iniciales de la sucesión de Fibonacci –o condiciones de fin de forma recursiva– y a partir de estos calcular los siguientes
# valores de dicha sucesión, hasta obtener el valor correspondiente a un número n ingresado por
# el usuario.
# 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
# Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
# costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
# de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
# quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
# que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.
# 23. Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
# obtener la siguiente información sin perder los datos:
# a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
# b. calcular el promedio de temperatura (o media) del total de valores;
# c. determinar la cantidad de valores por encima y por debajo de la media.
# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.####