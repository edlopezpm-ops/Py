# enciclopedia_sql.py

SECCIONES = {
    "1": "Comandos principales",
    "2": "Cláusulas",
    "3": "Joins",
    "4": "Operadores",
    "5": "Funciones agregadas",
    "6": "Funciones de texto",
    "7": "Funciones de fecha",
    "8": "Tipos de datos",
    "9": "DDL",
    "10": "DML",
    "11": "Constraints",
    "12": "Índices",
    "13": "Transacciones",
    "14": "Errores TRY CATCH",
    "15": "Stored procedures",
    "16": "Variables y tablas temporales",
    "17": "Window functions",
    "18": "Conceptos internos",
}


DATA = {
    "Comandos principales": {
        "SELECT": "Consulta datos.",
        "INSERT": "Inserta filas.",
        "UPDATE": "Actualiza filas existentes.",
        "DELETE": "Elimina filas.",
        "MERGE": "Inserta, actualiza o elimina según coincidencias.",
        "CREATE": "Crea objetos.",
        "ALTER": "Modifica objetos.",
        "DROP": "Elimina objetos.",
        "TRUNCATE": "Vacía una tabla rápidamente.",
        "EXEC": "Ejecuta stored procedures o SQL dinámico.",
    },

    "Cláusulas": {
        "FROM": "Indica la tabla fuente.",
        "WHERE": "Filtra filas antes de agrupar.",
        "GROUP BY": "Agrupa filas.",
        "HAVING": "Filtra después de agrupar.",
        "ORDER BY": "Ordena resultados.",
        "TOP": "Limita cantidad de filas en SQL Server.",
        "DISTINCT": "Elimina duplicados del resultado.",
        "OFFSET / FETCH": "Paginación.",
        "INTO": "Crea tabla desde un SELECT.",
    },

    "Joins": {
        "INNER JOIN": "Sólo coincidencias entre tablas.",
        "LEFT JOIN": "Todo de la izquierda + coincidencias.",
        "RIGHT JOIN": "Todo de la derecha + coincidencias.",
        "FULL OUTER JOIN": "Todo de ambas tablas.",
        "CROSS JOIN": "Producto cartesiano.",
        "SELF JOIN": "Una tabla unida consigo misma.",
        "APPLY": "Ejecuta expresión por cada fila.",
        "CROSS APPLY": "Como INNER JOIN lateral.",
        "OUTER APPLY": "Como LEFT JOIN lateral.",
    },

    "Operadores": {
        "=": "Igualdad.",
        "<> / !=": "Diferente.",
        "> / < / >= / <=": "Comparaciones.",
        "AND": "Ambas condiciones deben cumplirse.",
        "OR": "Al menos una condición debe cumplirse.",
        "NOT": "Niega condición.",
        "IN": "Coincide contra una lista.",
        "NOT IN": "No coincide contra una lista.",
        "BETWEEN": "Rango inclusivo.",
        "LIKE": "Comparación por patrón.",
        "IS NULL": "Evalúa valores NULL.",
        "IS NOT NULL": "Evalúa valores no NULL.",
        "+": "Suma o concatenación en SQL Server.",
    },

    "Funciones agregadas": {
        "COUNT()": "Cuenta filas o valores.",
        "SUM()": "Suma valores.",
        "AVG()": "Promedio.",
        "MIN()": "Valor mínimo.",
        "MAX()": "Valor máximo.",
        "COUNT(DISTINCT)": "Cuenta valores únicos.",
        "STRING_AGG()": "Concatena valores agrupados.",
    },

    "Funciones de texto": {
        "LEN()": "Longitud del texto.",
        "LEFT()": "Extrae caracteres desde la izquierda.",
        "RIGHT()": "Extrae caracteres desde la derecha.",
        "SUBSTRING()": "Extrae parte del texto.",
        "CHARINDEX()": "Busca posición de texto.",
        "REPLACE()": "Reemplaza texto.",
        "UPPER()": "Convierte a mayúsculas.",
        "LOWER()": "Convierte a minúsculas.",
        "LTRIM()": "Quita espacios a la izquierda.",
        "RTRIM()": "Quita espacios a la derecha.",
        "TRIM()": "Quita espacios al inicio y final.",
        "CONCAT()": "Concatena valores.",
        "FORMAT()": "Formatea valores como texto.",
    },

    "Funciones de fecha": {
        "GETDATE()": "Fecha/hora actual.",
        "SYSDATETIME()": "Fecha/hora actual con más precisión.",
        "DATEADD()": "Suma/resta unidades de tiempo.",
        "DATEDIFF()": "Diferencia entre fechas.",
        "DATEPART()": "Extrae parte de fecha.",
        "YEAR()": "Extrae año.",
        "MONTH()": "Extrae mes.",
        "DAY()": "Extrae día.",
        "EOMONTH()": "Último día del mes.",
        "CAST()": "Convierte tipo de dato.",
        "CONVERT()": "Convierte tipo con formato opcional.",
    },

    "Tipos de datos": {
        "INT": "Entero.",
        "BIGINT": "Entero grande.",
        "DECIMAL(p,s)": "Número exacto con precisión y escala.",
        "FLOAT": "Número aproximado.",
        "BIT": "0, 1 o NULL.",
        "VARCHAR(n)": "Texto no Unicode.",
        "NVARCHAR(n)": "Texto Unicode.",
        "CHAR(n)": "Texto fijo.",
        "DATE": "Sólo fecha.",
        "DATETIME": "Fecha y hora.",
        "DATETIME2": "Fecha y hora con mayor precisión.",
        "UNIQUEIDENTIFIER": "GUID.",
    },

    "DDL": {
        "CREATE TABLE": "Crea tabla.",
        "ALTER TABLE": "Modifica tabla.",
        "DROP TABLE": "Elimina tabla.",
        "CREATE VIEW": "Crea vista.",
        "CREATE PROCEDURE": "Crea stored procedure.",
        "CREATE INDEX": "Crea índice.",
        "DROP INDEX": "Elimina índice.",
    },

    "DML": {
        "INSERT INTO": "Inserta datos.",
        "UPDATE": "Actualiza datos.",
        "DELETE": "Elimina filas.",
        "MERGE": "Upsert / sincronización.",
        "SELECT INTO": "Crea tabla desde resultado.",
        "BULK INSERT": "Carga masiva de archivo.",
    },

    "Constraints": {
        "PRIMARY KEY": "Identifica filas de forma única.",
        "FOREIGN KEY": "Relaciona tablas.",
        "UNIQUE": "Evita duplicados.",
        "NOT NULL": "Obliga valor.",
        "CHECK": "Valida condición.",
        "DEFAULT": "Valor por defecto.",
    },

    "Índices": {
        "CLUSTERED INDEX": "Orden físico/lógico principal de la tabla.",
        "NONCLUSTERED INDEX": "Estructura secundaria para búsqueda.",
        "INCLUDE": "Columnas adicionales en índice.",
        "SEEK": "Búsqueda eficiente por índice.",
        "SCAN": "Lectura amplia de filas/páginas.",
        "FRAGMENTATION": "Desorden interno del índice.",
        "STATISTICS": "Datos que usa el optimizador.",
    },

    "Transacciones": {
        "BEGIN TRAN": "Inicia transacción.",
        "COMMIT": "Confirma cambios.",
        "ROLLBACK": "Revierte cambios.",
        "@@TRANCOUNT": "Cantidad de transacciones activas.",
        "XACT_STATE()": "Estado de la transacción.",
        "SAVE TRAN": "Punto de guardado.",
    },

    "Errores TRY CATCH": {
        "TRY": "Bloque protegido.",
        "CATCH": "Captura error.",
        "ERROR_MESSAGE()": "Mensaje del error.",
        "ERROR_NUMBER()": "Número del error.",
        "ERROR_LINE()": "Línea del error.",
        "THROW": "Relanza error moderno.",
        "RAISERROR": "Lanza error estilo anterior.",
    },

    "Stored procedures": {
        "CREATE PROCEDURE": "Crea procedimiento.",
        "ALTER PROCEDURE": "Modifica procedimiento.",
        "EXEC procedure": "Ejecuta procedimiento.",
        "@param": "Parámetro.",
        "OUTPUT": "Parámetro de salida.",
        "RETURN": "Código de retorno.",
        "SET NOCOUNT ON": "Evita mensajes de filas afectadas.",
    },

    "Variables y tablas temporales": {
        "DECLARE": "Declara variable.",
        "SET": "Asigna valor.",
        "SELECT @var =": "Asigna desde consulta.",
        "#temp": "Tabla temporal local.",
        "##temp": "Tabla temporal global.",
        "@table": "Variable de tabla.",
        "IF OBJECT_ID('tempdb..#t')": "Verifica si existe una temp table.",
    },

    "Window functions": {
        "OVER()": "Define ventana de cálculo.",
        "PARTITION BY": "Divide grupos dentro de ventana.",
        "ORDER BY": "Orden dentro de ventana.",
        "ROW_NUMBER()": "Número secuencial.",
        "RANK()": "Ranking con saltos.",
        "DENSE_RANK()": "Ranking sin saltos.",
        "LAG()": "Valor de fila anterior.",
        "LEAD()": "Valor de fila siguiente.",
        "SUM() OVER": "Suma analítica.",
    },

    "Conceptos internos": {
        "NULL": "Valor desconocido/ausente, no igual a cero ni string vacío.",
        "SARGable": "Condición que puede usar índice eficientemente.",
        "Execution Plan": "Plan elegido por el optimizador.",
        "Cardinality": "Estimación de cantidad de filas.",
        "Lock": "Bloqueo para controlar concurrencia.",
        "Deadlock": "Dos sesiones bloqueándose mutuamente.",
        "Isolation Level": "Nivel de visibilidad entre transacciones.",
        "TempDB": "Base temporal usada para #temp, sorts, hashes, versiones.",
    },
}


def titulo(texto):
    print()
    print("=" * 80)
    print(texto)
    print("=" * 80)


def mostrar_menu():
    titulo("ENCICLOPEDIA NAVEGABLE DE SQL")

    for numero, nombre in SECCIONES.items():
        print(f"{numero:>2}. {nombre}")

    print()
    print("B. Buscar término")
    print("Q. Salir")


def mostrar_seccion(nombre_seccion):
    titulo(nombre_seccion)

    elementos = DATA[nombre_seccion]

    for clave, descripcion in elementos.items():
        print(f"{clave:<30} -> {descripcion}")


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
        print(f"[{seccion}] {clave:<26} -> {descripcion}")


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

        elif opcion in SECCIONES:
            mostrar_seccion(SECCIONES[opcion])
            pausar()

        else:
            print("\nOpción inválida.")
            pausar()


if __name__ == "__main__":
    main()