from cola import Cola
from pila import Pila
from random import*
# 1. Eliminar de una cola de caracteres todas las vocales que aparecen.
cola_caracteres = Cola()
pila_aux=Pila()
cola_aux=Cola()

# cola_caracteres.add("n")
# cola_caracteres.add("e")
# cola_caracteres.add("u")
# cola_caracteres.add("q")
# cola_caracteres.add("u")
# cola_caracteres.add("e")
# cola_caracteres.add("n")

def mostrar_cola(cola):
    i=0
    while (cola.tamanio()-1>=i):
        print (cola.mover_final())
        i+=1

def eliminar_vocales(cola):
    i=0
    tamanio = cola.tamanio()-1
    while (tamanio>=i):
        caracter = cola_caracteres.delete()
        if ((caracter != "a") and (caracter != "e") and(caracter != "i") and(caracter != "o") and(caracter != "u")):
            cola_caracteres.add(caracter)
        i+=1

# eliminar_vocales(cola_caracteres)
# mostrar_cola(cola_caracteres)

# 2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.
pila_caracteres=Pila()

def cola_a_pila (cola,pila):
    while (not cola.cola_vacia()):
        x=cola.delete()
        pila.apilar(x)

def pila_a_cola(cola,pila):
    while (not pila.pila_vacia()):
        x = pila.desapilar()
        cola.add(x)

# mostrar_cola(cola_caracteres)
# cola_a_pila(cola_caracteres,pila_caracteres)
# pila_a_cola(cola_caracteres,pila_caracteres)
# mostrar_cola(cola_caracteres)

# 3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.

def copia_cola(cola,cola_aux):
    i=0
    while (cola.tamanio()-1>=i):
        cola_aux.add(cola.mover_final())
        i+=1

def comparar_cola(cola,cola_aux):
    i=0
    c=0
    if (cola.tamanio()==cola_aux.tamanio()):
        while (cola.tamanio()-1>=i):
            elemento1=cola.mover_final()
            elemento2=cola_aux.mover_final()
            if (elemento1 == elemento2):
                c=c+1
            i+=1
    if (c == cola.tamanio()):
        return True
    else:
        return False

# copia_cola(cola_caracteres,cola_aux)
# cola_a_pila(cola_caracteres, pila_caracteres)
# pila_a_cola(cola_caracteres, pila_caracteres)
# boolean =comparar_cola(cola_caracteres,cola_aux)
# if (boolean==True):
#     print ("es un palindromo")
# elif (boolean==False):
#     print ("no es un palindromo")

# 4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
cola_numeros=Cola()

def cargarN_random(cola):
    for i in range (0,15):
        numero = randint(0,10)
        cola.add(numero)

def numero_primo(num):
    if (num==0) or (num==1):
        return False
    elif (num==2):
        return True
    elif (num>2):
        for div in range (2,num):
            if (num % div == 0):
                return False
            if (num % div != 0)and (div == (num //2)+1):
                return True

def eliminar_primos(cola):
    tamanio=cola.tamanio()-1
    i=0
    while (tamanio>=i):
        numero = cola.delete()
        boolean = numero_primo(numero)
        if (boolean==True):
            cola.add(numero)
        i+=1

# cargarN_random(cola_numeros)
# mostrar_cola(cola_numeros)
# print ()
# eliminar_primos(cola_numeros)
# mostrar_cola(cola_numeros)

# 5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.
# pila_caracteres.apilar("a")
# pila_caracteres.apilar("e")
# pila_caracteres.apilar("b")
# pila_caracteres.apilar("g")
# pila_caracteres.apilar("j")
# pila_caracteres.apilar("w")
# pila_caracteres.apilar("g")
# pila_caracteres.apilar("d")
# pila_caracteres.apilar("a")
# pila_caracteres.apilar("a")

# pila_a_cola(cola_caracteres,pila_caracteres)
# mostrar_cola(cola_caracteres)

# 6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.

def contar_ocurrencias(cola, buscado):
    i=0
    cont=0
    while (cola.tamanio()-1>=i):
        elemento = cola.mover_final()
        if (elemento==buscado):
            cont+=1
        i+=1
    return cont

# cargarN_random(cola_numeros)
# numero = int(input("ingrese un numero para ver cuantas veces se repite: "))
# ocurrencias= contar_ocurrencias(cola_numeros,numero)
# print("la cantidad de ocurrencias es de: ",ocurrencias)

#7. Eliminar el i-ésimo elemento después del frente de la cola.

def eliminar_pos(pos,cola):
    i=0
    pos-=1
    tamanio=cola.tamanio()-1
    while (tamanio>=i):
        elemento = cola.delete()
        if (i!=pos):
            cola.add(elemento)
        i+=1

# pos=2
# cargarN_random(cola_numeros)
# mostrar_cola(cola_numeros)
# print()
# eliminar_pos(pos, cola_numeros)
# mostrar_cola(cola_numeros)

# 8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando solo una cola 
# como estructura auxiliar.

def rellenar_cola(cola,cola_aux):
    while (not cola_aux.cola_vacia()):
        cola.add(cola_aux.delete())

def ordenamiento (cola):
    while (not cola.cola_vacia()):
        i=0
        min=cola.delete()
        tamanio=cola.tamanio()-1
        while (tamanio>=i):
            elemento=cola.delete()
            if (elemento <= min):
                cola.add(min)
                min=elemento
            else:
                cola.add(elemento)
            i+=1
        cola_aux.add(min)
    rellenar_cola(cola,cola_aux)

# cargarN_random(cola_numeros)
# mostrar_cola(cola_numeros)
# print()
# ordenamiento(cola_numeros)
# mostrar_cola(cola_numeros)

#9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay. 

def minimo(cola):
    i=0
    min= +100
    while (cola.tamanio()-1 >=i):
        elemento=cola.mover_final()
        if (elemento <= min):
            min=elemento
        i+=1
    return min

def maximo(cola):
    i=0
    max= -100
    while (cola.tamanio()-1 >=i):
        elemento=cola.mover_final()
        if (elemento >= max):
            max=elemento
        i+=1
    return max

def cont_negativo(cola):
    negativo=0
    i=0
    while (cola.tamanio()-1>=i):
        elemento = cola.mover_final()
        if (elemento < 0):
            negativo+=1
        i+=1
    return negativo

# cargarN_random(cola_numeros)
# mostrar_cola(cola_numeros)
# print ("el rango es desde ",minimo(cola_numeros),"hasta ",maximo(cola_numeros))
# print("hay ",cont_negativo(cola_numeros)," numeros negativos")

# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta 
# con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra  ‘Python’, sin perder datos en la cola;  
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43  y las 15:57, y determinar cuántas son.
cola_notificacion=Cola()
cola_notificacion.add({"app":"Facebook","mensaje":"has recibido una nueva solicitud de amistad","hora":"16:30"})
cola_notificacion.add({"app":"Facebook","mensaje":"rocio agrego un artivo en venta en 'mercado libre'","hora":"11:50"})
cola_notificacion.add({"app":"Facebook","mensaje":"tienes una nueva sugerencia de amistad","hora":"14:20"})
cola_notificacion.add({"app":"Twitter","mensaje":"nuevo curso python para principiantes","hora":"20:15"})
cola_notificacion.add({"app":"Twitter","mensaje":"aprende java gratis con estos cursos","hora":"23:20"})
cola_notificacion.add({"app":"Twitter","mensaje":"python el mejor lenguaje de programacion","hora":"13:00"})
cola_notificacion.add({"app":"juego","mensaje":"tus vidas han sido recargadas","hora":"12:23"})

def eliminar_elementos(cola,campo,a_eliminar):
    i=0
    tamanio = cola.tamanio()-1
    while (tamanio>=i):
        elemento = cola.delete()
        if (elemento[campo]!=a_eliminar):
            cola.add(elemento)
        i+=1

def palabra_en_texto(cola,campo,palabra,cola_aux):
    k=0
    while(cola.tamanio()-1>=k):
        noti=cola.obtener_elemento(j)
        texto= noti[campo]
        for i in range(0,len(texto)-1):
            if (texto[i]==buscado[0]):
                for j in range (1,len(buscado)):
                    if (texto[i+j]==buscado[j]):
                        print (buscado[j])
        k+=1


def copia_elementos(cola,campo,a_copiar,copia):
    i=0
    tamanio = cola.tamanio()-1
    while (tamanio>=i):
        elemento = cola.delete()
        if (elemento[campo]==a_copiar):
            copia.add(elemento)
        cola.add(elemento)
        i+=1

def copia_desde_hasta(cola,campo,desde,hasta,copia):
    i=0
    tamanio = cola.tamanio()-1
    while (tamanio>=i):
        elemento = cola.delete()
        if ((elemento[campo]>desde)and(elemento[campo]<hasta)):
            copia.add(elemento)
        cola.add(elemento)
        i+=1
# def mostrar_campo(cola,campo):
#     i=0
#     while (cola.tamanio())-1>=i):
#         print ()
#         i+=1


# copia_desde_hasta(cola_notificacion,"hora","11:43","15:57",pila_aux)
# eliminar_elementos(cola_notificacion,"app","Facebook")
# copia_elementos(cola_notificacion,"app","Twitter",cola_aux)



# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta 
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks[96]
# 12. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una 
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, 
# ni métodos de ordenamiento.
# 13. Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades:
# a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
# b. determinar cuántas letras hay en la segunda cola.
# c. determinar además si existen los caracteres “?” y “#”.
# 14. Realizar un algoritmo que permita realizar las siguientes funciones:
# a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en verde –cargue 
# al menos tres semáforos–.
# b. simular el funcionamiento de los semáforos cargados (cola circular).
# c. debe mostrar por pantalla el cambio de colores y el número del semáforo.
# 15. Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un Destructor Estelar 
# y necesita localizar la base rebelde más cercana– y se tiene una cola con información de las bases rebeldes
# en la tierra de las cuales conoce su nombre, número de flota aérea, 
# coordenadas de latitud y longitud. Desarrolle un algoritmo que permita resolver las siguientes 
# tareas una vez que aterrice:
# a. determinar cuál es la base rebelde más cercana desde su posición actual.
# b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine:
# donde r es el radio medio de la tierra en metros (6371000), φ1 y φ2 las latitudes de los 
# dos puntos –por ejemplo coordenadas actual–, λ1 y λ2 las longitudes de los dos puntos 
# –coordenadas de la base– ambos expresadas en radianes; para convertir de grados a 
# radianes utilice la función math.radians(ángulo coordenada).
# c. mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y determinar cual tiene mayor flota aérea.
# d. determinar la distancia hasta la base rebelde con mayor flota aérea.[97]
# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente 
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la 
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con 
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.
# 17. Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un procesador, 
# de los cuales se conoce id del proceso y tiempo de ejecución. Resuelva las siguientes situaciones:
# a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando la función time.sleep (segundos) – hasta que se vacíe la cola.
# b. considerar que el quantum de tiempo asignado por el procesador a cada proceso es como 
# máximo 4.5 segundos –si el proceso no terminó su ejecución deberá volver a la cola con el 
# tiempo restante para terminar su ejecución–.
# c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se le agotó el 
# quantum de tiempo, se pueden ingresar nuevos procesos a la cola por el usuario.
# d. no se aplican criterios de prioridad en los procesos.
# 18. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una 
# letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo 
# que resuelva las siguientes situaciones:
# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
# y F, y la cola_2 con el resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras 
# tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea 
# mayor que 506.[98]
# 19. Modificar las funciones de arribo y atención del TDA cola para adaptarlo a una cola circular, 
# que no necesite la función mover al final; y desarrollar un función que permita realizar un barrido de dicha estructura respetando el principio de funcionamiento de la cola.
# 20. Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro), 
# que resuelva las siguientes actividades:
# a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son 
# los siguientes:
# I. automóviles (tarifa $47);
# II. camionetas (tarifa $59);
# III. camiones (tarifa $71);
# IV. colectivos (tarifa $64).
# b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
# c. determinar qué cabina recaudó mayor cantidad de pesos ($).
# d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.
# 21. Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un aeropuerto que tiene una pista, contemplando 
# las siguientes actividades:
# a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada, aeropuerto de origen, aeropuerto de destino y su 
# tipo (pasajeros, negocios o carga).
# b. utilizar una cola para administrar los despegues, se deben cargan ordenados por horario de salida. Otra para los aterrizajes, 
# se deben agregan a medida que arriban al aeropuerto.
# c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.
# d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas colas después de realizar una atención.
# e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje –dado que son aviones que están sobrevolando en 
# la zona de espera–, salvo que sea el horario de salida del primer avión de la cola de despegue, en ese caso se deberá atender 
# dicho despegue.[99]
# f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de despegue y aterrizaje –adaptados a segundo 
# para los fines prácticos del ejercicio–:
# I. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
# II. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
# III. carga (aterrizaje = 12 segundos, despegue = 9 segundos).
# g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para más tarde cuando se lo atiende para 
# despegar (en esta caso el horario de salida será mayor que el  último de la cola).
# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del 
# superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, 
# {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.