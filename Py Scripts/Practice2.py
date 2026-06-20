######SCRIPT DE PRÁCTIAS II

#**************************************
#ejercicio pendiente: llamar desde otro script
#**************************************
#formato visual TERMINAL
separation = ("\n")
bordes = ("=" * 25)
bordeslargo = (bordes*3)
print(separation)
print(bordeslargo)

#**************************************
#funciones con  INPUT // funciones anidadas 
#**************************************
#nota: input es str, si la quieres numeric debes poner int(input())
#no lo uso así porque en la función condicional uso isdigit()
#:<5 es un espaciador, agrega espacios en terminal y no quede pegado a la variable/input
# f"{'Texto {variable} texto':espaciador}" es diferente a f"Texto {variable} texto"
    #---> el primero: es una forma de combinar texto + input + espaciador
    #---> el segundo: es una forma de combinar texto + variable


#variable principal input
#uso While True para regresar al flujo cuando ciertas condiciones no apliquen
while True:
    container_id = input(f"{'Container ID::  ':<5}")

#variables mensajes-input/print
    invalid_cont      = "A value must be entered"
    invalid_num       = "Container must be numeric"
    invalid_len       = f"Container {container_id} is not valid"
    prompt_confirm    = f"Do you want to Confirm Container ID: {container_id}?:: (Y / N){'':<5}"
    invalid_command   = "Value must be Y or N"
    invalid_command2  = "Value must be P or C"
    confirmed_cont    = f"Process Completed: Container {container_id} is confirmed"
    prompt_qc         = f"Do you want to mark {container_id} for QC?: (Y / N){'':<5}"
    marked_qc         = f"Container {container_id} has been marked for QC"
    confirm_qc        = f"Do you want to Confirm QC and Container for ID:{container_id}:: (Y / N){'':<5}"
    pass_startover    = f"No QC for Container {container_id}, do you want to Confirm or Pass?:: (C / P){'':<5}"
    pass_confirm      = f"Container {container_id} Passed. Do you want to Confirm Container?:: (Y / N){'':<5}"
    startover_conf    = f"Container {container_id} Failed. Starting again..."

#función condicional input anidada con while True
    if container_id == "":
        print(invalid_cont)
        print(bordeslargo)
        continue
    elif not container_id.isdigit():     #-Nota1---> isdigit() se usa para que acepte sólo valores numéricos
        print(invalid_num)
        print(bordeslargo)
        continue
    elif len(container_id) !=8:          #-Nota2---> len() se usa para que acepte max/min de caracteres
        print(invalid_len)
        print(bordeslargo)
        continue
    else:
        confirm = input(prompt_confirm).strip().upper() #-Nota3---> strip para que sea un caracter, upper para mayúscula/minúscula
        if confirm == "":                     
            print(invalid_cont)
            print(bordeslargo)
            continue
        elif confirm not in ("Y","N"):                  #-Nota4---> se utiliza IN para los inputs, como en SQL :D
            print(invalid_command)
            print(bordeslargo)
            continue
        elif confirm == "Y":
            print(confirmed_cont)
            break
        else:
            qc = input(prompt_qc).strip().upper() 
            if qc == "":
                print(invalid_command)
                print(bordeslargo)
                continue
            elif qc not in ("Y","N"):                   
                print(invalid_command)
                print(bordeslargo)
                continue
            elif qc != "Y":
                pass_or_startover = input(pass_startover).strip().upper()
                if pass_or_startover not in ("P","C"):
                    print(invalid_command2)
                    print(bordeslargo)
                    continue
                elif pass_or_startover == "P":
                    confirm = input(pass_confirm).strip().upper()
                    if confirm == "":                     
                        print(invalid_cont)
                        print(bordeslargo)
                        continue
                    elif confirm not in ("Y","N"):                  
                        print(invalid_command)
                        print(bordeslargo)
                        continue
                    elif confirm == "Y":
                        print(confirmed_cont)
                        break
                    else:
                         print(startover_conf)
                         continue
                elif pass_or_startover == "C":
                     confirm = input(prompt_confirm).strip().upper()
                     if confirm == "":
                          print(invalid_cont)
                          print(bordeslargo)
                          continue
                     elif confirm not in ("Y","N"):
                          print(invalid_command)
                          print(bordeslargo)
                          continue
                     elif confirm == "Y":
                          print(confirmed_cont)
                          break
                     else:
                          print(startover_conf)
                          continue
                else:
                    print(startover_conf)
                    continue
            elif qc == "Y":
                print(marked_qc)
                confirm = input(confirm_qc).strip().upper()
                if confirm == "":                     
                        print(invalid_cont)
                        print(bordeslargo)
                        continue
                elif confirm not in ("Y","N"):                  
                        print(invalid_cont)
                        print(bordeslargo)
                        continue
                elif confirm == "Y":
                        print(confirmed_cont)
                        break
                else:
                        print("Process Cancelled: returning to main screen...")
                        print(bordeslargo)
            else:
                print("Process Completed: Returning to main screen...")
                print(bordeslargo)
                