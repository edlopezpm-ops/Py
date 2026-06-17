/*
    Script objetivo:
    1. Revisar si existe la base de datos PYDB.
       - Si no existe, crearla.
       - Si existe, no hacer nada.

    2. Entrar a PYDB.

    3. Revisar si existe la tabla dbo.REGISTER.
       - Si no existe, crearla.
       - Si existe, no hacer nada.

    4. Revisar si la tabla tiene datos.
       - Si está vacía, insertar 2 registros.
       - Si ya tiene datos, no insertar nada.
*/


/*=========================================================
  1. CREAR BASE DE DATOS SI NO EXISTE
=========================================================*/

IF NOT EXISTS
(
    SELECT 1
    FROM sys.databases
    WHERE name = 'PYDB'
)
BEGIN
    -- Si PYDB no existe, se crea la base de datos.
    CREATE DATABASE PYDB;
END;
GO


/*=========================================================
  2. CAMBIAR EL CONTEXTO A LA BASE PYDB
=========================================================*/

-- Todo lo que venga después corre dentro de PYDB.
USE PYDB;
GO


/*=========================================================
  3. CREAR TABLA SI NO EXISTE
=========================================================*/

IF NOT EXISTS
(
    SELECT 1
    FROM sys.tables t
    INNER JOIN sys.schemas s
        ON t.schema_id = s.schema_id
    WHERE t.name = 'REGISTER'
      AND s.name = 'dbo'
)
BEGIN
    -- Si la tabla dbo.REGISTER no existe, se crea.
    CREATE TABLE dbo.REGISTER
    (
        INTERNAL_NUM INT IDENTITY(1,1) NOT NULL,
        SCRIPT_NAME       NVARCHAR(50) NOT NULL,
        SCRIPT_TYPE       NVARCHAR(10) NOT NULL,
        ACTIVE            NVARCHAR(1) NOT NULL,
        USER_STAMP        NVARCHAR(50) NULL,
        PROCESS_STAMP     NVARCHAR(50) NULL,
        DATE_TIME_STAMP   DATETIME NOT NULL
    );
END;
GO


/*=========================================================
  4. INSERTAR DATOS SÓLO SI LA TABLA ESTÁ VACÍA
=========================================================*/

IF NOT EXISTS
(
    SELECT 1
    FROM dbo.REGISTER
)
BEGIN
    -- Si la tabla está vacía, insertar datos iniciales.
    INSERT INTO dbo.REGISTER
    (
        SCRIPT_NAME,
        SCRIPT_TYPE,
        ACTIVE,
        USER_STAMP,
        PROCESS_STAMP,
        DATE_TIME_STAMP
    )
    VALUES
    (
        'HolaMundo',
        'PY',
        'Y',
        'ED',
        'INITIAL_LOAD',
        GETDATE()
    ),
    (
        'HelloWordOverEng',
        'PY',
        'Y',
        'ED',
        'INITIAL_LOAD',
        GETDATE()
    ),
    (
        'SampleKeywords',
        'PY',
        'Y',
        'ED',
        'INITIAL_LOAD',
        GETDATE()
    ),
    (
        'MasterPyKWs',
        'PY',
        'Y',
        'ED',
        'INITIAL_LOAD',
        GETDATE()
    ),
    (
        'T1',
        'SQL',
        'Y',
        'ED',
        'INITIAL_LOAD',
        GETDATE()
    ),
    (
        'CVS DropDown Inverview',
        'HTML5',
        'Y',
        'ED',
        'INITIAL_LOAD',
        GETDATE()
    );
END;
GO


/*=========================================================
  5. VALIDAR RESULTADO FINAL
=========================================================*/

-- Mostrar los datos actuales de la tabla.
SELECT *
FROM dbo.REGISTER;
GO