# Cálculo del año bisiesto

try:
    año = int(input('¿Cuál es el año? '))
    if  año % 400 == 0:
        print('El año',año,'es bisiesto')
    elif año % 100 == 0:
        print('El año',año,'no es bisiesto')
    elif año % 4 == 0:
        print('El año',año,'es bisiesto')
    else:
        print('El año',año,'no es bisiesto')
except:
    print('Dato no válido')
    


