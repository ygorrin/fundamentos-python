# 1. TAREA: imprimir "Hola mundo"
print ("Hola Mundo") 

# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print( "Hola", name )	# con una coma
print( "Hola " + name )	# con un +

# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print( "Hola", name, "!")	# con una coma
print( f"Hola {name} !")	# con un + - !Este debería darnos un error!

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print(f"Me encanta {fave_food1} and {fave_food2}") # con una cadena f
print("Me encanta comer {} y {}".format(fave_food1, fave_food2) ) # con .format()

comida1 = "Arepa"
comida2 = "Huevo"
print(f"Me encanta comer {comida1} con {comida2}")
print("Me encanta comer {} con {}".format(comida1,comida2))