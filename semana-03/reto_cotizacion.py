#Cotización de consultoría con tipo de cliente

# Calcula el total a cobrar por las horas de consultoría, con IVA del 19 %
def calcular_total(horas,tarifa):
    if horas <= 0 or tarifa <= 0:
        total = 'Datos no válidos'
    else:
        total = horas * tarifa *1.19
    return total

# Clasifica al cliente según su facturación anual
def clasificar_cliente(factura_anual):
    if factura_anual < 0:
        tipo_cliente = 'Datos no válidos'
    elif factura_anual == 0:
        tipo_cliente = 'Cliente inactivo'
    elif factura_anual < 500000000:
        tipo_cliente = 'Cliente pequeño'
    elif factura_anual < 2000000000:
        tipo_cliente = 'Cliente mediano'
    else:
        tipo_cliente = 'Cliente grande'
    return tipo_cliente

try:
    horas_trabajadas = float(input('Horas: '))
    tarifa_hora = float(input('Tarifa por hora: '))
    facturacion_anual = float(input('Facturación anual del cliente: '))
    total_cobro = calcular_total(horas_trabajadas,tarifa_hora)
    cliente = clasificar_cliente(facturacion_anual)
    print('Total a cobrar:',total_cobro)
    print('Tipo de cliente:',cliente)
except:
    print('Error: ingrese solo números')
