from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch




def makepdf(text, name):
    name = name.replace(" ", "_").lower()

    
    story = []
    text = text.replace("//", "<strong>")
    text = text.replace("*", "</strong>")


    # GIVE NAME FILE AND SET SIZE DOC
    doc = SimpleDocTemplate("certificado_" + name  +  ".pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
    #Darle stylos
    estilos = getSampleStyleSheet()
    estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    estilos.add(ParagraphStyle(name='center', fontName="Helvetica-Bold", fontSize=12, leftIndent=180))
    
    # Date today 
    
    today = datetime.now()
    today1 = "<strong>" + today.strftime('%d-%m-%Y') + "</strong>"
    #print(type(today1))
    story.append(Paragraph(today1, estilos["Normal"]))


    #  URL IMAGE AND SIZE 

    imagen = Image("img/logo.png", 1 * inch, 1 * inch, hAlign="RIGHT")
    story.append(imagen)
    

    #Title
    story.append(Paragraph('<h1><strong>CERTIFICADO LABORAL</strong></h1>', estilos["center"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(text, estilos["Justify"]))
        

    #Save
    doc.build(story)

if __name__ == "__main__":
    makepdf("//hola*", "nicoll")