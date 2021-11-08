# PROYECTO FINAL PYTHON INICIAL 
# AUTOR: FRANCO BALTASAR MASSI
# BUSCADOR DE ALQUILERES

from other_functions import desea_seguir
from lectura import contar_propiedades

def main():

    """
    Funcion principal del programa. A travez de esta, corre el programa general.
    Le muestra al usuario los resyltados de su busqueda.
    """

    #propiedades = open("propiedades.csv")
    #resultados_de_busqueda = ("resultados_de_busqueda.csv, "w")    print("BIENVENIDO AL BUSCADOR DE ALQUILERES")
    print("AQUI USTED PODRA ENCONTRAR LOS MEJORES DEPARTAMENTOS EN ALQUILER EN LA CIUDAD \nQUE USTED ELIJA, CON LAS CARACTERISTICAS QUE USTED DESEE.")
    #while desea_seguir():
    #   extraer_datos(propiedades, resultados_de_busqueda)
    #  print("S")
    print("MUCHAS GRACIAS POR HABER USADO ESTA PLATAFORMA, VUELVA PRONTO.")

    
main()

"""
CABA = open('propiedades_CABA.csv')
print(contar_propiedades(CABA))
linea = CABA.readline()
print(linea)
CABA.close()
"""
