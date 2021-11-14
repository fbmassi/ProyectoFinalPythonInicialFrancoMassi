# PROYECTO FINAL PYTHON INICIAL 
# AUTOR: FRANCO BALTASAR MASSI
# BUSCADOR DE ALQUILERES

from lectura import contar_propiedades, analizar_datos, mostrar_resultados
from otras_funciones import validar_ingreso

def main():

    """
    Funcion principal del programa. A travez de esta,
    corre el programa general. Estara activo mientras
    el usuario desee llevar a cabo su busqueda. 
    Le muestra al usuario los resultados de su busqueda.
    """
    print("\n\nBIENVENIDO AL BUSCADOR DE ALQUILERES")
    print("AQUI USTED PODRA ENCONTRAR LOS MEJORES DEPARTAMENTOS EN ALQUILER EN LA CIUDAD \nDE BUENOS AIRES, CON LAS CARACTERISTICAS QUE USTED DESEE.")
    desea_seguir = True
    while desea_seguir:
        propiedades = open("propiedades_CABA.csv")
        busqueda = open("busqueda.csv", "w")
        analizar_datos(propiedades, busqueda)
        propiedades.close()
        busqueda.close()
        resultados_de_busqueda = open("busqueda.csv")
        mostrar_resultados(resultados_de_busqueda)
        resultados_de_busqueda.close()
        desea_seguir = validar_ingreso(input("\n\nDesea seguir buscando propiedades? (Ingrese S/N): ").upper())
    print("MUCHAS GRACIAS POR HABER USADO ESTA PLATAFORMA, VUELVA PRONTO.\n\n")

    
main()


