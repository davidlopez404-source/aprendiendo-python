#Clasificador de evaluaciones

def computegrade(puntaje):
    if puntaje < 0 or puntaje > 1:
        nota = 'Bad score'
    elif puntaje < 0.6:
        nota = 'F'
    elif puntaje < 0.7:
        nota = 'D'
    elif puntaje < 0.8:
        nota = 'C'
    elif puntaje < 0.9:
        nota = 'B'
    else:
        nota = 'A'
    return nota
try:
    evaluacion = float(input('Enter score: '))
    calificacion = computegrade(evaluacion)
    print(calificacion)
except:
    print('Bad score')
