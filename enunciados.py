introduccion = '''
                Mini TP1 - Representación de Datos
En este trabajo se pondrán en práctica los conceptos aprendidos sobre representación de
enteros, caracteres y números en punto flotante.

Evaluación

Esta actividad es individual, obligatoria y con autoevaluación. La fecha de entrega se encuentra
en el calendario, ese mismo día se publicará la solución para que pueda realizar la
autoevaluación.
Para acreditar esta actividad se solicita:

● Un informe en pdf del trabajo realizado punto por punto.

En caso de no realizar la entrega en el día previsto en el calendario se solicitará al alumno que
re-entregue los ejercicios más un ejercicio adicional a criterio de la comisión.
Fecha límite de entrega: ver calendario en moodle
Espacio de entrega: ver en moodle
Ayuda y consultas
Para realizar consultas se puede usar cualquiera de los canales habilitados: horas de consulta
en clase online, foro de consultas, mail, y otros canales que habilite la comisión. En particular,
alentamos las consultas en vivo en horario de cursada.
'''



enunciado_a = '''
Enunciado del Mini TP:

Lo que vemos en la siguiente grilla es una porción de memoria donde se encuentran los datos
de un programa después de la ejecución del mismo. Cada celda de la grilla es una posición de
memoria que almacena 1 byte.

En dicho programa se definió:

int valor1;
int valor2;
int valor3;
int dato1;
int dato2;
int producto
float coeficiente;
string mensaje;
'''

enunciado_b = '''
1) Sabiendo que cada int (entero) ocupa 16 bits, que el tipo de datos float respeta la norma
IEEE-754 para números de punto flotante de precisión simple y que el string usa la convención
de C (finaliza con 0), identificar las posiciones ocupadas por cada variable (marcar en la tabla
cada dato con un color diferente). Tener en cuenta que el tipo de datos de las variables
determina cuántos bytes ocupa. Las variables producto y coeficiente, deben ser completadas,
en producto se debe guardar el producto de dato1 y dato2. En coeficiente se debe almacenar
0.003
'''

enunciado_c = '''
2) Indicar cuál es el valor de cada una de las variables identificadas anteriormente y tener en
cuenta que la alineación de memoria del procesador es big endian. Expresar los valores
numéricos en el sistema decimal y aquellos que corresponden a letras del mensaje en letras
según la codificación ascii.
'''

enunciado_d = '''
3) Leer de memoria el valor almacenado en coeficiente y volver a convertir a decimal.
Explicar que pasa, ¿el número en decimal es correcto? Desarrollar una explicación y sacar una
conclusión.
'''

enunciado_e = '''
4) ¿Además de ascii cuál puede ser la codificación de caracteres utilizada?
'''


enunciados = {
    "introduccion": introduccion,
    "enunciado_a": enunciado_a,
    "enunciado_b": enunciado_b,
    "enunciado_c": enunciado_c,
    "enunciado_d": enunciado_d,
    "enunciado_e": enunciado_e
}


