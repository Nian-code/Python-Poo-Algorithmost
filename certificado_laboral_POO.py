import makepdf

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

        text = """Que el(la) señor(a) //{}*, colombiano, identificado(a) con la cédula 
        de ciudadanía No //{}* y residente en //{}*, labora(ó) para esta empresa 
        desde año //{}* hasta //{}*, con un contrato //{}*, desempeñando el 
        cargo de: //{}*.Durante este tiempo, la persona ha devengado un 
        salario mensual de: //{}*.""".format(persona.nombre, persona.cc, persona.departamento,
                persona.inicio, persona.final, persona.tipo_de_contrato, persona.cargo, persona.salario)
        
        makepdf.makepdf(text, persona.nombre)
    

if __name__ == "__main__":

        nombre = str(input("¿Cuál es tu nombre?: "))
        departamento =  str(input("¿De qué departamento eres?: "))
        cc =  str(input("¿Cuál es tu número de cc?: "))
        fecha_inicio =  str(input("¿Cuál es la fecha inicial de contrato?: "))
        fecha_final  =  str(input("¿Cuál es la fecha final del contrato?: "))
        tipo_de_contrato = str(input("¿Cuál es tu tipo de contrato?: "))
        cargo = str(input("¿Cuál es tu cargo?: "))
        salario =  str(input("¿Cuál es tu salario?: "))

        persona1  = persona(nombre, cc, departamento, fecha_inicio, fecha_final, 
                        tipo_de_contrato,cargo, salario)

        certificado(persona1)



