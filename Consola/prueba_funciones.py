from lectura import NUMERO, AMBIENTES, SUPERFICIE, MONEDA, PRECIO, TIPO_DE_PROPIEDAD
from other_functions import validar_numero

#PRUEBA NUMERO 1

"""
CABA = open('Archivos Usados\\propiedades_CABA.csv')
print(contar_propiedades(CABA))
linea = CABA.readline()
print(linea)
CABA.close()
"""


#PRUEBA NUMERO 2

"""
def superficie(propiedad):
    
    min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))

    max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))


    while min_superficie_deseada > max_superficie_deseada:

         print("LA SUPERFICIE MINIMA DEBE SER IGUAL O MAYOR A LA SUPERFICIE MAXIMA DESEADA.")

         min_superficie_deseada = validar_numero(input("Ingrese la minima superficie que desea para su propiedad: "))
         
         max_superficie_deseada = validar_numero(input("Ingrese la maxima superficie que desea para su propiedad: "))


    if propiedad[SUPERFICIE] >= min_superficie_deseada and propiedad[SUPERFICIE] <= max_superficie_deseada:

        propiedad += [SUPERFICIE]

    return propiedad



def prueba_de_funciones(propiedad, filtros_deseados):
    
    NUMERO_DE_FILTROS = len(filtros_deseados)

    if propiedad[NUMERO]:
        
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

            print('APROBADO')

        else:
            print('NO APROBADO')


prueba_de_funciones([3,2021_10_25,-34.596046,-58.392166,'https://departamento.mercadolibre.com.ar/MLA-1100293298-alquiler-dto-2-12-ambientes-tipo-loft-recoleta-caba-_JM', 'Alquiler Dto. 2 1/2  Ambientes Tipo Loft Recoleta (caba)', 'Departamento' , 47000.0, 'ARS' ,55,3], [SUPERFICIE])
"""

#PRUEBA NUMERO 3
"""
dict_1 = {1:3,2:4,5:6}
fil = [x for x in dict_1]
if fil == [1,2,5]:
    print('si')
"""

#PRUEBA NUMERO 4
