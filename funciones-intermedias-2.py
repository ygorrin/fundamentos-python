#1.Actualiza los valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
def cambio(lista):
    for i in range(len(lista)):
        for x in range(len(lista[i])):
            if lista[i][x] == 10:
                lista[i][x] = 15
    print(lista)
x = [ [5,2,3], [10,8,9] ] 
cambio(x)

#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'

def cambio(sports_directory):
    for lista in sports_directory:
        for x in range(len(sports_directory[lista])):
            if sports_directory[lista][x] == 'Jordan':
                sports_directory[lista][x] = 'Bryant'
    print(sports_directory)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
} 
cambio(sports_directory)

#En el directorio sports_directory, cambia 'Messi' a 'Andres'

def cambio(sports_directory):
    for lista in sports_directory:
        for x in range(len(sports_directory[lista])):
            if sports_directory[lista][x] == 'Messi':
                sports_directory[lista][x] = 'Andres'
    print(sports_directory)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
} 
cambio(sports_directory)

#2 Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de 
# la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for x in students:
            print(f'first_name - {x["first_name"]}, last_name - {x["last_name"]}')
iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel


#3.Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
#Michael John Mark KB


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def  iterateDictionary2 (key, lista):
    for x in lista:                     
        print(x[key])
iterateDictionary2 ('first_name', students)


#4.Itera a través de un diccionario con valores de listas
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(objeto):
    for key in objeto.keys():
        print(key)
        for value in objeto.values():
            print(value)
printInfo(dojo)




# output:
#7 LOCATIONS
#San Jose
#Seattle
#Dallas
#Chicago
#Tulsa
#DC
#Burbank
#    
#8 INSTRUCTORS
#Michael
#Amy
#Eduardo
#Josh
#Graham
#Patrick
#Minh
#Devon