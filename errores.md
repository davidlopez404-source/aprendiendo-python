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
