# Mi bitácora de errores
## Error 1
Mensaje: SyntaxError: multiple statements found while compiling a single statement
Causa: pegué varias líneas en la Shell (>>>), que acepta una instrucción a la vez
Cómo lo arreglé: escribí el programa en el editor (File > New File) y lo ejecuté con F5

## Error 2
Mensaje: SyntaxError: invalid character '¿' (U+00BF)
Causa: le quité las comillas al mensaje de input() pensando que así la respuesta sería un número; el '¿' quedó suelto fuera de un texto y Python no lo entiende
Cómo lo arreglé: dejé las comillas en el mensaje y envolví input() con int(): horas = int(input('¿Cuántas horas trabajaste? '))
