#Cálculo de costo de envío

try:
    peso = float(input('Peso del paquete (Kg): '))
    if 0<peso<=1:
        print('Costo de envío: 8000 pesos')
    elif 1<peso<=5:
        print('Costo de envío: 15000 pesos')
    elif 5<peso<=20:
        print('Costo de envío:',int(15000+(peso-5)*2000),'pesos')
    elif peso>20:
        print('Paquete demasiado pesado, requiere transportadora especial')
    else:
        print('Peso no válido')
except:
    print('Dato no válido')

