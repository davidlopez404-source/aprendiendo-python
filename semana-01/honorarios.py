horas_trabajadas = float(input('¿Cuántas horas trabajó? '))
tarifa_hora = float(input('¿Cuál es la tarifa por hora? ')) #en dólares
subtotal = horas_trabajadas*tarifa_hora
tasa_iva = 0.19
cobro_iva = subtotal*tasa_iva
total_iva_incluido = subtotal+cobro_iva
print('El subtotal es',subtotal,'dólares')
print('El IVA es',cobro_iva, 'dólares')
print('El total es',total_iva_incluido,'dólares')
