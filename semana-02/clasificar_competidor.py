#Clasificacion de competidor
cuota_mercado = input('Cuál es la cuota de mercado del competidor (%)? ')
try:
    cuota = float(cuota_mercado)
    if cuota >100:
        print('Porcentaje fuera de rango')
    elif cuota <0:
        print('Porcentaje fuera de rango')
    elif cuota >=30:
        print('Competidor dominante')
    elif cuota >=10:
        print('Competidor relevante')
    else:
        print('Competidor marginal')
except:
    print('Dato no válido')
print('Clasificación de competidor terminada')

    
