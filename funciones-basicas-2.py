#Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
array = []
def regresa(num): 
    for x in range(num, 0-1, -1):
        array.append(x)
    print(array)
regresa(5)

#Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def dev(a,b):
    print(a)
    return(b)
dev(3,6)

#First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
#Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def plus(array):
    plus = array[0] + len(array)
    print(plus)
    return (plus)
plus([1,2,3,4,5])

#Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de 
# la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista 
# tiene menos de 2 elementos, haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False
lista2 = []
def nuevalista(lista):
    longitud = (len(lista))
    lista2.append(lista[0])
    for x in range(0, longitud-1, 1):
        if lista[x+1]>lista[x]:
            lista2.append(lista[x+1])
    print(len(lista2))
    print(lista2)
nuevalista([5,2,3,2,1,4])

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son 
# todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def vuelve(tamano,valor):
    array = []
    for x in range(tamano):
        array.append(valor)
    print(array)
vuelve(4,7)
vuelve(6,2)