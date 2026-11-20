#alertas de un servidor
#Un programa revisa cuánto se está usando el procesador (CPU) y la memoria, y lanza alertas.

try:
    cpu = int(input('Uso de CPU, en porcentaje: '))
    memoria = int(input('Uso de memoria, en porcentaje: '))
    if cpu < 0 or memoria < 0 or cpu > 100 or memoria > 100:
        print('Lectura fuera de rango')
    elif cpu >= 90 or memoria >= 90:
        print('ALERTA CRÍTICA')
    elif cpu >= 70 and memoria >= 70:
        print('Advertencia')
    else:
        print('Normal')
except:
    print('Dato no válido')
