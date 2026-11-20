#Cálculo de pago para el trabajador (1,5 veces la tarifa por cada hora por encima de 40)
horas_trabajadas = input('Cuántas horas trabajó? ')
tarifa_hora = input('¿Cuánto vale la hora trabajada (USD)?: ')
try:
    horas = float(horas_trabajadas)
    tarifa = float(tarifa_hora)
    if horas <0:
        print('Dato fuera de rango')
    elif tarifa <0:
        print('Dato fuera de rango')
    elif horas >40:
        print('El pago es de',40*tarifa+(horas-40)*1.5*tarifa,'dólares')
    else:
        print('El pago es de',horas*tarifa,'dólares')
except:
    print('Dato no válido')
print('Cálculo terminado')


    
