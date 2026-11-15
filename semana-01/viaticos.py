nombre_consultor = input('Nombre del consultor: ')
dias_viaje = int(input('¿Cuántos días dura el viaje? '))
valor_viaticos_dia = float(input('¿Cuánto vale un dia de viaticos? ')) #valor en usd
total_viaticos = dias_viaje*valor_viaticos_dia #valor en usd
print('El consultor', nombre_consultor, 'gastó en viáticos',total_viaticos, 'dólares')
