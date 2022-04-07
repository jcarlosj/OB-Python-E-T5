# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def es_bisiesto( anio ) :
        return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0;

anio = 2016
print ( f'El año { anio } { "es bisiesto" if es_bisiesto( anio ) else "NO es bisiesto" }' )

anio = 2022
print ( f'El año { anio } { "es bisiesto" if es_bisiesto( anio ) else "NO es bisiesto" }' )
