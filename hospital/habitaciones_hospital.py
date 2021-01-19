import pandas as pd

df = pd.read_csv("entrada.csv")
print(df)
entrada = "h101c3"
# Este comando verifica que lineas contienen la entrada y retorna el indice
index_names = df[df["comando"].str.contains(entrada)].index
# Este comando los elimina del dataframe directamente con inplace los sobreescribe
df.drop(index_names, inplace = True) 
# Cambia el nombre de las columnas
df.columns = ["Señal", "Luegar", "Número", "Cama", "Tipo de llamado", "Hora de inicio"]
print(df)

#convierte el data frame en una tabla html
tabla_html = df.to_html()

text_file = open("index.html", "w")
text_file.write('<link href="./css/index.css" rel="stylesheet">')
text_file.write("<main>")
text_file.write('<section class="title">')
text_file.write("<h1> Digiturnos hospital </h1>")
text_file.write('<img src = "https://image.flaticon.com/icons/png/512/33/33777.png">')
text_file.write("</section>")
text_file.write(tabla_html)
text_file.write("</main>")
text_file.close()