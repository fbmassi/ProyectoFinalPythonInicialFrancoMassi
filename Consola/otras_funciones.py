def validar_ingreso(ingreso):

    """
    Valida si el usuario ingreso los datos correctamente. 
    Devuelve una variable de tipo Booleano dependiendo de 
    si el usuario ingreso 'S' o 'N'.
    """

    validacion = False 

    while not validacion:

        if ingreso == "S" or ingreso == "N":
            validacion = True 
        
        else:
            ingreso = input("INGRESO INCORRECTO. POR FAVOR INGRESE 'S' O 'N': ").upper()
    
    return ingreso == "S"


    
def validar_numero(ingreso):

    """
    Valida si el usuario ingreso los datos correctamente. 
    Devuelve una la misma variable que el usuario ingreso,
    siempre y cuando sea de tipo numerica.
    """

    validacion = False 

    while not validacion:

        if ingreso.isnumeric():
            validacion = True 
        
        else:
            ingreso = input("INGRESO INCORRECTO. POR FAVOR INGRESE UNA VARIABLE NUMERICA: ").upper()
    
    return int(ingreso)


def validar_tipo_propiedad(ingreso):

    validacion = False

    while not validacion:

        if ingreso == 'Casa' or ingreso == 'Departamento':
            
            validacion = True 
        
        else:
            
            ingreso = input("INGRESO INCORRECTO. POR FAVOR INGRESE 'CASA' O 'DEPARTAMENTO' SIN PUNTOS NI ESPACIOS: ").capitalize()

    return ingreso

def leer(archivo):

    """
    Esta funcion recibe como parametro un archivo CSV y
    lee una linea del archivo cada vez que se ejecuta.
    Devuelve una lista con el contenido de la linea que se leyo.
    En cada elemento se almacenan los valores separdos por las comas.
    """

    linea = archivo.readline()

    return linea.rstrip("\n").split(",") if linea else ["","","","","","","","","","",""]