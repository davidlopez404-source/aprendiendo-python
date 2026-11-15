min_taller_inn = int(input('¿Cuántos minutos duró el taller? '))
horas_completas = min_taller_inn//60
minutos_sobrantes = min_taller_inn%60
print('Se dictaron',horas_completas,'horas completas de taller')
print('Sobraron',minutos_sobrantes,'minutos de taller')
