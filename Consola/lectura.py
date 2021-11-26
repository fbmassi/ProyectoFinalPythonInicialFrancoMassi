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
    """
    Esta funcion solicita al usuario que
    ingrese en que divisa en la que le interesa
    pagar. Luego le pide al usuario que ingrese
    un monto minimo y uno maximo. Devuelve una
    lista de listas con la informacion acerca
    de que divisa escogio y los montos minimos
    y maximos de cada una. 
    """

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
    """
    Esta funcion solicita al usuario que
    ingrese una cantidad minima y maxima
    de ambientes que desea para su inmueble.
    Devuelve una lista con la informacion
    ingresada por el usuario.
    """

    min_ambientes_deseados = validar_numero(input("Ingrese la minima cantidad de ambientes que desea para su propiedad: "))

    max_ambientes_deseados = validar_numero(input("Ingrese la maxima cantidad de ambientes que desea para su propiedad: "))

    while min_ambientes_deseados > max_ambientes_deseados:

         print("LA CANDIDAD MINIMA DE AMBIENTES DEBE SER IGUAL O MENOR A LA CANTIDAD MAXIMA DESEADA.")

         min_ambientes_deseados = validar_numero(input("Ingrese la minima cantidad de ambientes que desea para su propiedad: "))
         
         max_ambientes_deseados = validar_numero(input("Ingrese la maxima cantidad de ambientes que desea para su propiedad: "))
    
    cant_ambientes = [min_ambientes_deseados, max_ambientes_deseados]
    
    return cant_ambientes 


def superficie():
    """
    Esta funcion solicita al usuario que
    ingrese una cantidad minima y maxima
    de superficie (en metros cuadrados)
    que desea para su inmueble.
    Devuelve una lista con la informacion
    ingresada por el usuario.
    """

    min_superficie_deseada = validar_numero(input("Ingrese la minima superficie (en metros cuadrados) que desea para su propiedad: "))

    max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie (en metros cuadrados) que desea para su propiedad: "))

    while min_superficie_deseada > max_superficie_deseada:

         print("LA SUPERFICIE MINIMA DESEADA DEBE SER IGUAL O MENOR A LA MAXIMA.")

         min_superficie_deseada = validar_numero(input("Ingrese la minima superficie (en metros cuadrados) que desea para su propiedad: "))
         
         max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie (en metros cuadrados) que desea para su propiedad: "))
    
    cant_superficie = [min_superficie_deseada, max_superficie_deseada]

    return cant_superficie


def filtros_a_aplicar(filtros_deseados):
    """
    Esta funcion recibe como parametro
    un diccionario vacio. Le solicita
    al usuario el ingreso de los filtros
    que desea aplicar en su busqueda.
    A partir de ello graba el diccionario
    con la informacion requerida para filtrar
    la informacion.
    Devuelve el diccionario con la informacion
    requerida.
    """
    
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
    """
    Esta funcion recibe como parametros
    una lista con la informacion sobre
    una propiedad que se esta analizando
    y el diccionario con los filtros que
    se desea aplicar en la busqueda.
    Analiza si el precio grabado en la
    propiedad cumple con los requisitos
    establecidos por el usuario. Si ese
    es el caso, graba que cumple los
    requisitos, sino es asi devuelve la
    lista tal como estaba cuando la recibio.
    """
    
    try:
        
        if (filtros_deseados[PRECIO][PESOS][DESEA_DIVISA]) and (propiedad[MONEDA] == "ARS") and (float(propiedad[PRECIO]) >= filtros_deseados[PRECIO][PESOS][MINIMO_DIVISA]) and (float(propiedad[PRECIO]) <= filtros_deseados[PRECIO][PESOS][MAXIMO_DIVISA]):
            
            propiedad += [PRECIO]
            
        elif filtros_deseados[PRECIO][DOLARES][DESEA_DIVISA] and propiedad[MONEDA] == "USD" and (float(propiedad[PRECIO]) >= filtros_deseados[PRECIO][DOLARES][MINIMO_DIVISA]) and (float(propiedad[PRECIO]) <= filtros_deseados[PRECIO][DOLARES][MAXIMO_DIVISA]):
            
            propiedad += [PRECIO]
            
    except:
        
        propiedad = propiedad

    return propiedad


def filtrar_ambientes(propiedad, filtros_deseados):
    """
    Esta funcion recibe como parametros
    una lista con la informacion sobre
    una propiedad que se esta analizando
    y el diccionario con los filtros que
    se desea aplicar en la busqueda.
    Analiza si la cantidad de ambientes
    grabada en la propiedad cumple con
    los requisitos establecidos por el
    usuario. Si ese es el caso, graba que
    cumple los requisitos, sino es asi
    devuelve la lista tal como estaba
    cuando la recibio.
    """
    
    try:
        
        if (float(propiedad[AMBIENTES]) >= filtros_deseados[AMBIENTES][MINIMO]) and (float(propiedad[AMBIENTES]) <= filtros_deseados[AMBIENTES][MAXIMO]):
            
            propiedad += [AMBIENTES]
            
    except:
        
        propiedad = propiedad

    return propiedad


def filtrar_superficie(propiedad, filtros_deseados):
    """
    Esta funcion recibe como parametros
    una lista con la informacion sobre
    una propiedad que se esta analizando
    y el diccionario con los filtros que
    se desea aplicar en la busqueda.
    Analiza si la cantidad de superficie
    grabada en la propiedad cumple con
    los requisitos establecidos por el
    usuario. Si ese es el caso, graba que
    cumple los requisitos, sino es asi
    devuelve la lista tal como estaba
    cuando la recibio.
    """
    
    try:
        
        if (float(propiedad[SUPERFICIE]) >= filtros_deseados[SUPERFICIE][MINIMO]) and (float(propiedad[SUPERFICIE]) <= filtros_deseados[SUPERFICIE][MAXIMO]):
            
            propiedad += [SUPERFICIE]
    except:
        
        propiedad = propiedad

    return propiedad


def filtrar_tipo_prop(propiedad, filtros_deseados):
    """
    Esta funcion recibe como parametros
    una lista con la informacion sobre
    una propiedad que se esta analizando
    y el diccionario con los filtros que
    se desea aplicar en la busqueda.
    Analiza si el tipo de propiedad
    cumple con los requisitos establecidos
    por el usuario. Si ese es el caso,
    graba que cumple los requisitos,
    sino es asi devuelve la lista tal
    como estaba cuando la recibio.
    """
    
    try:
        
        if propiedad[TIPO_DE_PROPIEDAD] == filtros_deseados[TIPO_DE_PROPIEDAD]:
            
            propiedad += [TIPO_DE_PROPIEDAD]
            
    except:
        
        propiedad = propiedad

    return propiedad


def aplicar_filtros(propiedades, busqueda, filtros_deseados):
    """
    Esta funcion recibe como parametros
    los archivos abiertos y el diccionario
    con la informacion requerida para filtrar
    la informacion. Analiza que filtros quiere
    aplicar el usuario al archivo que se lee y,
    si cumple con los requerimientos, graba la
    informacion en el archivo en modo de
    escritura. Si la propiedad analizada
    no cumple con los requisitos, simplemente
    se descarta y se lee la siguiente.
    Tambien lleva la cuenta de las propiedades 
    encontradas que se encuentran tasadas en 
    pesos y en dolares.
    """

    propiedad = leer(propiedades)

    propiedad = leer(propiedades)

    NUMERO_DE_FILTROS = len(filtros_deseados)

    contar_prop_pesos = 0

    contar_prop_dolares = 0

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

        if (propiedad[11: 11 + NUMERO_DE_FILTROS] == lista_filtros_deseados) and (propiedad[MONEDA] == "USD"):

            busqueda.write(propiedad[NUMERO] + "," + propiedad[FECHA] + "," + propiedad[LATITUD] + "," + propiedad[LONGITUD] + "," + propiedad[URL] + "," + propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[PRECIO] + "," + propiedad[MONEDA] + "," + propiedad[SUPERFICIE] + "," + propiedad[AMBIENTES] + "\n")

            contar_prop_dolares += 1

            propiedad = leer(propiedades)

        if (propiedad[11: 11 + NUMERO_DE_FILTROS] == lista_filtros_deseados) and (propiedad[MONEDA] == "ARS"):

            busqueda.write(propiedad[NUMERO] + "," + propiedad[FECHA] + "," + propiedad[LATITUD] + "," + propiedad[LONGITUD] + "," + propiedad[URL] + "," + propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[PRECIO] + "," + propiedad[MONEDA] + "," + propiedad[SUPERFICIE] + "," + propiedad[AMBIENTES] + "\n")

            contar_prop_pesos += 1

            propiedad = leer(propiedades)

        else:
            propiedad = leer(propiedades)

    print("FUERON ENCONTRADAS ", contar_prop_pesos, "TASADAS EN PESOS Y ", contar_prop_dolares, "TASADAS EN DOLARES.")

    


def analizar_datos(propiedades, busqueda):
    """
    Recibe como parametros el archivo
    a leer y el archivo a escribir.
    Dirige como se graba la informacion
    en el segundo archivo dependiendo de
    si el usuario desea aplicar filtros
    de busqueda o desea ver todas las
    propiedades disponibles.
    """

    print("GRACIAS POR ELEGIRNOS.")

    print("HAY", contar_propiedades(propiedades), " PROPIEDADES DISPONIBLES, PUEDE VERLAS TODAS O TAMBIEN PUEDE FLITRAR SU BUSQUEDA POR:  \n1)TIPO DE PROPIEDAD\n2)PRECIO\n3)SUPERFICIE\n4)AMBIENTES")

    desea_filtros = validar_ingreso(input("Desea realizar filtros en su busqueda? (Ingrese S/N): ").upper())

    filtros_deseados = {}

    contar_prop_pesos = 0

    contar_prop_dolares = 0
    
    busqueda.write("numero" + "," + "fecha" + "," + "latitud" + "," + "longitud" + "," + "url" + "," + "titulo" + "," + "tipo de propiedad" + "," + "precio" + "," + "moneda" + "," + "superficie" + "," + "ambientes" + "\n")

    if not desea_filtros:

        propiedad = leer(propiedades)

        propiedad = leer(propiedades)

        while propiedad[NUMERO]:

            if propiedad[MONEDA] == "USD":
                
                busqueda.write(propiedad[NUMERO] + "," + propiedad[FECHA] + "," + propiedad[LATITUD] + "," + propiedad[LONGITUD] + "," + propiedad[URL] + "," + propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[PRECIO] + "," + propiedad[MONEDA] + "," + propiedad[SUPERFICIE] + "," + propiedad[AMBIENTES] + "\n")

                contar_prop_dolares += 1
            
                propiedad = leer(propiedades)

            elif propiedad[MONEDA] == "ARS":

                busqueda.write(propiedad[NUMERO] + "," + propiedad[FECHA] + "," + propiedad[LATITUD] + "," + propiedad[LONGITUD] + "," + propiedad[URL] + "," + propiedad[TITULO] + "," + propiedad[TIPO_DE_PROPIEDAD] + "," + propiedad[PRECIO] + "," + propiedad[MONEDA] + "," + propiedad[SUPERFICIE] + "," + propiedad[AMBIENTES] + "\n")

                contar_prop_pesos += 1
            
                propiedad = leer(propiedades)

            else:

                propiedad = leer(propiedades)
        
        print("FUERON ENCONTRADAS ", contar_prop_pesos, "TASADAS EN PESOS Y ", contar_prop_dolares, "TASADAS EN DOLARES.")

    else:

        filtros_deseados = filtros_a_aplicar(filtros_deseados)

        aplicar_filtros(propiedades, busqueda, filtros_deseados)
        

def determinar_precios(resultados_de_busqueda, cant_resultados):
    """
    Esta funcion recibe como parametro
    en archivo de texto con los resultados
    de busqueda encontrados. Encuentra un
    precio maximo, uno minimo y el promedio
    de los precios y los devuelve en una tupla
    con la informacion encontrada.
    """
    
    propiedad = leer(resultados_de_busqueda)
    
    propiedad = leer(resultados_de_busqueda)
    
    precio_maximo = propiedad[PRECIO]
    
    precio_minimo = propiedad[PRECIO]
    
    ambientes_p_max = propiedad[AMBIENTES]
    
    ambientes_p_min = propiedad[AMBIENTES]
    
    suma_precios = 0
    
    promedio_precios = 0

    while propiedad[NUMERO]:
        
        suma_precios += float(propiedad[PRECIO])
        
        if precio_maximo < propiedad[PRECIO]:
            
            precio_maximo = propiedad[PRECIO]
            
            ambientes_p_max = propiedad[AMBIENTES]
        
        if precio_minimo > propiedad[PRECIO]:
            
            precio_minimo = propiedad[PRECIO]
            
            ambientes_p_min = propiedad[AMBIENTES]
            
        propiedad = leer(resultados_de_busqueda)
        
    promedio_precios = suma_precios/cant_resultados
        
    resultados_de_busqueda.seek(PRINCIPIO)
    
    return (precio_maximo, precio_minimo, promedio_precios, ambientes_p_max, ambientes_p_min)


def mostrar_resultados(resultados_de_busqueda):
    """
    Recibe como parametro el archivo con
    los resultados de busqueda del usuario.
    La funcion administra el como se
    imprimen en pantalla los datos,
    dependiendo de la cantidad que se filtro
    y si el usuario desea o no que los resultados
    se muestren en orden ascendente o descendente
    respecto al precio de los mismos. Tambien
    muestra en pantalla el mayor precio del
    resultado de busqueda, el menor y el promedio. 
    """
    
    cant_resultados = contar_propiedades(resultados_de_busqueda)

    print("\n\nHAY", cant_resultados, " PROPIEDADES AJUSTADAS A SUS PREFERENCIAS.")
    
    precio_maximo, precio_minimo, promedio_precios, ambientes_p_max, ambientes_p_min = determinar_precios(resultados_de_busqueda, cant_resultados)
    
    if (precio_minimo != precio_maximo) and (cant_resultados >= 1):
        
        print("EL PRECIO MAXIMO ENCONTRADO EN SU BUSQUEDA ES DE ", precio_maximo, ",LA PROPIEDAD POSEE ", ambientes_p_max, " AMBIENTES.")
        
        print("EL PRECIO MINIMO ENCONTRADO EN SU BUSQUEDA ES DE ", precio_minimo, ", LA PROPIEDAD POSEE ", ambientes_p_min, "AMBIENTES.")
        
        print("EL PRECIO PROMEDIO DE LOS RESULTADOS DE BUSQUEDA ES ", promedio_precios)
        
    elif (precio_maximo == precio_minimo) or (cant_resultados == 1):
        
        print("EL/LOS RESULTADO/S DE BUSQUEDA TIENE/N UN VALOR DE ", precio_maximo)

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
            
            for propiedad in lista_ordenada:

               print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL] + "\n" )
        
        else:
            
            lista_ordenada = sorted(lista_a_ordenar, reverse = True, key = lambda inmueble:inmueble[PRECIO])
            
            for propiedad in lista_ordenada:

               print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL] + "\n")
    
    elif cant_resultados == 0:
        
        print("NO SE HAN ENCONTRADO RESULTADOS PARA TU BUSQUEDA.")
        
    elif cant_resultados == 1:
        
        propiedad = leer(resultados_de_busqueda)
            
        print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: " + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL])
            
    else:
        
        propiedad = leer(resultados_de_busqueda)

        while propiedad[NUMERO]:
            
            print("\n" + "\n" + "Titulo: " + propiedad[TITULO] + "\n" + "Tipo de propiedad: " + propiedad[TIPO_DE_PROPIEDAD]  + "\n" + "Ubicacion ---->  Latitud: " + propiedad[LATITUD] + "  Longitud:" + propiedad[LONGITUD] + "\n" + "Moneda: " + propiedad[MONEDA] + "\n" + "Precio: " + propiedad[PRECIO] + "\n" + "Ambientes: " + propiedad[AMBIENTES] + "\n" + "Superficie: "  + propiedad[SUPERFICIE] + "\n" + "URL: " + propiedad[URL])
            
            propiedad = leer(resultados_de_busqueda)
            