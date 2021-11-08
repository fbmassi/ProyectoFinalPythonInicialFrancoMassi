def validar_ingreso(ingreso):

    """
    Valida si el usuario ingreso los datos correctamente. 
    devuelve una variable de tipo Booleano.
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
    devuelve una variable de tipo Booleano.
    """

    validacion = False 

    while not validacion:

        if ingreso.isnumeric():
            validacion = True 
        
        else:
            ingreso = input("INGRESO INCORRECTO. POR FAVOR INGRESE UNA VARIABLE NUMERICA: ").upper()
    
    return ingreso.isnumeric()

def desea_seguir():
    
    """
    Le pregunta al usuario si desea seguir realizando busquedas de alquileres. 
    La funcion devuelve una cadena no vacia si el usuario ingreso 'S' 
    y una vacia si ingreso 'n'.
    """

    seguir = input("Desea seguir buscando? (Ingrese S/N): ").upper()

    return "Seguir" if validar_ingreso(seguir) else ""



def ingreso():

 #  Solicita el ingreso de un valor y devuelve el mismo.

    ingreso = input("Ingrese: ")

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