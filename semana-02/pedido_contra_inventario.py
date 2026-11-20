#Pedido contra inventario

try:
    unidades = int(input('Unidades disponibles: '))
    pedidos = int(input('Unidades pedidas: '))
    if unidades<0 or pedidos<=0:
        print('Cantidad no válida')
    elif unidades<pedidos:
        print('Stock insuficiente, faltan',pedidos-unidades,'unidades')
    elif unidades==pedidos:
        print('Pedido aprobado. Producto agotado, hay que reabastecer')
    else:
        print('Pedido aprobado. Quedan',unidades-pedidos,'unidades')   
except:
    print('Dato no válido')
