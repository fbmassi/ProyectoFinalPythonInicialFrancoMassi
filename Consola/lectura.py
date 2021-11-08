#IMPORTACIONES
from other_functions import validar_ingreso
from other_functions import validar_numero
from other_functions import leer

#CONSTANTES
(NUMERO, FECHA, LATITUD, LONGITUD, URL, TITULO, TIPO_DE_PROPIEDAD, PRECIO, MONEDA, SUPERFICIE, AMBIENTES) = (0,1,2,3,4,5,6,7,8,9,10) 
(PRINCIPIO, FIN) = (0,2) 

#FUNCIONES
def contar_propiedades(propiedades):

    """
    Esta funcion toma como parametro el archivo de las 
    propiedades en alquiler. Lo recorre contando la 
    cantidad que hay en total.
    Devuelve el numero de propiedades en alquiler. 
    Al final del conteo se posiciona al principio del
    archivo para ser leido otra vez. 
    """

    propiedad = leer(propiedades)

    contador = 0

    while propiedad[NUMERO]:

        contador += 1

        propiedad = leer(propiedades)

    propiedades.seek(PRINCIPIO)
    
    return contador


def superficie(propiedades, archivo_filtrado):

    propiedad = leer(propiedades)

    min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))

    max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))

    
    while min_superficie_deseada > max_superficie_deseada:

         print("LA SUPERFICIE MINIMA DEBE SER IGUAL O MAYOR A LA SUPERFICIE MAXIMA DESEADA")

         min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))
         
         max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))

   

    while propiedad[NUMERO]:


        if propiedad[SUPERFICIE] >= min_superficie_deseada and propiedad[SUPERFICIE] <= max_superficie_deseada:
            
            archivo_filtrado.write(propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[MONEDA] + "," + propiedad[PRECIO] + "," + propiedad[AMBIENTES] + "," + propiedad[SUPERFICIE] + "," + propiedad[URL] + "\n")


#def rango_de_precios(propiedades, resultados_de_busqueda):

#    """
#    Esta funcion analiza si un elemento del archivo 
#    del que se extrae la informacion,
#    cumple con requisitos ingresados por el usuario.
#    """

#    propiedad = leer(propiedades)

#"""

#"""

def extraer_datos(propiedades, resultados_de_busqueda):

    propiedad = leer(propiedades)

    print("GRACIAS POR ELEGIRNOS.")

    print("HAY", contar_propiedades(propiedades), " PROPIEDADES DISPONIBLES, PUEDE VERLAS TODAS O TAMBIEN PUEDE FLITRAR SU BUSQUEDA POR:  \n1)'TIPO DE PROPIEDAD\n2)MONEDA\n3)PRECIO\n4)SUPERFICIE\n5)AMBIENTES")

    desea_filtros = validar_ingreso(input("Desea realizar filtros en su busqueda? (Ingrese S/N").upper())

    if not desea_filtros:

        propiedad = leer(propiedades)

        while propiedad[NUMERO]:

            print("\n" + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Ubicacion----  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL])

            propiedad = leer(propiedades)
    else:
        desea_superficie =  validar_ingreso(input("Desea filtrar la busqueda por la suoerficie de la propiedad? (Ingrese S/N): ").upper())




#lista = [x.upper() for x in ["numero", "fecha", "latitud" , "longitud", "url", "titulo", "tipo de propiedad", "precio" ,"moneda" , "SUPERFICIE", "ambientes"]]
#print(lista)

