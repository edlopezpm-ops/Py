# MASTER LIST: elementos propios del lenguaje Python
# Ignora variables/objetos custom creados por el usuario

import keyword
import builtins

keywords = {
    "False": "Valor booleano falso.",
    "None": "Ausencia de valor.",
    "True": "Valor booleano verdadero.",
    "and": "Operador lógico Y.",
    "or": "Operador lógico O.",
    "not": "Operador lógico NO.",
    "if": "Condicional.",
    "elif": "Condición alternativa.",
    "else": "Bloque alternativo.",
    "for": "Bucle por iteración.",
    "while": "Bucle por condición.",
    "break": "Rompe un bucle.",
    "continue": "Salta a la siguiente iteración.",
    "def": "Define una función.",
    "return": "Devuelve un valor.",
    "class": "Define una clase.",
    "import": "Importa módulos.",
    "from": "Importa partes específicas de un módulo.",
    "as": "Crea alias.",
    "try": "Inicia manejo de errores.",
    "except": "Captura errores.",
    "finally": "Siempre se ejecuta al final.",
    "raise": "Lanza un error.",
    "with": "Administra recursos automáticamente.",
    "lambda": "Función anónima.",
    "pass": "No hace nada; placeholder.",
    "in": "Verifica pertenencia.",
    "is": "Compara identidad.",
    "global": "Declara variable global.",
    "nonlocal": "Usa variable de scope externo.",
    "yield": "Devuelve valores desde un generador.",
    "async": "Define código asíncrono.",
    "await": "Espera una operación asíncrona.",
    "match": "Comparación de patrones.",
    "case": "Caso dentro de match.",
    "del": "Elimina referencias.",
    "assert": "Valida una condición."
}

caracteres_especiales = {
    "\\n": "Salto de línea.",
    "\\t": "Tabulación.",
    "\\\\": "Barra invertida literal.",
    "\\\"": "Comilla doble dentro de string.",
    "\\'": "Comilla simple dentro de string.",
    "\\r": "Retorno de carro.",
    "\\b": "Backspace.",
    "\\f": "Salto de página.",
}

operadores = {
    "+": "Suma o concatenación.",
    "-": "Resta.",
    "*": "Multiplicación o repetición.",
    "/": "División decimal.",
    "//": "División entera.",
    "%": "Módulo / residuo.",
    "**": "Potencia.",
    "=": "Asignación.",
    "==": "Igualdad.",
    "!=": "Diferente.",
    ">": "Mayor que.",
    "<": "Menor que.",
    ">=": "Mayor o igual.",
    "<=": "Menor o igual.",
    "+=": "Suma y reasigna.",
    "-=": "Resta y reasigna.",
    "*=": "Multiplica y reasigna.",
    "/=": "Divide y reasigna.",
}

simbolos = {
    "()": "Paréntesis: llamadas, agrupación, tuplas.",
    "[]": "Listas, índices o slicing.",
    "{}": "Diccionarios, sets o bloques en f-strings.",
    ":": "Inicia bloques de código.",
    ",": "Separa elementos.",
    ".": "Accede a métodos o atributos.",
    "#": "Comentario.",
    "@": "Decorador.",
    "->": "Anotación de retorno.",
    "_": "Variable temporal o valor ignorado.",
}

estructuras = {
    "list": "Lista mutable: [1, 2, 3].",
    "tuple": "Tupla inmutable: (1, 2, 3).",
    "dict": "Diccionario clave/valor: {'a': 1}.",
    "set": "Conjunto sin duplicados: {1, 2, 3}.",
    "str": "Texto.",
    "int": "Entero.",
    "float": "Decimal.",
    "bool": "Booleano True/False.",
}

def imprimir_titulo(titulo):
    print("=" * 60)
    print(titulo)
    print("=" * 60)

def imprimir_diccionario(diccionario):
    for clave, descripcion in diccionario.items():
        print(f"{clave:<12} -> {descripcion}")
    print()

imprimir_titulo("KEYWORDS DE PYTHON")
for kw in keyword.kwlist:
    print(f"{kw:<12} -> {keywords.get(kw, 'Keyword reservada de Python.')}")
print(f"\nTotal keywords: {len(keyword.kwlist)}\n")

imprimir_titulo("CARACTERES ESPECIALES")
imprimir_diccionario(caracteres_especiales)

imprimir_titulo("OPERADORES")
imprimir_diccionario(operadores)

imprimir_titulo("SÍMBOLOS IMPORTANTES")
imprimir_diccionario(simbolos)

imprimir_titulo("ESTRUCTURAS / TIPOS BÁSICOS")
imprimir_diccionario(estructuras)

imprimir_titulo("FUNCIONES BUILT-IN MÁS USADAS")
funciones_comunes = [
    "print", "input", "len", "type", "str", "int", "float", "bool",
    "list", "dict", "set", "tuple", "range", "enumerate", "zip",
    "sum", "min", "max", "abs", "round", "sorted", "open", "help"
]

for funcion in funciones_comunes:
    obj = getattr(builtins, funcion)
    print(f"{funcion:<12} -> {obj.__doc__.split('.')[0] if obj.__doc__ else 'Función built-in.'}")

print("=" * 60)
print("FIN DEL MASTER LIST")
print("=" * 60)