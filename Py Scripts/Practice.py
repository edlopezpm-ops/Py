"""
Script para prácticas simples

"""

#inicio-problema-punto de partida
#razón del código que haces

separation = ("\n*\n")
print(separation)

a = 1
b = 5
c = 7.5

#armado de variables

result1 = a * b - c
result2 = (c+b)/a
result3 = a + b + c

#otras variables para traer

mensaje1 = "Operacion 1"
mensaje2 = "Operacion 2"
mensaje3 = "Operacion 3"

glosario = {
    mensaje1: result1,
    mensaje2: result2,
    mensaje3: result3,
           }

#output - final - print

print("=" * 25)

if result1 + result3 : 
      print ("Es válida:",mensaje1)
else:
      print ("Es válida:",mensaje2)

#funcion glosario
"""
notar que aquí se crearon varias variables/parámetros que no estaban antes
"imprimir" es el nombre de la función
"mensaje" y "resultado" se crean para capturar los rows en "glosario" arriba
se llaman en la fución con "items"cls, para luego armar el print
"""

def imprimir(funcion_imprimir):
    for mensaje, resultado in funcion_imprimir.items():
         print(f"{mensaje:<12} -->> {resultado}")

#impresión de glosario
print("=" * 25)
imprimir(glosario)
print("=" * 25)

#**************************************
#mini programa para traer hundredweight
#**************************************
print(separation)

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

#output
print("=" * 40)
print(f"HUNDREDWEIGHT RATES::{HundredWeight:<12}")
if T_QTY > 100 :
    print(f"Hundred Weight Shipment, Total Freigh Charges: ${T_QTY*HundredWeight}")
else:
    print(f"No Freigh Charges Applied for {T_QTY} {REQ_UOM}")
print("=" * 40)

print(separation)