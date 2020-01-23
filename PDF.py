from reportlab.pdfgen import canvas

j = canvas.Canvas("Ejercicio PDF.pdf")
j.setFont('Helvetica', 20)
j.drawString(180, 750, "Joshua Roman Vazquez Benitez",)
j.drawImage("C:/Users/Administrador/Desktop/Josh.jpg", 70, 700, 70, 80, )
j.showPage()
j.save()