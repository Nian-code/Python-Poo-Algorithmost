class persona():

    def __init__(self, nombre, cc, departamento, inicio, final, tipo_de_contrato,
                cargo, salario):
        self.nombre = nombre
        self.cc = cc
        self.departamento = departamento
        self.inicio = inicio
        self.final  = final
        self.tipo_de_contrato = tipo_de_contrato
        self.cargo = cargo
        self.salario = salario
 
def certificado(persona):
    print("""
            CERTIFICA

            Que el (la) señor (a) {}, colombiano, 
            identificado (a) con la cédula de ciudadanía No. {} y 
            residente en {}, labora (ó) para esta empresa desde año {} hasta {}, 
            con un contrato {}, desempeñando el cargo de: {}. 
            Durante este tiempo, la persona ha devengado un salario mensual de: {}.
    """.format(persona.nombre, persona.cc, persona.departamento,
              persona.inicio, persona.final, persona.tipo_de_contrato, persona.cargo, persona.salario))
    

if __name__ == "__main__":
    persona1  = persona("nicoll", 123, "Tunja", 2019, 2020, "de aprendizaje", "Aprendiz", "1 salario mínimo vigente")
    persona2  = persona("jesus", 451, "Meta", 2018, 2020, "Por servicios", "instalador de CCTV", "a convenir")
    persona3  = persona("daniel", 321, "Tunja", 2016, 2020, "indefinido", "Contador", "1 salario mínimo vigente")
    certificado(persona1)
    certificado(persona2)
    certificado(persona3)


