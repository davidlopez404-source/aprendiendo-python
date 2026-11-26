import math

#Punto de reorden con stock de seguridad

def calcular_punto_reorden(demanda_dia,variacion_dia,dias_entrega):
    if demanda_dia <= 0 or variacion_dia < 0 or dias_entrega < 1:
        punto_reorden = 'Datos no válidos'
    else:
        stock_seg = 1.65 * variacion_dia * math.sqrt(dias_entrega)
        punto_reorden = demanda_dia * dias_entrega + stock_seg
    return punto_reorden

try:
    demanda_diaria = float(input('Demanda diaria: '))
    variacion_diaria = float(input('Variación diaria: '))
    dias_entrega_1 = int(input('Días de entrega: '))
    reorden = calcular_punto_reorden(demanda_diaria,variacion_diaria,dias_entrega_1)
    print('Punto de reorden:',reorden)
except:
    print('Error: ingrese solo números')


