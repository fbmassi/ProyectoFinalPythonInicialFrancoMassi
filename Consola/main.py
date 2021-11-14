# PROYECTO FINAL PYTHON INICIAL 
# AUTOR: FRANCO BALTASAR MASSI
# BUSCADOR DE ALQUILERES

from lectura import contar_propiedades, analizar_datos, mostrar_resultados

def main():

    """
    Funcion principal del programa. A travez de esta, corre el programa general.
    Le muestra al usuario los resyltados de su busqueda.
    """

    propiedades = open("propiedades_CABA.csv")
    busqueda = open("busqueda.csv", "w")
    print("BIENVENIDO AL BUSCADOR DE ALQUILERES")
    print("AQUI USTED PODRA ENCONTRAR LOS MEJORES DEPARTAMENTOS EN ALQUILER EN LA CIUDAD \nDE BUENOS AIRES, CON LAS CARACTERISTICAS QUE USTED DESEE.")
    analizar_datos(propiedades, busqueda)
    propiedades.close()
    busqueda.close()
    resultados_de_busqueda = open("busqueda.csv")
    mostrar_resultados(resultados_de_busqueda)
    print("MUCHAS GRACIAS POR HABER USADO ESTA PLATAFORMA, VUELVA PRONTO.")

    
main()


