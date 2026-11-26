#factura con descuento por volumen

def calcular_total(cantidad_unid,valor_uni):
    subtotal = cantidad_unid*valor_uni
    if cantidad_unid <= 0 or valor_uni <= 0:
        total = 'Pedido no válido'
    elif subtotal >= 1000000:
        total = (subtotal - subtotal*0.1)*1.19
    else:
        total = subtotal*1.19
    return total

try:
    cantidad = int(input('Cantidad: '))
    precio = float(input('Precio unitario: '))
    total_pagar = calcular_total(cantidad,precio)
    print('Total a pagar:',total_pagar)
except:
    print('Error: ingrese solo números')
    
        
    
    
    
