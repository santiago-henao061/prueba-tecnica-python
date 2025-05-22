# Crea una función llamada numero_mas_frecuente(lista) que reciba una lista de
# números enteros y devuelva el número que más veces se repite. Si hay más de uno con la
# misma frecuencia, devuelve el menor de ellos.


def numero_mas_frecuente(list_num:list):
    """Esta funcion sacara la moda (numero mas frecuente) de una lista de numeros, "sin importar librerias solo python".
    
    Args:
        list_num (list): lista de numeros a evaluar
        
    Returns:
        num_enviar: se hace la validacion para enviar el numero con mayor frecuencia y si hay mas de uno devuelve el menor
        
    """
    conteo_numeros = {}
    #iteramos sobre la lista para realizar un conteo y adicionarlo al diccionario
    for numero in list_num:
        #validamos si el numero existe en el diccionario si existe le adiciona +1 al campo correspondiente
        if numero in conteo_numeros:
            conteo_numeros[numero] += 1
            
        #si el numero no existe en el diccionario lo crea y le agrega 1 para el conteo 
        else:
            conteo_numeros[numero] = 1
    #ejemplo de resultado moda={1:2,3:1,5:4.....n:num_veces}

    #traemos los valores del diccionario y sacamos el numero maximo de ellos
    numero_max_moda = max(conteo_numeros.values())

    numeros_enviar = []
    #iteramos sobre el diccionario de numeros
    for numero in conteo_numeros:
        #si el valor en el campo del numero del diccionario es igual al numero maximo de la moda lo agrega a la lista
        if conteo_numeros[numero] == numero_max_moda:
            numeros_enviar.append(numero)
    
    #sacamos el numero menor de la lista de numeros para la exception de si hay dos numeros iguales en moda 
    numero_moda=min(numeros_enviar)
    
    return numero_moda

#validacion rapida del funcionamiento de la funcion 
print(numero_mas_frecuente([9,8,8,9,7,2,1,2]))