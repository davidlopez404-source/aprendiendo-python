#Clasificación de proveedores

def clasificar_proveedor(calidad,puntualidad,precio):
    puntaje = (calidad * 5  + puntualidad * 3 + precio * 2)/10
    if calidad < 0 or calidad > 10 or puntualidad < 0 or puntualidad > 10 or precio <0 or precio > 10:
        tipo_proveedor = 'Datos no válidos'
    elif puntaje >= 8:
        tipo_proveedor = 'Proveedor A'
    elif 6 <= puntaje:
        tipo_proveedor = 'Proveedor B'
    else:
        tipo_proveedor = 'Proveedor C'
    return tipo_proveedor

try:
    nc = float(input('Nota de calidad: '))
    np = float(input('Nota de puntualidad: '))
    n_precio = float(input('Nota de precio: '))
    categoria = clasificar_proveedor(nc,np,n_precio)
    print('Categoría:',categoria)
except:
    print('Error: ingrese solo números')
