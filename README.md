Encriptador XOR en Python

Este proyecto implementa un sencillo sistema de encriptación y desencriptación basado en la operación lógica XOR, utilizando una clave generada aleatoriamente compuesta por bits (0 y 1).

La particularidad de este método es que aplicar la misma clave dos veces devuelve el texto original, lo que hace que el mismo algoritmo sirva tanto para encriptar como para desencriptar.

Cómo funciona

El usuario ingresa una palabra o texto a encriptar.

El programa genera automáticamente una clave binaria aleatoria (de 0s y 1s) del mismo largo que la palabra.

Se aplica la operación XOR (^) entre el código ASCII de cada carácter y el bit correspondiente de la clave.

El resultado es una cadena encriptada.

Si se vuelve a aplicar el mismo proceso con la misma clave, se obtiene el texto original (desencriptado)

Ejemplo de uso

Entrada:

Ingrese una palabra a encriptar: hola


Salida (puede variar por la clave aleatoria):

iglb
hola


La primera línea corresponde al texto encriptado.

La segunda línea es el texto desencriptado, que coincide con el original.

Notas importantes

Este script es solo una demostración educativa del principio XOR.

No debe usarse para seguridad real, ya que la clave generada es demasiado simple y predecible.

Puedes modificar el generador de clave o usar claves más largas o complejas para mejorar la seguridad.

Concepto clave: XOR

El operador XOR (^) tiene la propiedad:

A ^ B ^ B = A


Esto significa que aplicar la misma clave dos veces sobre el mismo texto revierte el proceso, permitiendo desencriptar sin usar una función distinta.
