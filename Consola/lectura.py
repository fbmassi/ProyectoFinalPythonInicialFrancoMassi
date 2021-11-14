#IMPORTACIONES
from otras_funciones import validar_ingreso, validar_numero, leer, validar_tipo_propiedad

#CONSTANTES
NUMERO, FECHA, LATITUD, LONGITUD, URL, TITULO, TIPO_DE_PROPIEDAD, PRECIO, MONEDA, SUPERFICIE, AMBIENTES = 0,1,2,3,4,5,6,7,8,9,10
PRINCIPIO, FIN = 0,2 
PESOS, DOLARES = 0,1
DESEA_DIVISA, MINIMO_DIVISA, MAXIMO_DIVISA = 0,1,2
MINIMO, MAXIMO = 0,1


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
    
    propiedad = leer(propiedades)
    
    contador = 0

    while propiedad[NUMERO]:
            
        contador += 1
            
        propiedad = leer(propiedades)

    propiedades.seek(PRINCIPIO)
    
    return contador



def precio():

    desea_pesos = validar_ingreso(input("Desea que se muestren propiedades tasadas en pesos? (Ingrese S/N): ").upper())

    pesos = [desea_pesos, 0, 0]
        
    desea_dolares = validar_ingreso(input("Desea que se muestren propiedades tasadas en dolares? (Ingrese S/N): ").upper())

    dolares = [desea_dolares, 0, 0]
    
    if desea_pesos:
            
        min_precio_pesos = validar_numero(input("Ingrese el minimo monto que desea de un alquiler en pesos: "))
            
        max_precio_pesos = validar_numero(input("Ingrese el maximo monto que desea de un alquiler en pesos: "))

        while min_precio_pesos > max_precio_pesos:
                
            print("EL PRECIO MINIMO DEBE SER MAYOR AL PRECIO MAXIMO DEL ALQUILER.")
                
            min_precio_pesos = validar_numero(input("Ingrese el minimo monto que desea de un alquiler en pesos: "))
                
            max_precio_pesos = validar_numero(input("Ingrese el maximo monto que desea de un alquiler en pesos: "))
    
        pesos[MINIMO_DIVISA] = min_precio_pesos

        pesos[MAXIMO_DIVISA] = max_precio_pesos

    if desea_dolares:

        min_precio_dolares = validar_numero(input("Ingrese el minimo monto que desea de un alquiler en dolares: "))
            
        max_precio_dolares = validar_numero(input("Ingrese el maximo monto que desea de un alquiler en dolares: "))
            
        while min_precio_dolares > max_precio_dolares:
            
            print("EL PRECIO MINIMO DEL ALQUILER DEBE SER IGUAL O MENOR AL MAXIMO.")
                
            min_precio_dolares = validar_numero(input("Ingrese el minimo monto que desea de un alquiler en dolares: "))
                
            max_precio_dolares = validar_numero(input("Ingrese el maximo monto que desea de un alquiler en dolares: "))

        dolares[MINIMO_DIVISA] = min_precio_dolares

        dolares[MAXIMO_DIVISA] = max_precio_dolares
        
    precios = [pesos, dolares]

    return precios


def ambientes():

    min_ambientes_deseados = validar_numero(input("Ingrese la minima cantidad de ambientes que desea para su propiedad: "))

    max_ambientes_deseados = validar_numero(input("Ingrese la maxima cantidad de ambientes que desea para su propiedad: "))

    while min_ambientes_deseados > max_ambientes_deseados:

         print("LA CANDIDAD MINIMA DE AMBIENTES DEBE SER IGUAL O MENOR A LA CANTIDAD MAXIMA DESEADA.")

         min_ambientes_deseados = validar_numero(input("Ingrese la minima cantidad de ambientes que desea para su propiedad: "))
         
         max_ambientes_deseados = validar_numero(input("Ingrese la maxima cantidad de ambientes que desea para su propiedad: "))
    
    cant_ambientes = [min_ambientes_deseados, max_ambientes_deseados]
    
    return cant_ambientes 


def superficie():

    min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))

    max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))

    while min_superficie_deseada > max_superficie_deseada:

         print("LA SUPERFICIE MINIMA DESEADA DEBE SER IGUAL O MENOR A LA MAXIMA.")

         min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))
         
         max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))
    
    cant_superficie = [min_superficie_deseada, max_superficie_deseada]

    return cant_superficie


def filtros_a_aplicar(filtros_deseados):
    
    desea_precio =  validar_ingreso(input("Desea filtrar la busqueda por el precio de la propiedad? (Ingrese S/N): ").upper())

    desea_ambientes =  validar_ingreso(input("Desea filtrar la busqueda por cantidad de ambientes de la propiedad? (Ingrese S/N): ").upper())
    
    desea_superficie =  validar_ingreso(input("Desea filtrar la busqueda por la superficie de la propiedad? (Ingrese S/N): ").upper())
        
    desea_t_propiedad =  validar_ingreso(input("Desea filtrar la busqueda por el tipo de propiedad? (Ingrese S/N): ").upper())
    
    if desea_precio:

        filtros_deseados[PRECIO] = precio()

    if desea_ambientes:

        filtros_deseados[AMBIENTES] = ambientes()

    if desea_superficie:

        filtros_deseados[SUPERFICIE] = superficie()

    if desea_t_propiedad:

        propiedad_deseada = validar_tipo_propiedad(input("Ingrese el tipo de propiedad que se encuentra buscando: (Ingrese 'Casa' o 'Departamento' sin puntos ni espacios): ").capitalize())

        filtros_deseados[TIPO_DE_PROPIEDAD] = propiedad_deseada

    return filtros_deseados


def filtrar_precio(propiedad, filtros_deseados):
    
    try:
        if (filtros_deseados[PRECIO][PESOS][DESEA_DIVISA]) and (propiedad[MONEDA] == "ARS") and (float(propiedad[PRECIO]) >= filtros_deseados[PRECIO][PESOS][MINIMO_DIVISA]) and (float(propiedad[PRECIO]) <= filtros_deseados[PRECIO][PESOS][MAXIMO_DIVISA]):
            
            propiedad += [PRECIO]
            
        elif filtros_deseados[PRECIO][DOLARES][DESEA_DIVISA] and propiedad[MONEDA] == "USD" and (float(propiedad[PRECIO]) >= filtros_deseados[PRECIO][DOLARES][MINIMO_DIVISA]) and (float(propiedad[PRECIO]) <= filtros_deseados[PRECIO][DOLARES][MAXIMO_DIVISA]):
            
            propiedad += [PRECIO]
            
    except:
        
        propiedad = propiedad

    return propiedad


def filtrar_ambientes(propiedad, filtros_deseados):
    
    try:
        
        if (float(propiedad[AMBIENTES]) >= filtros_deseados[AMBIENTES][MINIMO]) and (float(propiedad[AMBIENTES]) <= filtros_deseados[AMBIENTES][MAXIMO]):
            
            propiedad += [AMBIENTES]
            
    except:
        
        propiedad = propiedad

    return propiedad


def filtrar_superficie(propiedad, filtros_deseados):

    try:
        if (float(propiedad[SUPERFICIE]) >= filtros_deseados[SUPERFICIE][MINIMO]) and (float(propiedad[SUPERFICIE]) <= filtros_deseados[SUPERFICIE][MAXIMO]):
            
            propiedad += [SUPERFICIE]
    except:
        
        propiedad = propiedad

    return propiedad


def filtrar_tipo_prop(propiedad, filtros_deseados):
    
    try:
        if propiedad[TIPO_DE_PROPIEDAD] == filtros_deseados[TIPO_DE_PROPIEDAD]:
            
            propiedad += [TIPO_DE_PROPIEDAD]
            
    except:
        
        propiedad = propiedad

    return propiedad


def aplicar_filtros(propiedades, busqueda, filtros_deseados):

    propiedad = leer(propiedades)

    propiedad = leer(propiedades)

    NUMERO_DE_FILTROS = len(filtros_deseados)

    while propiedad[NUMERO]:

        if NUMERO_DE_FILTROS > 0:

            if PRECIO in filtros_deseados:
                
                propiedad = filtrar_precio(propiedad, filtros_deseados)
            
            if AMBIENTES in filtros_deseados:
                 
                 propiedad = filtrar_ambientes(propiedad, filtros_deseados)

            if SUPERFICIE in filtros_deseados:
                
                propiedad = filtrar_superficie(propiedad, filtros_deseados)
                
            if TIPO_DE_PROPIEDAD in filtros_deseados:
                
                propiedad = filtrar_tipo_prop(propiedad, filtros_deseados)

        lista_filtros_deseados = [x for x in filtros_deseados]

        if propiedad[11: 11 + NUMERO_DE_FILTROS] == lista_filtros_deseados:

            busqueda.write(propiedad[NUMERO] + "," + propiedad[FECHA] + "," + propiedad[LATITUD] + "," + propiedad[LONGITUD] + "," + propiedad[URL] + "," + propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[PRECIO] + "," + propiedad[MONEDA] + "," + propiedad[SUPERFICIE] + "," + propiedad[AMBIENTES] + "\n")

            propiedad = leer(propiedades)

        else:
            propiedad = leer(propiedades)



def analizar_datos(propiedades, busqueda):

    print("GRACIAS POR ELEGIRNOS.")

    print("HAY", contar_propiedades(propiedades), " PROPIEDADES DISPONIBLES, PUEDE VERLAS TODAS O TAMBIEN PUEDE FLITRAR SU BUSQUEDA POR:  \n1)TIPO DE PROPIEDAD\n2)PRECIO\n3)SUPERFICIE\n4)AMBIENTES")

    desea_filtros = validar_ingreso(input("Desea realizar filtros en su busqueda? (Ingrese S/N): ").upper())

    filtros_deseados = {}
    
    busqueda.write("numero" + "," + "fecha" + "," + "latitud" + "," + "longitud" + "," + "url" + "," + "titulo" + "," + "tipo de propiedad" + "," + "precio" + "," + "moneda" + "," + "superficie" + "," + "ambientes" + "\n")

    if not desea_filtros:

        propiedad = leer(propiedades)

        propiedad = leer(propiedades)

        while propiedad[NUMERO]:

            busqueda.write(propiedad[NUMERO] + "," + propiedad[FECHA] + "," + propiedad[LATITUD] + "," + propiedad[LONGITUD] + "," + propiedad[URL] + "," + propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[PRECIO] + "," + propiedad[MONEDA] + "," + propiedad[SUPERFICIE] + "," + propiedad[AMBIENTES] + "\n")

            propiedad = leer(propiedades)
    else:

        filtros_deseados = filtros_a_aplicar(filtros_deseados)

        aplicar_filtros(propiedades, busqueda, filtros_deseados)



def mostrar_resultados(resultados_de_busqueda):
    
    cant_resultados = contar_propiedades(resultados_de_busqueda)

    print("\n\nHAY", cant_resultados, " PROPIEDADES AJUSTADAS A SUS PREFERENCIAS.")

    propiedad = leer(resultados_de_busqueda)

    if (cant_resultados > 1) and validar_ingreso(input("Desea que los resultados se muestren ordenados a partir del precio? (Ingrese S/N): ").upper()) :

        lista_a_ordenar = []
        
        propiedad = leer(resultados_de_busqueda)

        while propiedad[NUMERO]:
            
            lista_a_ordenar += [(propiedad)]
            
            propiedad = leer(resultados_de_busqueda)

        orden = validar_ingreso(input("Desea que los resultados se ordenen de menor a mayor segun el precio o al revez? (Ingrese S/N): ").upper())

        if orden:
            
            lista_ordenada = sorted(lista_a_ordenar, key = lambda inmueble:inmueble[PRECIO])
            
            #print(lista_ordenada)
            
            for propiedad in lista_ordenada:

               print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL] + "\n" )
        
        else:
            
            lista_ordenada = sorted(lista_a_ordenar, reverse = True, key = lambda inmueble:inmueble[PRECIO])
            
            #print(lista_ordenada)
            
            for propiedad in lista_ordenada:

               print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL] + "\n")
    
    
    elif cant_resultados == 0:
        
        print("NO SE HAN ENCONTRADO RESULTADOS PARA TU BUSQUEDA.")
        
    elif cant_resultados == 1:
        
        propiedad = leer(resultados_de_busqueda)
            
        print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: " + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL])
            
    else:

        while propiedad[NUMERO]:
            
            propiedad = leer(resultados_de_busqueda)
            
            print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL])
            
            






#lista = [x.upper() for x in ["numero", "fecha", "latitud" , "longitud", "url", "titulo", "tipo de propiedad", "precio" ,"moneda" , "SUPERFICIE", "ambientes"]]
#print(lista)

#if propiedad[SUPERFICIE] >= min_superficie_deseada and propiedad[SUPERFICIE] <= max_superficie_deseada:
            
#busqueda.write(propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[MONEDA] + "," + propiedad[PRECIO] + "," + propiedad[AMBIENTES] + "," + propiedad[SUPERFICIE] + "," + propiedad[URL] + "," + propiedad[LATITUD] +"," + propiedad[LONGITUD] +"\n")