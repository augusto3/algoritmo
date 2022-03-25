from lista import Lista
# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, 
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar 
# las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

lista_personajes=Lista()

lista_personajes.insertar({"nombre":"Flash","anio":1940,"comic":"DC","biografia":"corre rapido"},"nombre")
lista_personajes.insertar({"nombre":"Star-Lord","anio":1976,"comic":"Marvel","biografia":"policia interplanetario"},"nombre")
lista_personajes.insertar({"nombre":"Linterna Verde","anio":1940,"comic":"DC","biografia":"anillo de poder"},"nombre")
lista_personajes.insertar({"nombre":"Capitana Marvel","anio":1995,"comic":"Marvel","biografia":"IA"},"nombre")
lista_personajes.insertar({"nombre":"Wolverine","anio":1974,"comic":"Marvel","biografia":"garras de acero"},"nombre")
lista_personajes.insertar({"nombre":"Mujer Maravilla","anio":1941,"comic":"DC","biografia":"latigo y arco"},"nombre")
lista_personajes.insertar({"nombre":"Dr. Strange","anio":1963,"comic":"DC","biografia":"hechizero supremo protector de la tierra"},"nombre")
lista_personajes.insertar({"nombre":"Iron Man","anio":1963,"comic":"Marvel","biografia":"tiene un traje de acero con una IA y armas"},"nombre")

def busqueda_caracteres(texto,buscado):
    for i in range(0,len(texto)-1):
        if (texto[i]==buscado[0]):
            c=1
            for j in range (1,len(buscado)-1):
                if (texto[i+j]==buscado[j]):
                    c+=1
                    if c==len(buscado)-1:
                        return True

def barrido_traje(lista):
    pos=0
    while (pos <= lista.tamanio()-1):
        elemento = lista.obtener_elemento(pos)
        if (busqueda_caracteres(elemento["biografia"],"traje")):
            print (elemento["nombre"])
        pos+=1

def barrido_año(lista,anio):
    pos=0
    while (pos <= lista.tamanio()-1):
        elemento = lista.obtener_elemento(pos)
        if (elemento["anio"]< anio):
            print (elemento["nombre"],", casa: ",elemento["comic"])
        pos+=1

def mostrarBMS (lista):
    pos=0
    while (pos <= lista.tamanio()-1):
        personaje = lista.obtener_elemento(pos)
        aux = personaje["nombre"]
        if ((aux[0]=="B")or(aux[0]=="M")or(aux[0]=="S")):
            print (aux)
        pos+=1

def casaComic (lista):
    pos=0
    cont1=0
    cont2=0
    while (pos<=lista.tamanio()-1):
        personaje =lista.obtener_elemento(pos)
        aux=personaje["comic"]
        if (aux=="Marvel"):
            cont1 += 1
        else:
            cont2 +=1
        pos+=1
    print ("marvel= ",cont1)
    print ("DC= ",cont2)

lista_personajes.eliminar("Linterna Verde", "nombre")
pos = lista_personajes.busqueda("Wolverine","nombre")
wolv = lista_personajes.obtener_elemento(pos)
print ("el anio de aparicion de wolverine es: ",wolv["anio"])
strange = lista_personajes.eliminar("Dr. Strange","nombre")
strange["comic"]="Marvel"
lista_personajes.insertar(strange,"nombre")
barrido_traje(lista_personajes)

barrido_año(lista_personajes, 1963)

pos=lista_personajes.busqueda("Capitana Marvel","nombre")
aux=lista_personajes.obtener_elemento(pos)
print (aux["nombre"],"pertenece a la casa de comics:",aux["comic"])
pos=lista_personajes.busqueda("Mujer Maravilla","nombre")
aux=lista_personajes.obtener_elemento(pos)
print (aux["nombre"],"pertenece a la casa de comics:",aux["comic"])

pos=lista_personajes.busqueda("Flash","nombre")
aux=lista_personajes.obtener_elemento(pos)
print (aux["nombre"],"pertenece a la casa de comics:",aux["comic"]," con su primera aparicion en el anio:",aux["anio"],"y su biografia es:",aux['biografia'])
pos=lista_personajes.busqueda("Star-Lord","nombre")
aux=lista_personajes.obtener_elemento(pos)
print (aux["nombre"],"pertenece a la casa de comics:",aux["comic"]," con su primera aparicion en el anio:",aux["anio"],"y su biografia es:",aux['biografia'])
mostrarBMS(lista_personajes)
casaComic(lista_personajes)

# 7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

lista1=Lista()
lista2=Lista()
concadenacion=Lista()

lista1.insertar(1)
lista1.insertar(2)
lista1.insertar(3)
lista1.insertar(7)
lista1.insertar(9)

lista2.insertar(1)
lista2.insertar(3)
lista2.insertar(4)
lista2.insertar(5)
lista2.insertar(8)

def concadenar(lista1,lista2):
    pos=0
    while (pos<=lista2.tamanio()-1):
        lista1.insertarPos(lista1.tamanio(),lista2.obtener_elemento(pos))
        pos+=1

def eliminarRep (lista):
    pos=0
    while (pos<lista.tamanio()-1):
        if (lista.obtener_elemento(pos)==lista.obtener_elemento(pos+1)):
            lista.eliminarPos(pos)
        pos+=1

def contRep (lista):
    pos=0
    rep=0
    while (pos<lista.tamanio()-1):
        if (lista.obtener_elemento(pos)==lista.obtener_elemento(pos+1)):
            rep+=1
        pos+=1
    print (rep)

def mostrarRemove(lista):
    while (not lista.lista_vacia()):
        print (lista.eliminarPos(0))

concadenar(lista1,lista2)
lista1.ordenar()
eliminarRep(lista1)
contRep(lista1)
lista1.barrido()
mostrarRemove(lista1)
lista1.barrido()

# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad 
# de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de 
# sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver 
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador(tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador 
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se 
# deberán mostrar los datos de ambos;
lista_entrenadores = Lista()

entrenadores = [{'name':'juan','torneos_ganados': 12, 'batallas_perdidas' : 5, 'batallas_ganadas': 32, 'pokemons': Lista()},
                {'name':'enzo','torneos_ganados': 2, 'batallas_perdidas' : 8, 'batallas_ganadas': 20, 'pokemons': Lista()},
                {'name':'maria','torneos_ganados': 4, 'batallas_perdidas' : 15, 'batallas_ganadas': 28, 'pokemons': Lista()},]

pokemons = [{'name':'tyrantrum','nivel':12,'tipo':'fuego','subtipo':'planta','entrenador':'juan'},
            {'name':'wingull','nivel':180,'tipo':'agua','subtipo':'volador','entrenador':'juan'},
            {'name':'wolverine','nivel':3,'tipo':'fuego','subtipo':'terreno','entrenador':'enzo'},
            {'name':'tyrantrum','nivel':12 ,'tipo':'fuego','subtipo':'planta','entrenador':'maria'},
            {'name':'wingull','nivel':18,'tipo':'agua','subtipo':'volador','entrenador':'enzo' },
            {'name':'tyrantrum','nivel':12 ,'tipo':'fuego','subtipo':'planta','entrenador':'maria' },
            {'name':'gigante','nivel':21,'tipo':'agua','subtipo':'volador','entrenador':'juan' },
            {'name':'rayo','nivel':3,'tipo':'fuego','subtipo':'terreno','entrenador':'enzo' },
            {'name':'terrakion','nivel':21 ,'tipo':'roca','subtipo':'lucha','entrenador':'maria'}]

def cargarEntrenadores(lista,entrenadores):
    for entrenador in entrenadores:
        lista.insertar(entrenador, 'name')
cargarEntrenadores(lista_entrenadores,entrenadores)

def cargarPokemon(lista,pokemons):
    for pokemon in pokemons:
        pos = lista.busqueda(pokemon['entrenador'], 'name')
        if(pos > -1):
            del pokemon['entrenador']
            lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon, 'name')
cargarPokemon(lista_entrenadores,pokemons)
name='enzo'
pos = lista_entrenadores.busqueda(name, 'name')
if(pos != -1):
    print('cantidad de pokemones de ', name,': ',lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio())

def mas3Trofeos(lista):
    print ('entrenadores con mas de 3 trofeos:')
    for i in range (lista.tamanio()):
        aux=lista.obtener_elemento(i)
        if (aux['torneos_ganados']>3):
            print ('entrenador: ',aux['name'])
mas3Trofeos(lista_entrenadores)

def masTrofeos(lista):
    maximo = 0
    pos_maximo = -1
    for i in range(lista.tamanio()):
        if(lista.obtener_elemento(i)['torneos_ganados'] > maximo):
            maximo = lista.obtener_elemento(i)['torneos_ganados'] 
            pos_maximo = i
    return pos_maximo
posTrofeo=masTrofeos(lista_entrenadores)
print('entrenador con mas trofeos: ',lista_entrenadores.obtener_elemento(posTrofeo)['name'])

def masNivel(lista,pos):
    nivel_max = 0
    posMax = -1
    for i in range(lista.obtener_elemento(pos)['pokemons'].tamanio()):
        if(lista.obtener_elemento(pos)['pokemons'].obtener_elemento(i)['nivel'] > nivel_max):
            nivel_max = lista.obtener_elemento(pos)['pokemons'].obtener_elemento(i)['nivel']
            posMax = i
    return posMax
posNivel=masNivel(lista_entrenadores,posTrofeo)
print('su pokemon con mayor nivel es: ',lista_entrenadores.obtener_elemento(posTrofeo)['pokemons'].obtener_elemento(posNivel)['name'])
print('entrenador:',lista_entrenadores.obtener_elemento(posTrofeo)['name'],',torneos ganados:', lista_entrenadores.obtener_elemento(posTrofeo)['torneos_ganados'],',batallas ganadas:', lista_entrenadores.obtener_elemento(posTrofeo)['batallas_ganadas'],',batallas perdidas:', lista_entrenadores.obtener_elemento(posTrofeo)['batallas_perdidas'])
print('pokemons:')
lista_entrenadores.obtener_elemento(posTrofeo)['pokemons'].barrido()

def ganadas_porcentaje(listae,porcentaje):
    print ('los entrenadores con mas del ',porcentaje,' porciento son:')
    for i in range(listae.tamanio()):
        lista=listae.obtener_elemento(i)
        total = lista['batallas_ganadas']+lista['batallas_perdidas']
        if ((lista['batallas_ganadas']*100/total)>porcentaje):
            print (lista['name'])
porcentaje=79
ganadas_porcentaje(lista_entrenadores,porcentaje)

def tipoysub(listae):
    for j in range(listae.tamanio()):
        lista=listae.obtener_elemento(j)
        for i in range(lista['pokemons'].tamanio()):
            poke=lista['pokemons'].obtener_elemento(i)
            if ((poke['tipo'] =='fuego') and (poke['subtipo']=='planta')):
                print ('entrenador de tipo fuego, subtipo planta:',lista['name'])
            if ((poke['tipo'] =='agua') and (poke['subtipo']=='volador')):
                print ('entrenador de tipo agua, subtipo volador:',lista['name'])
tipoysub(lista_entrenadores)

def promedio(listae):
        pos=0
        total=0
        lista=listae.obtener_elemento(pos)
        for i in range(lista['pokemons'].tamanio()):
            total+= lista['pokemons'].obtener_elemento(i)['nivel']
        print ('el promedio de nivel de ',lista['name'],' es: ',total/lista['pokemons'].tamanio())
promedio(lista_entrenadores)

def busquedaPokemon(lista,buscado):
    print('los entrenadores con el pokeon ',buscado,' son:')
    for i in range (lista.tamanio()):
        if (lista.obtener_elemento(i)['pokemons'].busqueda(buscado,'name') > -1):
            print(lista_entrenadores.obtener_elemento(i)['name'])
buscado= 'wingull'
busquedaPokemon(lista_entrenadores,buscado)

def pokemonRepetidos(lista):
    print ('los entrenadores con pokemones repetidos son:')
    for j in range (lista.tamanio()):
        for i in range (lista.obtener_elemento(j)['pokemons'].tamanio()-1):
            if (lista.obtener_elemento(j)['pokemons'].obtener_elemento(i)['name']==lista.obtener_elemento(j)['pokemons'].obtener_elemento(i+1)['name']):
                print(lista.obtener_elemento(j)['name'])
pokemonRepetidos(lista_entrenadores)
busquedaPokemon(lista_entrenadores,'tyrantrum')
busquedaPokemon(lista_entrenadores,'terrakion')
busquedaPokemon(lista_entrenadores,'wingull')

def entrenadorXpokemonY(lista, entrenadorX, pokemonY ):
    posEntrenador = lista.busqueda(entrenadorX, 'name')
    if posEntrenador > -1:
        posPokemon = lista.obtener_elemento(posEntrenador)['pokemons'].busqueda(pokemonY, 'name')
        if posPokemon > -1:
            print('El entrenador ', entrenadorX, ' tiene al pokemon ',pokemonY)
            mostrarX=lista.obtener_elemento(posEntrenador)
            print('entrenador: ',mostrarX['name'],' torneos_ganados: ',mostrarX['torneos_ganados'],' batallas ganadas: ',mostrarX['batallas_ganadas'],' batallas perdidas: ',mostrarX['batallas_perdidas'])
            mostrarY = lista.obtener_elemento(posEntrenador)['pokemons'].obtener_elemento(posPokemon)
            print('pokemon: ',mostrarY['name'],' nivel: ',mostrarY['nivel'],' tipo: ',mostrarY['tipo'],' subtipo: ',mostrarY['subtipo'])
        else:
            print('El Entrenador ', entrenadorX, ' no tiene a ',pokemonY)
    else:
        print('El Entrenador ', entrenadorX, ' no esta en la lista')
entrenadorx = input('nombre del entrenador: ')
pokemony = input('nombre del pokemon: ')
entrenadorXpokemonY(lista_entrenadores,entrenadorx,pokemony)

# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, 
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las 
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

Jedis = [
        {'name' : 'Bo Keevil', 'maestro' : 'Mace Windu', 'sables' : [], 'especie' : 'Humana'},
        {'name' : 'Bossk', 'maestro' : 'Yoda' , 'sables' : [], 'especie' : 'Humana'},
        {'name' : 'Boba Fett', 'maestro' : 'Luke Skywalker', 'sables' : [], 'especie' : 'Twi´lek'},
        {'name' : 'Kit Fisto', 'maestro' : 'Qui-Gon Jin' , 'sables' : [], 'especie' : 'Nautolano'},
        {'name' : 'Baby Yoda', 'maestro' : 'Yoda' , 'sables' : [], 'especie' : 'desconocida'},
        {'name' : 'Ahsoka Tano', 'maestro' : 'Luke Skywalker', 'sables' : [], 'especie' : 'Togruta'},
        ]

sables= [['rojo', 'azul'],
        ['rojo'],
        ['blanco', 'violeta'],
        ['violeta', 'amarillo'],
        ['verde', 'verde'],
        ['azul']
        ]

listaJedis = Lista()

for Jedi in Jedis:
    listaJedis.insertar(Jedi, 'name')

for i in range(0, listaJedis.tamanio()):
    listaJedis.obtener_elemento(i)['sables'] = sables[i]

def barridoJedis(lista):
    for i in range (0,lista.tamanio()):
        elemento=lista.obtener_elemento(i)
        print ('nombre: ',elemento['name'])
        print ('maestros: ',elemento['maestro'])
        print ('sables: ',elemento['sables'])
        print ('especie: ',elemento['especie'])
        print ()

listaJedis.ordenar('especie')
barridoJedis(listaJedis)
listaJedis.ordenar('name')
barridoJedis(listaJedis)

def barridoBusqueda(lista,pos):
    elemento=lista.obtener_elemento(pos)
    print ('nombre: ',elemento['name'])
    print ('maestros: ',elemento['maestro'])
    print ('sables: ',elemento['sables'])
    print ('especie: ',elemento['especie'])
    print ()

pos = listaJedis.busqueda('Ahsoka Tano','name')
if (pos != -1):
    barridoBusqueda(listaJedis,pos)

pos = listaJedis.busqueda('Kit Fisto','name')
if (pos != -1):
    barridoBusqueda(listaJedis,pos)

def PadawansDeMaestros(lista, maestro):
    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)
        if (jedi['maestro'] == maestro):
            print(jedi['name'])

print ('padawans de luke Skywalker')
PadawansDeMaestros(listaJedis,'Luke Skywalker')
print ('padawans de Yoda')
PadawansDeMaestros(listaJedis,'Yoda')

def mostrarEspecies(lista, especie):
    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)
        if jedi['especie'] == especie:
            print(jedi['name'])
print ('especie humana:')
mostrarEspecies(listaJedis,'Humana')
print ('especie twi´lek:')
mostrarEspecies(listaJedis,'Twi´lek')

def JedisInicial(lista, letra):
    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)
        if (letra == jedi['name'].upper()[0]):
            print(jedi['name'])
JedisInicial(listaJedis,'A')

def JedisCon2Sables(lista):
    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)
        if len(jedi['sables']) > 1:
            if (jedi['sables'][0]!=jedi['sables'][1]):
                print (jedi['name'])
JedisCon2Sables(listaJedis)

def JedisColorDeSable(lista, color):
    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)
        for j in range(0, len(jedi['sables'])):
            if (jedi['sables'][j] == color) :
                print (jedi['name'])

print ('jedis con sables color amarillo:')
JedisColorDeSable(listaJedis,'amarillo')
print ('jedis con sables color violeta:')
JedisColorDeSable(listaJedis,'violeta')

print ('los padawans de Qui-Gon Jin: ')
PadawansDeMaestros (listaJedis,'Qui-Gon Jin')
print ('los padawansk de Mace Windu: ')
PadawansDeMaestros (listaJedis,'Mace Windu')