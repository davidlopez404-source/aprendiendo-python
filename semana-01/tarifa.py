cliente = input('¿Cuál es el nombre del cliente? ')
horas_proy = int(input('¿Cuántas horas se dedican al proyecto? '))
tarifa_hora = float(input('¿Cuál es la tarifa por hora? ')) #en usd
precio_total = horas_proy*tarifa_hora
print(cliente)
print(precio_total)
