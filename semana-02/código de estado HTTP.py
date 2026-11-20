try:
    codigo = int(input('¿Cuál es el código? '))
    if 200 <= codigo <= 299:
        print('Éxito')
    elif 300 <= codigo <= 399:
        print('Redirección')
    elif 400 <= codigo <= 499:
        print('Error del cliente')
    elif 500 <= codigo <= 599:
        print('Error del servidor')
    else:
        print('Código inexistente')
except:
    print('Dato no válido')
    
