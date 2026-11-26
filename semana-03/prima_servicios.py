#Prima de servicios

def calcular_prima(salario,auxilio,dias):
    if salario <= 0 or auxilio < 0 or dias < 1 or dias > 180:
        prima = 'Datos no válidos'
    else:
        prima = (salario + auxilio) * dias / 360
    return prima

try:
    salario_base = float(input('Salario mensual: '))
    auxilio_transporte = float(input('Auxilio de transporte: '))
    días_laborados = int(input('Días trabajados: '))
    prima_total = calcular_prima(salario_base,auxilio_transporte,días_laborados)
    print('Prima:',prima_total)
except:
    print('Error: ingrese solo números')
    
