#1. Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
def ctaRegresiva(num):
    array = []
    for i in range(num, -1, -1):
        array.append(i)
    return array
num = int(input('Ingresa un número:'))
print(ctaRegresiva(num))
print("*"*50)

#2. Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def imprimirYvolver(a,b):
    print (a)
    return (b)

print(imprimirYvolver(1,2))
imprimirYvolver(1,2)
print("*"*50)

#3. First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
#Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def firstPlusLength(list):
    #for i in range (len(list)):
        return (list[0] + len(list))

list= [5,4,3,21]
print(firstPlusLength(list))
print("*"*50)

#4. Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
def values_greater_than_second(list):
    new_list = []
    for i in range (len(list)):
        if len(list) < 2:
            return False
        else:    
            if list[i] > list[1]:    
                new_list.append(list[i])
    print(len(new_list))
    return new_list
     
lista = [5,2,3,2,1,4]
print(values_greater_than_second(lista))
print("*"*50)

#5. Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]

def length_and_value(a,b):
    array = []
    for i in range(a):
        #a = len(array)
        array.append(b)
    return array

print(length_and_value(4,7))
print ('*'*50)