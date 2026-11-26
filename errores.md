## Error 1
Mensaje: SyntaxError: multiple statements found while compiling a single statement
Causa: pegué varias líneas en la Shell (>>>), que acepta una instrucción a la vez
Cómo lo arreglé: escribí el programa en el editor (File > New File) y lo ejecuté con F5

## Error 2
Mensaje: SyntaxError: invalid character '¿' (U+00BF)
Causa: le quité las comillas al mensaje de input() pensando que así la respuesta sería un número; el '¿' quedó suelto fuera de un texto y Python no lo entiende
Cómo lo arreglé: dejé las comillas en el mensaje y envolví input() con int(): horas = int(input('¿Cuántas horas trabajaste? '))

## Error 3
Mensaje: NameError: name 'calififacion' is not defined
Causa: escribí mal el nombre de la variable; el except lo escondía y solo mostraba "Error"
Cómo lo arreglé: quité el try/except un momento para ver el error real y corregí el nombre

## Error 4
Mensaje: ValueError: could not convert string to float: 'perfect'
Causa: float() o int() reciben texto que no es número
Cómo lo arreglé: envolví el input en try/except y mostré un mensaje claro

## Error 5
Mensaje: TypeError: can only concatenate str (not "int") to str
Causa: intenté unir texto con un número usando + ('Ventas: ' + 500)
Cómo lo arreglé: separé con coma en el print: print('Ventas:', 500)

## Error 6
Mensaje: ZeroDivisionError: division by zero
Causa: dividí entre una variable que valía 0 (ventas / clientes con clientes = 0)
Cómo lo arreglé: puse primero la condición guardiana: clientes > 0 and ventas / clientes > 100

## Error 7
Mensaje: NameError: name 'punto_reorden' is not defined
Causa: llamé la función con el nombre de una variable interna (punto_reorden) en vez de su nombre real (revisar_inventario); el except amplio lo escondió y mostró "Error: ingrese solo números" aunque los datos eran números
Cómo lo arreglé: vi el error real y llamé la función por su nombre: revisar_inventario(...)

## Error 8
Mensaje: UnboundLocalError: cannot access local variable 'no_cajas' where it is not associated with a value
Causa: en calcular_despacho, la línea costo = no_cajas * costo_caja quedó fuera del if/elif/else, así que se ejecutaba siempre. Cuando los datos no eran válidos, solo corría el if, no_cajas nunca recibía valor y Python no podía usarla (además pisaba el 'Datos no válidos')
Cómo lo arreglé: moví la fórmula del costo dentro del elif y del else, donde no_cajas ya tiene valor; el return quedó afuera porque todas las ramas le dejan valor a costo

## Error 9
Mensaje: IndentationError: expected an indented block
Causa: (teoría cap. 3, sección 3.9) la línea después de un if, else o def quedó sin sangría. Python marca la línea siguiente, pero la causa está en la anterior
Cómo lo arreglé: le puse la sangría (4 espacios) a las líneas que van dentro del bloque

## Error 10
Mensaje: TypeError: función() missing 1 required positional argument
Causa: (teoría cap. 4) llamé una función sin pasarle el argumento que necesita, por ejemplo clasificar_cliente()
Cómo lo arreglé: llamé la función con todos sus argumentos: clasificar_cliente(facturacion_anual)

## Error 11
Mensaje: ValueError: math domain error
Causa: (predicción, ejercicio 8 de la semana 3) math.sqrt solo acepta números de 0 en adelante; con math.sqrt(-4) Python no da 2i, lanza este error. El except amplio lo escondería y mostraría "Error: ingrese solo números"
Cómo lo arreglé: validé primero en el if (dias_entrega < 1) para que la raíz solo se calcule con datos válidos
