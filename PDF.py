from reportlab.pdfgen import canvas

j = canvas.Canvas("Ejercicio PDF.pdf")
j.drawString(100, 750, "Joshua Roman Vazquez Benitez")
j.save()