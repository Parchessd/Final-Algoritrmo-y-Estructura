[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y1L1JQnh)
# Algoritmos y Estructuras de Datos. 

## FINAL - JULIO  - 30 / 07 / 2024 - 

<h2>(Completar) 
NOMBRE y APELLIDO:
</h2>



### Ejercicio 1: (1pt.) 

Generar un conjunto por comprensión que contenga los puntos <code>(x,y)</code>, en donde <code>x != y</code>. Cada punto es una tupla, comienzan en <code>0</code> hasta un numero dado <code>n</code>.

### Ejercicio 2: (2pt.) 

Escribir una clase <code>Caja</code> para representar cuánto dinero hay en una caja de un **negocio**, desglosado por tipo de billete/moneda (por ejemplo, en "el kiosco de la esquina" hay 5 billetes de 10 pesos, 7 monedas de 25 centavos y 4 monedas de 10 centavos).

Implementar métodos que permitan **comparar cajas** por la cantidad de dinero que hay en cada una, y además **ordenar** una lista de cajas de menor a mayor según la cantidad de dinero disponible.

<u><b>Importante:</b></u> 
- Deben definir cuales son los atributos y métodos esenciales de los objetos del tipo <code>Caja</code>
- Pueden agregar más atributos y métodos, si lo consideran necesario.  


### Ejercicio 3: (1pt.)

Sobrecargar los métodos <code>\_\_add\_\_</code> , <code>\_\_eq\_\_</code>, <code>\_\_sub\_\_</code> y <code>\_\_str\_\_</code> de la clase <code>Caja</code>. 


### Ejercicio 4: (1pt.)

Dada un lista de **Cajas** *(objetos del tipo <code>Caja</code>)* implementar esa lista usando la definición de <code>Lista Enlazada</code> que se encuentra en el archivo referente ejercicio). Se deben completar los métodos <code>\_\_init\_\_</code>, <code>\_\_len\_\_</code> y <code>is_empty</code>, además de proveer métodos que permitan **insertar** y **remover** cajas. Los métodos previamente definidos en el Ejercicio 2 para comparar/ordenar la lista de cajas, deben funcionar también con nueva lista definida en a base a la lista enlazada. 

<u><b>Importante:</b></u> 
- Pueden agregar más atributos y métodos, si lo consideran necesario.  

### Ejercicio 5: (1pt.)

Implementar un **Iterador** para la lista enlazada de cajas definida en el ejercicio anterior.


### Ejercicio 6: (1pt.)

Volver a implementar el método que nos permite ordenar la lista cajas (Ejercicio 2 y 4), utilizando un *algoritmo de ordenamiento recursivo*.   


### Ejercicio 7: (1pt.)

Escribir una función, que reciba como parámetros un archivo de texto de origen y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada en el archivo destino. En caso de no recibir un nombre para el archivo destino, el nombre del archivo debe ser <code>texto_cifrado.txt</code>.
El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo caracter. 


### Ejercicio 8: (2pt.)

Escribir una función <code>guardar_datos</code> que reciba un **diccionario** y un **nombre de archivo**, y guarde el contenido del diccionario en el archivo, con el formato <code>clave, valor</code>. Pueden usar un salto de línea para seprar los distintos pares *clave, valor*.

Escribir una función <code>cargar_datos</code> que reciba el **nombre de archivo**, cuyo contenido tiene el formato <code>clave, valor</code> y devuelva un **diccionario**. 
