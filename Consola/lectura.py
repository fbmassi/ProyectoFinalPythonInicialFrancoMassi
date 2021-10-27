#CONSTANTES
(0,1,2,3,4,5,6,7,8,9,10,11) = ['NUMERO', 'FECHA', 'LATITUD', 'LONGITUD', 'URL', 'TITULO', 'TIPO DE PROPIEDAD', 'PRECIO', 'MONEDA', 'SUPERFICIE', 'AMBIENTES']

def leer(archivo):

    """
    Esta funcion lee una linea del archivo.
    Devuelve una lista con el contenido de la linea que se leyo.
    En cada elemento se almacenan los valores separdos por las comas.
    """

    linea = archivo.readline()

    return linea.rstrip("\n").split(",") if linea else ["","","","","","","","","","",""]

def superficie():

    

def rango_de_precios(propiedades, resultados_de_busqueda):

    """
    Esta funcion analiza si un elemento del archivo 
    del que se extrae la informacion,
    cumple con requisitos ingresados por el usuario.
    """

    propiedad = leer(propiedades)




def extraer_datos(propiedades, resultados_de_busqueda):
    propiedad = leer(propiedades)
    print("GRACIAS POR ELEGIRNOS")
    filtros_deseados = input("HAY", contar_propiedadaes, " PROPIEDADES DISPONIBLES, SELECCIONE QUE CARACTERISTICAS ESTA BUSCANDO EN SU INMUEBLE: (Seleccione por el numero asignado) \n1)'TIPO DE PROPIEDAD\n2)MONEDA\n3)PRECIO\n4)SUPERFICIE\n5)AMBIENTES")

""" 
lista = [x.upper() for x in ["numero", "fecha", "latitud" , "longitud", "url", "titulo", "tipo de propiedad", "precio" ,"moneda" , "SUPERFICIE", "ambientes"]]
print(lista)
"""
