#Clasificador de clientes por facturación (pequeño, mediano, grande)

try:
    facturacion_anual=float(input('¿Cuál es la facturación anual del cliente? (millones de pesos) '))
    if facturacion_anual < 0:
        print('Facturación no válida')
    elif facturacion_anual == 0:
        print('Sin facturación: no es cliente activo')
    elif facturacion_anual < 100:
        print('Cliente pequeño')
    elif facturacion_anual <= 1000:
        print('Cliente mediano')
    else:
        print('Cliente grande')
except:
    print('Dato no válido')
    
