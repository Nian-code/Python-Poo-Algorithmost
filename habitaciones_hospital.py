import pandas as pd

df = pd.read_csv("entrada.csv")
print(df)
entrada = "h101c3"
# Este comando verifica que lineas contienen la entrada y retorna el indice
index_names = df[df["comando"].str.contains(entrada)].index
# Este comando los elimina del dataframe directamente con inplace los sobreescribe
df.drop(index_names, inplace = True) 
# Cambia el nombre de las columnas
df.columns = ["Señal", "Luegar", "Número", "Cama", "tipo de llamado", "Hora de inicio"]
print(df)