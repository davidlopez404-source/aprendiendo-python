#Clasificador de clientes por facturación

try:
    dias_mora = int(input('¿Cuántos días de mora tiene la factura? '))
    notificacion_cliente = input('¿El cliente fue notificado (si/no)? ') == 'si'
    if dias_mora ==0:
        print('Al día')
    elif dias_mora < 0:
        print('Los días de mora no pueden ser negativos')
    elif 1 <= dias_mora <= 30 and not notificacion_cliente:
        print('Enviar recordatorio')
    elif dias_mora <= 30 and notificacion_cliente:
        print('Esperar pago')
    else:
        print('Pasar a cobranza')
except:
    print('Dato no válido')
    
