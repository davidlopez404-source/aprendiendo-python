#Aprobación del descuento

try:
    compra = int(input('Valor de la compra ($COP): ')) #en pesos
    es_frecuente = input('¿Es cliente frecuente? (si/no): ') == 'si'
    if compra>=100000 and es_frecuente:
        print('Descuento del 20%')
    elif compra>=100000 or es_frecuente:
        print('Descuento del 10%')
    else:
        print('Sin descuento')
except:
    print('Dato no válido')

