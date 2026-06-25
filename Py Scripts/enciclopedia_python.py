# enciclopedia_python.py

import keyword
import builtins


SECCIONES = {
    "1": "Keywords",
    "2": "Operadores",
    "3": "Símbolos",
    "4": "Tipos básicos",
    "5": "Built-ins",
    "6": "Métodos str",
    "7": "Métodos list",
    "8": "Métodos dict",
    "9": "Métodos set",
    "10": "Archivos",
    "11": "Excepciones",
    "12": "OOP",
    "13": "Decoradores",
    "14": "Generadores",
    "15": "Context managers",
    "16": "Async / Await",
    "17": "Patrones comunes",
    "18": "Conceptos internos",
}


DATA = {
    "Keywords": {
        "def": "Define una función.",
        "return": "Devuelve un valor desde una función.",
        "class": "Define una clase.",
        "if / elif / else": "Control condicional.",
        "for": "Bucle por iteración.",
        "while": "Bucle por condición.",
        "break": "Sale de un bucle.",
        "continue": "Salta a la siguiente iteración.",
        "try / except / finally": "Manejo de errores.",
        "raise": "Lanza un error manualmente.",
        "with": "Administra recursos automáticamente.",
        "lambda": "Función anónima.",
        "yield": "Produce valores desde un generador.",
        "async / await": "Programación asíncrona.",
        "global": "Usa una variable global.",
        "nonlocal": "Usa una variable de un scope externo.",
        "match / case": "Pattern matching.",
        "import / from / as": "Importación de módulos.",
    },

    "Operadores": {
        "+": "Suma o concatenación.",
        "-": "Resta.",
        "*": "Multiplicación o repetición.",
        "/": "División decimal.",
        "//": "División entera.",
        "%": "Residuo.",
        "**": "Potencia.",
        "=": "Asignación.",
        ":=": "Asignación dentro de expresión.",
        "==": "Igualdad.",
        "!=": "Diferente.",
        "> / < / >= / <=": "Comparaciones.",
        "and / or / not": "Operadores lógicos.",
        "is": "Compara identidad de objetos.",
        "in": "Verifica pertenencia.",
    },

    "Símbolos": {
        "()": "Llamadas, agrupación o tuplas.",
        "[]": "Listas, índices o slicing.",
        "{}": "Diccionarios, sets o f-strings.",
        ":": "Inicia bloques o separa clave/valor.",
        ",": "Separa elementos.",
        ".": "Accede a métodos o atributos.",
        "#": "Comentario.",
        "@": "Decorador.",
        "->": "Anotación de retorno.",
        "_": "Valor ignorado o variable temporal.",
        "*args": "Argumentos posicionales variables.",
        "**kwargs": "Argumentos nombrados variables.",
    },

    "Tipos básicos": {
        "str": "Texto.",
        "int": "Entero.",
        "float": "Decimal.",
        "bool": "True o False.",
        "list": "Lista mutable.",
        "tuple": "Tupla inmutable.",
        "dict": "Diccionario clave/valor.",
        "set": "Conjunto sin duplicados.",
        "None": "Ausencia de valor.",
    },

    "Built-ins": {
        "print()": "Imprime en consola.",
        "input()": "Lee texto del usuario.",
        "len()": "Devuelve longitud.",
        "type()": "Devuelve tipo del objeto.",
        "id()": "Devuelve identidad en memoria.",
        "isinstance()": "Verifica si un objeto es de cierto tipo.",
        "range()": "Genera secuencia numérica.",
        "enumerate()": "Devuelve índice y valor.",
        "zip()": "Une iterables en pares.",
        "sum()": "Suma valores.",
        "min() / max()": "Mínimo y máximo.",
        "sorted()": "Ordena y devuelve nueva lista.",
        "open()": "Abre archivos.",
        "dir()": "Lista atributos/métodos.",
        "help()": "Muestra ayuda.",
    },

    "Métodos str": {
        "upper()": "Convierte a mayúsculas.",
        "lower()": "Convierte a minúsculas.",
        "strip()": "Quita espacios al inicio y final.",
        "lstrip() / rstrip()": "Quita espacios a izquierda/derecha.",
        "replace()": "Reemplaza texto.",
        "split()": "Divide string en lista.",
        "join()": "Une elementos con un separador.",
        "find()": "Busca posición; retorna -1 si no encuentra.",
        "count()": "Cuenta ocurrencias.",
        "startswith()": "Verifica inicio.",
        "endswith()": "Verifica final.",
        "isdigit()": "True si todo son dígitos.",
        "isalpha()": "True si todo son letras.",
        "isalnum()": "True si todo es alfanumérico.",
        "format()": "Inserta valores en string.",
        "f-string": "Texto dinámico: f'Hola {nombre}'.",
    },

    "Métodos list": {
        "append()": "Agrega un elemento al final.",
        "extend()": "Agrega múltiples elementos.",
        "insert()": "Inserta en posición específica.",
        "remove()": "Elimina por valor.",
        "pop()": "Elimina y retorna elemento.",
        "clear()": "Vacía la lista.",
        "sort()": "Ordena la lista original.",
        "reverse()": "Invierte la lista original.",
        "copy()": "Copia superficial.",
    },

    "Métodos dict": {
        "keys()": "Devuelve claves.",
        "values()": "Devuelve valores.",
        "items()": "Devuelve pares clave/valor.",
        "get()": "Obtiene valor sin lanzar error.",
        "update()": "Actualiza el diccionario.",
        "pop()": "Elimina clave y retorna valor.",
        "clear()": "Vacía el diccionario.",
    },

    "Métodos set": {
        "add()": "Agrega elemento.",
        "remove()": "Elimina; falla si no existe.",
        "discard()": "Elimina; no falla si no existe.",
        "union()": "Une conjuntos.",
        "intersection()": "Elementos comunes.",
        "difference()": "Elementos que están en uno y no en otro.",
    },

    "Archivos": {
        "open(path, mode)": "Abre archivo.",
        "read()": "Lee contenido completo.",
        "readline()": "Lee una línea.",
        "readlines()": "Lee todas las líneas.",
        "write()": "Escribe texto.",
        "with open(...) as f": "Abre y cierra automáticamente.",
    },

    "Excepciones": {
        "try": "Bloque protegido.",
        "except": "Captura error.",
        "finally": "Siempre se ejecuta.",
        "else": "Se ejecuta si no hubo error.",
        "raise": "Lanza error manualmente.",
        "Exception": "Clase base común para errores.",
    },

    "OOP": {
        "class": "Define clase.",
        "__init__": "Constructor.",
        "self": "Referencia a la instancia.",
        "atributo": "Dato dentro de un objeto.",
        "método": "Función dentro de una clase.",
        "herencia": "Una clase deriva de otra.",
        "super()": "Accede a la clase padre.",
    },

    "Decoradores": {
        "@decorador": "Modifica una función o clase.",
        "funcion = decorador(funcion)": "Equivalente real del @.",
        "wrapper": "Función envolvedora.",
        "*args / **kwargs": "Permiten envolver funciones flexibles.",
        "closure": "Permite recordar variables externas.",
    },

    "Generadores": {
        "yield": "Produce un valor sin terminar la función.",
        "next()": "Pide el siguiente valor.",
        "iter()": "Obtiene iterador.",
        "generator expression": "(x for x in lista).",
    },

    "Context managers": {
        "with": "Administra entrada y salida de recursos.",
        "__enter__": "Se ejecuta al entrar al contexto.",
        "__exit__": "Se ejecuta al salir del contexto.",
        "uso típico": "Archivos, locks, conexiones.",
    },

    "Async / Await": {
        "async def": "Define función asíncrona.",
        "await": "Espera una operación asíncrona.",
        "coroutine": "Función async pendiente de ejecución.",
        "event loop": "Motor que coordina tareas async.",
    },

    "Patrones comunes": {
        "list comprehension": "[x for x in lista].",
        "dict comprehension": "{k: v for k, v in pares}.",
        "ternary": "x if condicion else y.",
        "unpacking": "a, b = valores.",
        "enumerate": "for i, valor in enumerate(lista).",
        "zip": "for a, b in zip(lista1, lista2).",
    },

    "Conceptos internos": {
        "objeto": "Todo valor en Python es un objeto.",
        "referencia": "Nombre que apunta a un objeto.",
        "scope": "Zona donde existe un nombre.",
        "frame": "Marco de ejecución de una función.",
        "stack": "Pila de llamadas activas.",
        "heap": "Memoria donde viven los objetos.",
        "mutable": "Objeto que puede cambiar.",
        "inmutable": "Objeto que no puede cambiar.",
        "closure": "Función que recuerda variables externas.",
    },
}


def titulo(texto):
    print()
    print("=" * 80)
    print(texto)
    print("=" * 80)


def mostrar_menu():
    titulo("ENCICLOPEDIA NAVEGABLE DEL LENGUAJE PYTHON")

    for numero, nombre in SECCIONES.items():
        print(f"{numero:>2}. {nombre}")

    print()
    print("B. Buscar término")
    print("K. Ver keywords reales de esta versión de Python")
    print("Q. Salir")


def mostrar_seccion(nombre_seccion):
    titulo(nombre_seccion)

    elementos = DATA[nombre_seccion]

    for clave, descripcion in elementos.items():
        print(f"{clave:<28} -> {descripcion}")


def buscar(termino):
    termino = termino.lower()
    encontrados = []

    for seccion, elementos in DATA.items():
        for clave, descripcion in elementos.items():
            texto = f"{clave} {descripcion}".lower()

            if termino in texto:
                encontrados.append((seccion, clave, descripcion))

    titulo(f"RESULTADOS PARA: {termino}")

    if not encontrados:
        print("No encontré coincidencias.")
        return

    for seccion, clave, descripcion in encontrados:
        print(f"[{seccion}] {clave:<24} -> {descripcion}")


def mostrar_keywords_reales():
    titulo("KEYWORDS REALES SEGÚN TU VERSIÓN DE PYTHON")

    for kw in keyword.kwlist:
        print(kw)

    print()
    print(f"Total: {len(keyword.kwlist)}")


def pausar():
    input("\nPresiona ENTER para continuar...")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip().lower()

        if opcion == "q":
            print("\nFin.")
            break

        elif opcion == "b":
            termino = input("Buscar: ").strip()
            buscar(termino)
            pausar()

        elif opcion == "k":
            mostrar_keywords_reales()
            pausar()

        elif opcion in SECCIONES:
            nombre_seccion = SECCIONES[opcion]
            mostrar_seccion(nombre_seccion)
            pausar()

        else:
            print("\nOpción inválida.")
            pausar()


if __name__ == "__main__":
    main()