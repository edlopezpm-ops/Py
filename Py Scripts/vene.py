# Comparación Venezuela 1997 vs 2026
# Imprime una tabla formateada en consola

# data cruda
# se llamarán abajo con la función row
# rows separadas con comas
data = [
    ["1997", "US$ 35-40 B", "US$ 90-100 B", "45-50%"],
    ["2026", "US$ 240 B",   "US$ 80-120 B", "80-90%"]
]

# datos de cabecero en lista
# acá se agregan los valores que se llamarán abajo con center(widths)
headers = ["Año", "Deuda Externa", "PIB", "Índice de Pobreza"]

# Anchos de columna, los valores son caracteres que reservará python usando lista
# acá se agregan los valores que se llamarán abajo con center(widths)
widths = [8, 18, 18, 20]

# Línea horizontal
# líneas que crean los formatos
line = "+" + "+".join("-" * w for w in widths) + "+"

# imprime el header con formatos
# los valores 0, 1, 2, 3, son listas que traen la lista de widths, se concatenan con center
print(line)
print("|" + headers[0].center(widths[0]) + "|" + headers[1].center(widths[1]) + "|" + headers[2].center(widths[2]) + "|" + headers[3].center(widths[3]) + "|")
print(line)

# imprime data con formatos
# for los trae en loop
for row in data:
    print("|" + row[0].center(widths[0]) + "|" + row[1].center(widths[1]) + "|" + row[2].center(widths[2]) + "|" + row[3].center(widths[3]) + "|")

print(line)


#*******************************
#mini programa input con while
#*******************************


#variables principales
meta = float(input("¿Cuánto quieres ahorrar? : "))
ahorro = 0

# lógica que hará loop hasta que lo acumulado se alcance
while ahorro < meta:
    acumulado = float(input("Indica cantidad a guardar: "))
    ahorro += acumulado
    if meta-ahorro != 0:
        print(f"Te faltan {str(meta-ahorro)}")
    else: 
        continue

# esto imprime cuando se logre el total acumulado esperado
# esta lógica innecesaria y overkill es sólo para entender cómo trabajar el for
confirmacion = {"Tu":" meta","fue":" completada"}
for meta2, completada in confirmacion.items():
    print(f"{meta2}{completada}")

# confirmacion = str(ahorro)
# for total_ahorro in confirmacion:
#     print(f"Total ahorro {total_ahorro}")


#*******************************
#mini programa comida
#*******************************


dale = str(input("¿Quieres carne con vegetales?:  ")).strip()
if len(dale)==2 and dale.upper() == "SI":
    print("Ok, yo te la hago y comemos juntos")
elif dale.upper() != "SI":
    input("Ah, ¿qué quieres comer entonces?:  ")
    print("Bueh, traé comida pueh...")