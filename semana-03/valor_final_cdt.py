#Valor final de una inversión (CDT)

def calcular_valor_final(capital,tasa,años):
    if capital <= 0 or tasa < 0 or tasa > 100 or años < 1:
        valor_f = 'Datos no válidos'
    else:
        valor_f = capital * (1 + tasa /100)**años
    return valor_f

try:
    c = float(input('Capital: '))
    ta = float(input('Tasa anual: '))
    a = int(input('Años: '))
    vf = calcular_valor_final(c,ta,a)
    print('Valor final:',vf)
except:
    print('Error: ingrese solo números')
