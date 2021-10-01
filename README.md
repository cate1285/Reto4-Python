# Reto4-Python
Totalizando pagos 
En el área financiera de una empresa, guardan usualmente la información de los pagos realizados cada mes del año a un contratista, teniendo en cuenta que este puede trabajar solo algunos meses del año. Ocasionalmente, requieren totalizar los pagos realizados al contratista para algunos meses en particular, sin que el funcionario conozca los meses en los cuales le hicieron pagos.

 

Construir un programa que calcule el valor pagado al contratista, para los meses fijados por el funcionario del área financiera de la empresa. Entonces, debe leer la información almacenada, la cual está en formato JSON (un diccionario, con los meses y el valor pagado en cada uno), y la lista de meses de la cual el usuario del área financiera se encuentra interesado en totalizar (cadena de texto, compuesto por los meses separados por un espacio). La salida del programa debe ser el valor pagado, así como la lista de meses. Como el funcionario no sabe que meses trabajó el contratista, podría ocurrir que no se encuentre el registro de pago para algún (os) meses.

 

Entradas
 

-       Línea 1 – Meses pagados por la empresa al contratista en formato JSON

 

{"septiembre": 2840618, "marzo": 2565389, "julio": 1061800, "enero": 1619096, "noviembre": 1027358, "agosto": 2551810}

 

-       Línea 2 – Lista de meses de interés por parte del funcionario del área financiera

 

enero agosto mayo junio abril septiembre

 

Salidas
 

-       Línea 1 – El valor total pagado al contratista en los meses de interés

 

7011524

 

-       Línea 2 - lista de meses laborados por el contratista de acuerdo con la lista de meses interés del funcionario del área y encontrados en el JSON de pagos realizados.

 

enero agosto septiembre

 

Otros Ejemplos
 

Entrada

Salida

{"julio": 1453784, "diciembre": 2407679, "mayo": 1359464, "septiembre": 2961462, "junio": 1471872}

 

mayo julio enero abril marzo diciembre

5220927

mayo julio diciembre

{"noviembre": 2295793, "junio": 1878245, "diciembre": 2051848, "octubre": 2068259, "abril": 2489773}

 

diciembre enero abril marzo septiembre octubre

6609880

diciembre abril octubre

{"marzo": 2616229, "diciembre": 1458215, "febrero": 1490501, "enero": 1859581, "mayo": 2011358}

 

febrero noviembre septiembre diciembre marzo enero

7424526

febrero diciembre marzo enero

 

 
