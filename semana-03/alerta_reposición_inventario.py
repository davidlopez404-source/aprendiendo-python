#Alertas de reposicion de inventario

def revisar_inventario(stock,demanda,días_repo):
    punto_reorden = demanda*días_repo
    if stock <0 or demanda <= 0 or días_repo <=0:
        estado = 'Datos no válidos'
    elif stock <= punto_reorden:
        estado = 'Pedir ahora'
    else:
        estado = 'Stock suficiente'
    return estado


try:
    inventario = int(input('Stock actual: '))
    demanda_día = int(input('Demanda diaria: '))
    dias_entrega = int(input('Días de entrega: '))
    pr = revisar_inventario(inventario,demanda_día,dias_entrega)
    print('Estado:',pr)
except:
    print('Error: ingrese solo números')
