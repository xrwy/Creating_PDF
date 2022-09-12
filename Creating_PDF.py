from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try:
        namePDF = input('PDF Name :')
        pdf = canvas.Canvas('{}.pdf'.format(namePDF))
        x = 720
        for nome, idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome, idade))

        pdf.setTitle(namePDF)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750,'Lista de Clientes')
        pdf.setFont('Helvetica-Oblique', 12)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print('{0}.pdf Successfull!'.format(namePDF))
    
    except:
        print('Error {0}.pdf'.format(namePDF))

lista = {'Felipe':'24','Jose':'42','Maria':'22','Eduardo':'31'}

GeneratePDF(lista)
