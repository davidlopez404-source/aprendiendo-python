#calificacion examen
try:
    calificacion = float(input('nota del examen (0-1): '))
    if 0 <= calificacion < 0.6:
        print('La calificación es F')
    elif calificacion < 0.7:
        print('La calificación es D')
    elif calificacion < 0.8:
        print('La calificación es C')
    elif calificacion < 0.9:
        print('La calificación es B')
    elif calificacion <= 1:
        print('La calificación es A')
    else:
        print('Calificación inválida')
except:
    print('Error, Escribe un número')
