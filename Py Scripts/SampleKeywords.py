# Muestra todos los keywords de Python con una explicación breve en español

import keyword

explicaciones = {
    "False": "Valor booleano falso.",
    "None": "Representa ausencia de valor.",
    "True": "Valor booleano verdadero.",
    "and": "Operador lógico Y.",
    "as": "Asigna un alias en importaciones o excepciones.",
    "assert": "Verifica una condición; genera error si es falsa.",
    "async": "Define funciones o contextos asíncronos.",
    "await": "Espera el resultado de una operación asíncrona.",
    "break": "Sale inmediatamente de un bucle.",
    "case": "Caso dentro de un match.",
    "class": "Define una clase.",
    "continue": "Salta a la siguiente iteración del bucle.",
    "def": "Define una función.",
    "del": "Elimina una variable o elemento.",
    "elif": "Condición adicional en un if.",
    "else": "Bloque alternativo cuando no se cumple la condición.",
    "except": "Captura excepciones.",
    "finally": "Bloque que siempre se ejecuta al finalizar un try.",
    "for": "Bucle basado en iteración.",
    "from": "Importa elementos específicos de un módulo.",
    "global": "Declara una variable global.",
    "if": "Ejecuta código según una condición.",
    "import": "Importa módulos.",
    "in": "Verifica pertenencia o se usa en bucles.",
    "is": "Compara identidad de objetos.",
    "lambda": "Crea funciones anónimas.",
    "match": "Estructura de comparación de patrones.",
    "nonlocal": "Accede a variables de una función externa.",
    "not": "Operador lógico NO.",
    "or": "Operador lógico O.",
    "pass": "No hace nada; marcador de posición.",
    "raise": "Lanza una excepción.",
    "return": "Devuelve un valor desde una función.",
    "try": "Inicia manejo de excepciones.",
    "while": "Bucle basado en condición.",
    "with": "Gestiona recursos automáticamente.",
    "yield": "Devuelve valores gradualmente desde un generador."
}

print("=" * 20)
print("KEYWORDS DE PYTHON")
print("=" * 20)

for kw in keyword.kwlist:
    descripcion = explicaciones.get(kw, "Keyword reservada de Python.")
    print(f"{kw:<12} -> {descripcion}")

print("=" * 20)
print(f"Total de keywords: {len(keyword.kwlist)}")

ejemput = int(input("queloque"))