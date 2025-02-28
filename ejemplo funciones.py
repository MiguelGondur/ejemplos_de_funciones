#coding utf - 8
#================================
#tema: funciones
#programa: Ejemplo funciones
#contacto: 
#================================


#FUNCIONES
##EJEMPLO DE FUNCIONES

from datetime import datetime 

def saludar():
    print('hola a todo el que saludo')
    
def vizualizar_tabla(numero):
    for multiplicador in range(1,11):
        resultado = numero * multiplicador
        print(numero, 'x', multiplicador, '=', resultado)
def calcular_cubo(numero):
    cubo = numero **3
    return cubo 

    
def obtener_fecha_actual():
    fecha_obtenida = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return fecha_obtenida


print('prgrama para conocer las funciones')
for ciclo in range(1,11):
   saludar()

print('\n ahora generamos la tabla de multiplicar')
numero = int(input('Ingresa un numero entero: '))

vizualizar_tabla(numero) 
valor_cubico = calcular_cubo(numero)
print(f'el valor cubicco del dato {numero} es {valor_cubico}')

dato_fecha = obtener_fecha_actual()
print(f'la fecha obtinda es {dato_fecha}')