######SCRIPT PARA PRÁCTICAS SIMPLES

#**************************************
#mini función para traer operación y valor
#**************************************
#formato visual TERMINAL
separation = ("\n")
bordes = ("=" * 27)
bordeslargo = (bordes*3)
print(separation)
print(bordes)

#variables valores (se pueden cambiar)
a = 2
b = 5
c = 7.5

#armado de variables fijas
result1 = a * b - c
result2 = (c+b)/a
result3 = a + b + c

#otras variables para traer texto
mensaje1 = "Operacion 1"
mensaje2 = "Operacion 2"
mensaje3 = "Operacion 3"

#output - final - print con condicionales simples
if result1 + result3: 
      print ("Es válida:",mensaje1)
elif result2:
      print ("Es válida:",mensaje2)
else:
      print ("Es válida:",mensaje3)


#**************************************
#mini función / otra forma de output con función
#**************************************
print(bordes)
print(separation)
print(bordeslargo)

#valores_return (Sólo se puede cambiar uno a la vez)
    #define los valores a retornar 
    #para poder cambiarlos desde aquí
    #y no en la función condicional
ret1 = 2.5+14.5
ret2 = 0
ret3 = 0

#función con condicionales IF
def elegir_mensaje(result1, result2, result3):
    if result1 + result3 == ret1:
            return f"Función válida: {mensaje1} y {mensaje3} -->> {str(result1 + result3)}"
    elif result2 == ret2:
            return f"Función válida: {mensaje2} -->> {str(result2)}"
    elif result3 == ret3:
            return f"Función válida: {mensaje3} -->> {str(result3)}"
    else:
            return "No aplica ninguna condición"
print (elegir_mensaje(result1, result2, result3))


#**************************************
#mini visual para ver mensajes y resultado
#**************************************
    #notar que aquí se crearon varias variables/parámetros que no estaban antes
    #"imprimir" es el nombre de la función
    #"mensaje" y "resultado" se crean para capturar los rows en "glosario" arriba
    #se llaman en la fución con "items", para luego armar el print
print(bordeslargo)
print(separation)

#creación diccionario para glosario
glosario = {
    mensaje1: result1,
    mensaje2: result2,
    mensaje3: result3,
           }

#función imprimir:
    #"<10" Reserva 10 caracteres y alinea el texto a la izquierda.
    #fun_glosario es el parámetro que se declara para unirlo al diccionario por "glosario"
    #ya que no se puede usar el mismo nombre en la lógica
    #en el for: por cada fila del diccionario, toma la clave en mensaje y el valor en resultado (de glosario)
    #y lo lista abajo para el print
def imprimir(fun_glosario):
    for mensaje, resultado in fun_glosario.items():
         print(f"{mensaje:<10} -->> {resultado}")

#print con función imprimir para traer valores de glosario


#**************************************
#mini programa para traer hundredweight
#**************************************
print(bordes)
imprimir(glosario)
print(bordes)
print(separation)
print(bordeslargo)

#unit of measures configured (usando diccionario)
UOM = {
     "PL": 100,
     "CS": 10,
     "EA": 1,
    }

#quantity required
QTY = 8  #Cambia aquí to quantity
REQ_UOM = "PL" #Cambia aquí tu UoM
REQ = UOM[REQ_UOM] 

#total quantity
T_QTY = QTY * REQ

#estimación de HW
HundredWeight = 0.2

#output header
print(f"HUNDREDWEIGHT RATES: {HundredWeight:<12}")

#output con condicional
if T_QTY > 100 :
    print(f"Hundred Weight Shipment, Total Freight Charges: ${T_QTY*HundredWeight}")
else:
    print(f"No Freight Charges Applied for {T_QTY} {REQ_UOM}")

#Fin del SCRIPT
#***
print(bordeslargo)
print(separation)

"""
Nota: las tabulaciones son importantes, no es como en SQL
que no importa donde esté la lógica siempre y cuando
el batch anterior la continúe o pare y deje que una nueva vaya
y opere (como al poner GO o ;)

Pero en Py hay que tabular para hacer funciones, como por ejemplo:

IF condición
    return/print/elif/else

La tabulación es en la segunda línea, no hay corchetes ni nada que indiquen
el órden o grupo de la lógica, como por ejemplo en C# o en JSON
"""