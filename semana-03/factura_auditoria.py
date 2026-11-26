import random

# El área de control interno revisa facturas cada mes. Como no puede revisarlas todas, elige algunas al azar

def elegir_factura(primera,ultima):
    if primera < 1 or primera >= ultima:
        no_factura = 'Datos no válidos'
    else:
        no_factura = random.randint(primera,ultima)
    return no_factura

try:
    pr_factura = int(input('Primera factura: '))
    ult_factura = int(input('Última factura: '))
    auditar = elegir_factura(pr_factura,ult_factura)
    print('Factura a auditar:',auditar)
except:
    print('Error: ingrese solo números')
