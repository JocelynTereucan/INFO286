USE Covid19_Analysis2;

BULK INSERT Dim_Region
FROM 'C:\Users\tereu\OneDrive\Escritorio\UACH\1-2024\Info286\data\Dim_Region.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK
);

BULK INSERT Dim_Tiempo
FROM 'C:\Users\tereu\OneDrive\Escritorio\UACH\1-2024\Info286\data\Dim_Tiempo.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK
);

BULK INSERT Hechos_Covid
FROM 'C:\Users\tereu\OneDrive\Escritorio\UACH\1-2024\Info286\data\Hechos_Covid.csv'
WITH (
	FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK

);
