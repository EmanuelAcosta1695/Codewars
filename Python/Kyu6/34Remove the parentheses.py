def remove_parentheses(s):
    import re
    while re.search(r'\([^()]*\)', s):
        s = re.sub(r'\([^()]*\)', '', s)
    return s

"""
re.sub: Es una función del módulo re de Python que reemplaza todas las ocurrencias de una expresión regular en una cadena de texto por otro texto.

r: Es un prefijo que indica que la cadena es una cadena "raw" o "cruda", lo que significa que los caracteres escapados en la cadena (como \n para una nueva línea) no se interpretan como caracteres especiales.

\(: Es una secuencia de escape que representa el carácter "(".

[^)]*: Es una clase de caracteres negados que busca cualquier carácter que no sea el carácter ")". El "*" indica que puede haber 0 o más ocurrencias de cualquier carácter que no sea ")".

\): Es una secuencia de escape que representa el carácter ")".



En programación, una secuencia de escape es una combinación de caracteres que se utiliza
para representar un carácter especial o no imprimible en un texto.

Estas secuencias comienzan con un carácter de escape (como ) seguido de uno o varios caracteres
que especifican el carácter especial. Por ejemplo, \n se utiliza para representar un salto de
línea, \t para una tabulación horizontal, \r para un retorno de carro, entre otros.

Las secuencias de escape también se utilizan para representar caracteres que no son visibles en
el texto, como el espacio en blanco o el tabulador vertical. En general, las secuencias de escape
se utilizan para facilitar la lectura y la escritura de código que involucra caracteres especiales
o no imprimibles.



r : indica que es una cadena de texto en formato "raw" o crudo, lo que significa que los caracteres
especiales dentro de la cadena, como \, no serán interpretados por Python.

\( : indica que el patrón de búsqueda comienza con un paréntesis izquierdo "(".

[^()]* : es una clase de caracteres negativos que coincide con cualquier carácter que no sea paréntesis
izquierdo "(" ni paréntesis derecho ")" , y el cuantificador * indica que debe haber cero o más de estos
caracteres.

\) : indica que el patrón de búsqueda termina con un paréntesis derecho ")".

En resumen, este patrón de búsqueda encuentra cualquier cadena de texto que tenga un paréntesis izquierdo
"(" seguido de cualquier cantidad de caracteres que no sean paréntesis izquierdo o derecho, y luego finaliza
con un paréntesis derecho ")".

Cuando se usa en conjunto con la función re.sub() en Python, este patrón de búsqueda se utiliza para reemplazar
cualquier ocurrencia de una cadena que se ajuste al patrón con una cadena vacía.
"""
