import pandas as pd

 

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

 

# Leer CSV desde la URL

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

 


data = data.drop(columns=['columna_a_eliminar'])

# 2. Tratar valores faltantes (rellena los valores faltantes con un valor específico, por ejemplo, 0)
data = data.fillna(0)

# 3. Cambiar tipos de datos (sustituye 'nombre_columna' por el nombre de la columna y 'nuevo_tipo' por el tipo de datos deseado)
data['nombre_columna'] = data['nombre_columna'].astype('nuevo_tipo')

# 4. Renombrar columnas (sustituye 'nombre_antiguo' por el nombre antiguo y 'nombre_nuevo' por el nuevo nombre)
data = data.rename(columns={'nombre_antiguo': 'nombre_nuevo'})

# 5. Eliminar duplicados
data = data.drop_duplicates()

# Mostrar las primeras filas para visualizar los datos limpios
print(data.head())



