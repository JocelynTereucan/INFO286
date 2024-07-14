import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('path_to/owid-covid-data.csv')  # Ajusta 'path_to' a la ruta correcta

# Convertir la columna 'date' a datetime
df['date'] = pd.to_datetime(df['date'])

# Crear la tabla Dim_Region
dim_region = df[['location', 'population']].drop_duplicates().reset_index(drop=True)
dim_region['ID_Region'] = dim_region.index + 1
dim_region = dim_region.rename(columns={'location': 'Nombre_Region', 'population': 'Población'})

# Guardar en CSV para cargar en MySQL
dim_region.to_csv('data/Dim_Region.csv', index=False)

# Crear la tabla Dim_Tiempo
dim_tiempo = df[['date']].drop_duplicates().reset_index(drop=True)
dim_tiempo['ID_Tiempo'] = dim_tiempo.index + 1
dim_tiempo['Fecha'] = pd.to_datetime(dim_tiempo['date'])
dim_tiempo['Año'] = dim_tiempo['Fecha'].dt.year
dim_tiempo['Mes'] = dim_tiempo['Fecha'].dt.month
dim_tiempo['Día'] = dim_tiempo['Fecha'].dt.day
dim_tiempo['Trimestre'] = dim_tiempo['Fecha'].dt.quarter
dim_tiempo['Semana'] = dim_tiempo['Fecha'].dt.isocalendar().week
dim_tiempo = dim_tiempo.drop(columns=['date'])

# Guardar en CSV para cargar en MySQL
dim_tiempo.to_csv('data/Dim_Tiempo.csv', index=False)

# Merge para obtener los ID de región y tiempo
df = df.merge(dim_region, left_on='location', right_on='Nombre_Region', how='left')
df = df.merge(dim_tiempo, left_on='date', right_on='Fecha', how='left')

# Crear la tabla Hechos_Covid
hechos_covid = df[['ID_Region', 'ID_Tiempo', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests', 'new_tests']].rename(columns={
    'total_cases': 'Contagios',
    'new_cases': 'Nuevos_Contagios',
    'total_deaths': 'Fallecidos',
    'new_deaths': 'Nuevos_Fallecidos',
    'total_tests': 'Total_Tests',
    'new_tests': 'Nuevos_Tests'
})

# Añadir una columna de Camas_Ocupadas (opcional)
hechos_covid['Camas_Ocupadas'] = None  # Si no tienes estos datos, puedes dejarlos nulos

# Guardar en CSV para cargar en MySQL
hechos_covid.to_csv('data/Hechos_Covid.csv', index=False)
