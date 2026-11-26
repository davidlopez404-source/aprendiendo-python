#Calculadora de pago con def
def computepay(horas, tarifa):
    if 0< horas <=40 and tarifa > 0:
        pago = horas*tarifa
    elif horas > 40 and tarifa > 0:
        pago = 40*tarifa + (horas-40)*1.5*tarifa
    else:
        pago = 'Valor no válido'
    return pago

try:
    horas_trabajadas = float(input('Enter Hours: '))
    tarifa_pagada = float(input('Enter Rate: '))
    pay = computepay(horas_trabajadas,tarifa_pagada)
    print('Pay:',pay)
except:
    print('Error, please enter numeric input')
