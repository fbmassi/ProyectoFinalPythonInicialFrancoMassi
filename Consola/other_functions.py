def es_valido(ingreso):

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
    


def desea_seguir():
    
    """
    Le pregunta al usuario si desea seguir realizando busquedas de alquileres. 
    La funcion devuelve una cadena no vacia si el usuario ingreso 'S' 
    y una vacia si ingreso 'n'.
    """

    seguir = input("Desea seguir buscando? (Ingrese S/N): ").upper()

    return "Seguir" if es_valido(seguir) else ""



def ingreso():
    #Solicita el ingreso de un valor y devuelve el mismo. 
    ingreso = input("Ingrese: ")
    return ingreso 