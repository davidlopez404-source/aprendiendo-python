# Clasifica una propuesta de consultoría según su presupuesto
texto = input("Presupuesto del cliente (millones): ")

try:
    presupuesto = float(texto)
    if presupuesto >= 100:
        print("Proyecto grande: asignar equipo completo")
    elif presupuesto >= 30:
        print("Proyecto mediano: asignar dos consultores")
    elif presupuesto <=0:
        print('Presupuesto no válido: debe ser mayor que 0')
    else:
        print('Proyecto pequeño: asignar un consultor')
except:
    print("Dato no válido")

print("Clasificación terminada")
