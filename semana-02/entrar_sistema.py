# Control de acceso
try:
    intentos = int(input('Intentos fallidos: '))
    bloqueado = intentos >= 3          # True o False
    es_admin = input('¿Es admin? (si/no): ') == 'si'
    if not bloqueado and es_admin:
        print('Acceso total')
    elif not bloqueado:
        print('Acceso limitado')
    else:
        print('Acceso denegado')
except:
    print('Dato no válido')
