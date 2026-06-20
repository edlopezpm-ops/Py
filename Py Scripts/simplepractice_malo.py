######SCRIPT DE PRÁCTIAS

#**************************************
#llamar desde otro script
#**************************************
#formato visual TERMINAL
separation = ("\n")
bordes = ("=" * 25)
bordeslargo = (bordes*3)
print(separation)
print(bordes)

#**************************************
#funciones con  INPUT // funciones anidadas 
#**************************************
#nota: input es str, si la quieres numeric debes poner int(input())
#no lo uso así porque en la función condicional uso isdigit()
#:<5 es un espaciador, agrega espacios en terminal y no quede pegado a la variable/input
# f"{'Texto {variable} texto':espaciador}" es diferente a f"Texto {variable} texto"
    #---> el primero: es una forma de combinar texto + input + espaciador
    #---> el segundo: es una forma de combinar texto + variable

#variables input
container_id = input(f"{'Container ID:  ':<5}")
confirm      = input(f"{'Do you want to Confirm Container ID: {container_id:>5}?: ':<5}")
qc           = input(f"{'Do you want to mark {container_id} for QC?: ':<5}")

#función condicional input anidada
if container_id == "":
    print("A value must be entered")
elif not container_id.isdigit():     #---> isdigit() se usa para que acepte sólo valores numéricos
    print("Container must be numeric")
elif len(container_id) !=8:          #---> len() se usa para que acepte max/min de caracteres
    print(f"Container {container_id} is not valid")
elif container_id:
    if confirm.upper() == "Y":       #---> upper() se usa para que acepte "Y" o "y"
        print(f"Container {container_id} is confirmed")
    else:
        if qc.upper() == "Y":
            print(f"Container {container_id} has been marked for QC")
        else:
             container_id