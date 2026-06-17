-- Base de datos pequena de ejemplo para SQL Server.

CREATE DATABASE Escuela;
GO

USE Escuela;
GO

CREATE TABLE estudiantes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    curso VARCHAR(100) NOT NULL,
    nota DECIMAL(5,2) NOT NULL
);
GO

INSERT INTO estudiantes (nombre, edad, curso, nota)
VALUES
    ('Ana', 20, 'SQL Basico', 95.50),
    ('Luis', 22, 'Python', 88.00),
    ('Marta', 19, 'Bases de Datos', 91.25);
GO

SELECT * FROM estudiantes;
GO
