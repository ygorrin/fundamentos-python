#1Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def big(lista):
    for x in range(len(lista)):
        if lista[x] > 1:
            lista[x] = "Big"
    print(lista)
big([- 1, 3, 5, -5])
    

#2Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. 
# (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def contar(array):
    contar = 0
    for x in range (len(array)):
        if array[x]>0:
            contar = contar +1
    array[len(array)-1] = contar
    print(array)

contar([-1,1,1,1])
contar([1,6, -4, -2, -7, -2])

#3Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sumar(array):
    suma=0;
    for x in range(len(array)):
        suma += array[x]
    print(suma)
sumar([1,2,3,4])
sumar([6,3, -2])


#4Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promediar(array):
    promedio=0;
    for x in range(len(array)):
        promedio += array[x]
    promedio = promedio/len(array)
    print(promedio)
promediar([1,2,3,4])


#5Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0
def long(array):
    longitud= len(array)
    print(longitud)
long([37,2,1, -9])
long([])


#6Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False

def minimo(array):
    if len(array) == 0:
        print("False")
        return 'false'
    else:
        min=array[0]
        for x in range (len(array)):
            if array[x]<min:
                min = array[x]
        print(min)
minimo([37,2,1, -9])
minimo([])


#7Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False
def maximo(array):
    if len(array) == 0:
        print("False")
        return 'false'
    else:
        max=array[0]
        for x in range (len(array)):
            if array[x]>max:
                max = array[x]
        print(max)
maximo([37,2,1, -9])
maximo([])


#8Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo 
# y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def valores(array):
    suma=0
    prom = 0
    min = 0
    max = 0
    long = len(array)
    for x in range(len(array)):
        suma += array[x]
        if min> array[x]:
            min = array[x]
        elif max < array[x]:
            max = array[x]
    prom = suma /len(array)
    print({'total': suma, 'promedio': prom, 'minimo': min, 'maximo': max, 'longitud': long})
valores([37,2,1, -9])


#9Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. 
# Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def rever(lista):
    return lista[::-1] 
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(rever(mylist))
print(rever(mylist2))

def revertir(array):
    array2 = []
    for x in range(len(array)-1, -1, -1):
        array2.append(array[x])
    print(array2)
revertir([37,2,1, -9])

def revertir(array):
    temp = 0
    long = int(len(array)/2)
    for x in range(long):
        temp = array[x]
        array[x] = array[len(array) -1- x]
        array[len(array) -1 - x] = temp
    print(array)
revertir([37,2,1,-9])