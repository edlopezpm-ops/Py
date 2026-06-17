var1="qué fue mardito cómo estái"
print(var1)
# eso es fácil
# muy fácil
"""
comentario de varias líneas es con tres "
cambia color pero sigue siendo comentario
en SQL por ejemplo, todos son del mismo color
"""
# listo bebé no más suggestions (se arregla desabilitando copilot)
    # "editor.inlineSuggest.enabled": false

# una variable puede ser una función o un valor
# las variables son case sensitive
# es como un declare en SQL pero sin @ (y sin declare)

var = "verga mijo bien y vos" 
    #variable 1
if var == "verga mijo bien y vos":
    print(var)

var = "prueba nota abajo"     
    #variable 2 (se llama esta si no hay print antes)
print(var)

"""
en python, si definiste varias variables con el mismo nombre
pero diferente valor, ejemplo "var = 1" o "var = 2"
te traerá siempre la última si no se diferencian

"""

#texto es str
#numeros son int
#decimales son float

num1 = 5
dec1 = 4.4 #decimales no aceptan comas

var2 = "cuándo me vais a pagar los "+ str(num1) +" bolos?"
var3 = "qué "+ str(num1) +"? no eran "+ str(dec1) +"?"

print(var2)
print(var3)

"""
otra forma de mergear texto es con f"texto {variable} más texto"
una prueba corta abajo usando las mismas var pero cambiando valores
"""

var2 = f"cuándo me vais a pagar los {num1} bolos?" #ejemplo con f'
var3 = f"qué {num1}? no eran {dec1}?" #ejemplo con f'

#es mejor usar esta opción f para resultados que traen str e int/float
#python traerá todo lo que esté dentro de { } indistintamente si es numérico o texto

print(var2)
print(var3)

""" otros tipos de datos"""

var4 = None #tiene que estar en cap la N sino no lo reconoce
var5 = True #igual en cap la T, esto es boolean

print(var4)
print(type(var4)) #imprime el tipo de dato

print(var5)
print(type(var5)) #imprime el tipo de dato

""" cómo hacer CONVERT tipo SQL pero pa' python """

var6 = 10 #valor int
var6 = str(var6) #se pasa a valor string
print(var6) #lo trae como valor string
print(type(var6)) #confirma que el valor es string (class)

#nota: no se puede convertir texto-adcdfg a número
#pero sí al revez como en SQL

""" variable vacía, para cualquier cosa se usan """

var7="" #ya está vacía
var7=str() #ya está vacía, es igual que la otra

var8=int() #misma miesma

var9=bool() #igual, sirve para algo, creo

print(var7,var8,var9) #print unidos y bueno

""" cómo concatenar con f y {}"""

var10 = f"Ejemplo de concatenado {num1} y {type(num1)}"

print(var10)

#puedes meter variables, funciones y otros con {}, pero usando f""

""" variables de multiples valores, como IN en SQL"""

var11 = "\n".join([
    var1,
    var2,
    var3,
    "ajá mijo entonces cómo quedamos?",
    "no sé yo no tengo cobres"
])

print("=" * 5)
print(var11)
print("=" * 5)

""" llamar un script/funcion de otro archivo"""

# Importamos la clase Aplicacion desde el script HelloWordOverEng.py,
# creamos una instancia de esa clase y ejecutamos su método correr(),
# que arma el mensaje y lo imprime en consola.

from HelloWordOverEng import Aplicacion
app = Aplicacion()
app.correr()

# te extraño SQL:: EXEC SP_NAME PARAM =(