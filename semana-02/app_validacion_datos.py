#app necesita revisar los datos de una persona antes de crearle la cuenta
try:
    edad = int(input('Edad de la persona: '))
    terminos_cond = input('¿Acepta los términos? (si/no) ') ==  'si'
    if edad < 0 or edad > 120:
        print('Edad fuera de rango')
    elif not terminos_cond:
        print('Debe aceptar los términos')
    elif edad < 18:
        print('Registro pendiente: requiere permiso de un adulto')
    else:
        print('Registro exitoso')
except:
    print('Dato no válido')
