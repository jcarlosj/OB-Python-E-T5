# Escribe una función que pueda decirte si un número (número entero) es primo o no.
def es_primo( number ) :
    if number < 2:
        return False

    for i in range( 2, number ) :
        if number % i == 0:
            return False
    
    return True

number = 3
print ( f'El numero { number } { "es primo" if es_primo( number ) else "NO es primo" }' )

number = 119
print ( f'El numero { number } { "es primo" if es_primo( number ) else "NO es primo" }' )