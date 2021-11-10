#IMPORTACIONES
from other_functions import validar_ingreso, validar_numero, leer

#CONSTANTES
(NUMERO, FECHA, LATITUD, LONGITUD,
 URL, TITULO, TIPO_DE_PROPIEDAD, 
 PRECIO, MONEDA, SUPERFICIE, AMBIENTES) = (0,1,2,3,4,5,6,7,8,9,10) 
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


def filtros_a_aplicar(filtros_deseados):
    
    
    desea_ambientes =  validar_ingreso(input("Desea filtrar la busqueda por cantidad de ambientes de la propiedad? (Ingrese S/N): ").upper())
    
    desea_superficie =  validar_ingreso(input("Desea filtrar la busqueda por la superficie de la propiedad? (Ingrese S/N): ").upper())
        
    desea_divisa =  validar_ingreso(input("Desea filtrar la busqueda por divisa en la que se tasa de la propiedad? (Ingrese S/N): ").upper())
        
    desea_precio =  validar_ingreso(input("Desea filtrar la busqueda por el precio de la propiedad? (Ingrese S/N): ").upper())
        
    desea_t_propiedad =  validar_ingreso(input("Desea filtrar la busqueda por el tipo de propiedad? (Ingrese S/N): ").upper())
    
    
    if desea_ambientes:
        filtros_deseados += [AMBIENTES]
    if desea_superficie:
        filtros_deseados += [SUPERFICIE]
    if desea_divisa:
        filtros_deseados += [MONEDA]
    if desea_precio:
        filtros_deseados += [PRECIO]
    if desea_t_propiedad:
        filtros_deseados += [TIPO_DE_PROPIEDAD]

    
    return filtros_deseados


def ambientes(propiedad):



def superficie(propiedad):


    min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))

    max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))

    
    while min_superficie_deseada > max_superficie_deseada:

         print("LA SUPERFICIE MINIMA DEBE SER IGUAL O MAYOR A LA SUPERFICIE MAXIMA DESEADA")

         min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))
         
         max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))

   

    if propiedad[SUPERFICIE] >= min_superficie_deseada and propiedad[SUPERFICIE] <= max_superficie_deseada:

        propiedad += [SUPERFICIE]

    return propiedad

def divisa(propiedad):

def precio(propiedad):

def tipo_propiedad(propiedad):



def aplicar_filtros(propiedades, busqueda, filtros_deseados):

    propiedad = leer(propiedades)

    propiedad = leer(propiedades)

    NUMERO_DE_FILTROS = len(filtros_deseados)


    while propiedad[NUMERO]:


        if NUMERO_DE_FILTROS > 0:
            
            if AMBIENTES in filtros_deseados:
                 
                 propiedad = ambientes(propiedad)

            if SUPERFICIE in filtros_deseados:
                
                propiedad = superficie(propiedad)
                
            if MONEDA in filtros_deseados:
                
                propiedad = divisa(propiedad)
                
            if PRECIO in filtros_deseados:
                
                propiedad = precio(propiedad)
                
            if TIPO_DE_PROPIEDAD in filtros_deseados:
                
                propiedad = tipo_propiedad(propiedad)


        if propiedad[11: 11 + NUMERO_DE_FILTROS] == filtros_deseados:

            #CORREGIR!!!!!!
            # busqueda.write(propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[MONEDA] + "," + propiedad[PRECIO] + "," + propiedad[AMBIENTES] + "," + propiedad[SUPERFICIE] + "," + propiedad[URL] + "," + propiedad[LATITUD] +"," + propiedad[LONGITUD] +"\n")

            propiedad = leer(propiedades)

        else:
            propiedad = leer(propiedades)



def analizar_datos(propiedades, busqueda):

    print("GRACIAS POR ELEGIRNOS.")

    print("HAY", contar_propiedades(propiedades), " PROPIEDADES DISPONIBLES, PUEDE VERLAS TODAS O TAMBIEN PUEDE FLITRAR SU BUSQUEDA POR:  \n1)'TIPO DE PROPIEDAD\n2)MONEDA\n3)PRECIO\n4)SUPERFICIE\n5)AMBIENTES")

    desea_filtros = validar_ingreso(input("Desea realizar filtros en su busqueda? (Ingrese S/N").upper())

    filtros_deseados = []

    if not desea_filtros:

        propiedad = leer(propiedades)

        propiedad = leer(propiedades)

        while propiedad[NUMERO]:

            print("\n" + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Ubicacion----  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL])

            propiedad = leer(propiedades)
    else:

        filtros_deseados = filtros_a_aplicar(filtros_deseados)

        aplicar_filtros(propiedades, busqueda, filtros_deseados)



def mostrar_resultados(resultados_de_busqueda):

    print("HAY", contar_propiedades(resultados_de_busqueda), " PROPIEDADES A SUS PREFERENCIAS.")

    propiedad = leer(resultados_de_busqueda)

    while propiedad[NUMERO]:

        #CORREGIR!!!!!!!!
        # print("\n" + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Ubicacion----  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL])

        propiedad = leer(resultados_de_busqueda)






#lista = [x.upper() for x in ["numero", "fecha", "latitud" , "longitud", "url", "titulo", "tipo de propiedad", "precio" ,"moneda" , "SUPERFICIE", "ambientes"]]
#print(lista)

#if propiedad[SUPERFICIE] >= min_superficie_deseada and propiedad[SUPERFICIE] <= max_superficie_deseada:
            
#busqueda.write(propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[MONEDA] + "," + propiedad[PRECIO] + "," + propiedad[AMBIENTES] + "," + propiedad[SUPERFICIE] + "," + propiedad[URL] + "," + propiedad[LATITUD] +"," + propiedad[LONGITUD] +"\n")