#convertidor de tiempo
try:
    tiempo = int(input('Escribe el tiempo en segundos: '))
    if tiempo < 0:
        print('No puede ser negativo')
    elif tiempo == 0:
        print('No hay tiempo que convertir')
    else:
        print('El tiempo es',tiempo//3600,'horas',tiempo%3600//60,'minutos','y',tiempo%60,'segundos')
except:
    print('El valor debe ser numérico')
print('Cálculo terminado')
