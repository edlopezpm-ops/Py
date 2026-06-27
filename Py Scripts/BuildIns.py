# for item in dir(__builtins__):
#     print(item)

#
#*******************************
#diccionarions
#*******************************
#
diccionario = {
        "llave": "valor llave",
        "llave 2": "valor llave 2",
        "llave 3": "valor llave 3"
}
#para llamarlo necesitas mencional la llave o el valor en []
print(f"Esto imprime el diccionario que es '{diccionario["llave 3"]}'")

dic2 = {
        "llave1":
            {
                "metallave1":
                {
                    "metametallave1":"valor metametallave1",
                    "metametallave1_2":"valor metametallave1_2"
                }
            },
        "llave2":
            {
                    "metametallave2":
                {
                    "metametallave2":"valor metametallave2",
                    "metametallave2_2":"valor metametallave2_2"
                }
            }
        }
#debes hacer el print > llave > metallave > metametallava para imprimir 1 valor selecto
print(dic2["llave1"]["metallave1"]["metametallave1_2"])

#listar y contar con diccionarios vacíos
print("*"*50)

lista = ["v1","v2","v1","v3","v1","v4","v3"]
lista_diccionario = {}
for lt in lista:
    if lista_diccionario.get(lt):
        lista_diccionario[lt] += 1
    else:
        lista_diccionario[lt] = 1

#te dirá cuántas veces se repite el valor
print(lista_diccionario)