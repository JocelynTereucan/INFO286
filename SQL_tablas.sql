USE Covid19_Analysis2;

CREATE TABLE Dim_Region (
    Nombre_Region NVARCHAR(255) NOT NULL,
    Poblacion FLOAT,
	ID_Region INT PRIMARY KEY,
);

CREATE TABLE Dim_Tiempo (
    ID_Tiempo INT IDENTITY(1,1) PRIMARY KEY,
    Fecha DATE NOT NULL,
    Ano INT,
    Mes INT,
    Dia INT,
    Trimestre INT,
    Semana INT
);


CREATE TABLE Hechos_Covid (
    ID_Region INT,
    ID_Tiempo INT,
    Contagios FLOAT,
    Nuevos_Contagios FLOAT,
    Fallecidos FLOAT,
    Nuevos_Fallecidos FLOAT,
    Total_Tests FLOAT,
    Nuevos_Tests FLOAT,
    Camas_Ocupadas FLOAT,
    FOREIGN KEY (ID_Region) REFERENCES Dim_Region(ID_Region),
    FOREIGN KEY (ID_Tiempo) REFERENCES Dim_Tiempo(ID_Tiempo)
);
