
#Costo de despacho en cajas

def calcular_despacho(unidades_ped,unidades_caja,costo_caja):
    if unidades_ped <= 0 or unidades_caja <= 0 or costo_caja <= 0:
        costo = 'Datos no válidos'
    elif unidades_ped % unidades_caja == 0:
        no_cajas = (unidades_ped // unidades_caja)
        costo = no_cajas * costo_caja
    else:
        no_cajas = (unidades_ped // unidades_caja) + 1
        costo = no_cajas * costo_caja
    return costo
try:
    up = int(input('Unidades pedidas: '))
    uc = int(input('Unidades por caja: '))
    cc = float(input('Costo por caja: '))
    costo_final = calcular_despacho(up,uc,cc)
    print('Costo de despacho:',costo_final)
except:
    print('Error: ingrese solo números')
        

    
