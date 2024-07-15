USE Covid19_Analysis2;

-- Verificar datos en Dim_Region
SELECT TOP 10 * FROM Dim_Region;

-- Verificar datos en Dim_Tiempo
SELECT TOP 10 * FROM Dim_Tiempo;

-- Verificar datos en Hechos_Covid
SELECT TOP 1500 * FROM Hechos_Covid;
