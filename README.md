# 🏢 Buscador de Alquileres en CABA 🏡
![](Imagenes/CABA-002.jpg)
## Que hace el programa?
El programa analiza las propiedades disponibles en el archivo 'propiedades_CABA.csv'. 
Tambien puede realizar busquedas en cualquier otra ciudad del pais si descarga un archivo a travez del link [http://inove.pythonanywhere.com/alquileres/buscar?ubicacion=Mendoza] y reemplazar en el codigo del programa el archivo 'propiedades_CABA.csv' por el que descargo a travez del link y analizar las propiedades en otras ciudades. La librería genera un reporte de alquileres de MERCADO LIBRE en una determinada ubicacion. Para poder descargar el archivo "csv" de la zona o ciudad deseada debe editar la ubicación del link y colocar en ubicación donde desean que la librería realice la búsqueda y genere el "csv".

![](Imagenes/MercadoLibre.jpg)
## Como funciona el programa?
1) Debe descargar el repositorio desde esta pagina.
2) Debe entrar a la carpeta "Consola".
3) Debe abrir el archivo "main". 
4) Debe correr el programa en ese archivo. 
## Entrada del sistema.
El programa solicita al usuario el ingreso de los filtros que desee aplicar, tambien tiene la opcion de no ingresar ningun filtro si asi lo desea. Las propiedades de pueden filtrar por: 

1) Precio: Pesos, Dolares.   
2) Ambientes.
3) Superficie.
4) Tipo de propiedad: Departamento, Casa.

A partir de las freferencias del usuario, el algoritmo seleccionara las propiedades que cumplan con las caracteristicas deseadas y las grabara en un archivo 'busqueda.csv'.
## Salida del sistema. 
A partir del archivo 'busqueda.csv' se mostraran en pantalla:

1) La cantidad de propiedades tasadas en Pesos y en Dolares que cumplan con las caracteristicas deseadas.
2) El precio de la propiedad mas costosa, la mas barata y el precio promedio de los resultados.
3) La cantidad de ambientes de la propiedad mas costosa y de la mas barata.
4) La cantidad de propiedades en el archivo 'busqueda.csv'.
5) Las propiedades disponibles en el archivo 'busqueda.csv' como resultado de la busqueda del usuario. (ACLARACION IMPORTANTE!!! Tambien habra una opcion para visualizar las propiedades ordenadas segun su precio: de mayor a menor y vicevesa).

### AUTOR: Franco Baltasar Massi.
### Proyecto Final para el curso Python Inicial.
### Inove Coding School.
