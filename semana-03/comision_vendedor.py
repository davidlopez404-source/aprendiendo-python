#Comisión de un vendedor

def calcular_comision(ventas,meta,porcentaje):
    if ventas <0 or meta <= 0 or porcentaje <= 0 or porcentaje > 100:
        comision = 'Datos no válidos'
    elif ventas < meta:
        comision = 0
    elif ventas >= (1.2 * meta):
        comision = (ventas * porcentaje / 100)+ 500000
    else:
        comision = ventas * porcentaje / 100
    
    return comision

try:
    venta_mes = float(input('Ventas del mes (COP): '))
    meta_mes = float(input('Meta del mes (COP): '))
    porcentaje_com = float(input('Porcentaje de comisión (%): '))
    comision_final = calcular_comision(venta_mes,meta_mes,porcentaje_com)
    print('Comisión:',comision_final)
except:
    print('Error: ingrese solo números')
    
