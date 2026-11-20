#cobro de un parqueadero
#el sistema de un parqueadero calcula cuánto cobrar según los minutos que estuvo el carro.

try:
    minutos_permanencia = int(input('minutos de permanencia: '))
    if minutos_permanencia <= 0:
        print('Tiempo no válido')
    elif minutos_permanencia <= 15:
        print('Gratis')
    elif minutos_permanencia > 1440:
        print('Tarifa plena: 40000')
    elif minutos_permanencia%60>0:
        print('Total a pagar:',3000*(minutos_permanencia//60)+2000,'pesos')
    else:
        print('Total a pagar:',3000*(minutos_permanencia//60),'pesos')
except:
    print('Dato no válido')
    
