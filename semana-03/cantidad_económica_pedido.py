import math

#Calcular cuántas unidades pide cada vez a su proveedor EOQ (cantidad económica de pedido)
#EOQ = raíz cuadrada de (2 × demanda anual × costo por pedido ÷ costo de almacenar una unidad al año)
#regla: Los tres datos deben ser mayores que 0. Si no, la respuesta es Datos no válidos.

def calcular_eoq(demanda,costo_ped,costo_alm):
    if demanda <= 0 or costo_ped <= 0 or costo_alm <= 0:
        eoq = 'Datos no válidos'
    else:
        eoq = math.sqrt(2*demanda*costo_ped/costo_alm)
    return eoq

try:
    demanda_anual = float(input('Demanda anual: '))
    costo_pedido = float(input('Costo por pedido: '))
    costo_almacenar = float(input('Costo de almacenamiento: '))
    eoq_final = calcular_eoq(demanda_anual,costo_pedido,costo_almacenar)
    print('Unidades por pedido:',eoq_final)
except:
    print('Error: ingrese solo números')
