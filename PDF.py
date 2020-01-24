from reportlab.platypus import (Table, SimpleDocTemplate, TableStyle, Image)
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
I= Image("C:/Users/Administrador/Desktop/Josh.jpg", width= 100, height= 100)

pdf= SimpleDocTemplate("Ejercicio .pdf", pagezise= letter)
t = Table([
    [I,'Joshua Roman Vazquez Benitez.',],
    ['Materia', 'Calificacion'],
    ['Geografia', 10],
    ['Estructura Socioeconomica de Mexico', 10],
    ['Produccion oral y escrita del ingles I', 'A'],
    ['Atencion y servicio al cliente', 10],
    ['Fundamentos de contabilidad industrial', 10],
    ['Ciencias de la salud I', 10],
    ['Psicologia I', 10],
    ['Matematicas financieras I', 10],
    ['Calculo  diferencial', 10,]
])
style = TableStyle ([
    ('FONTSIZE',(0 ,0),(-1,0),25), # Tamaño de Letra
    ('ALIGN', (0,0) ,(-1,-1),'CENTER'), # Alinear texto
    ('BOX', (-1,-1),(-1,-1), 2, colors.black), # Color de borde
    ('BOTTOMPADDING', (-1,0), (-1,0), 75), # Ajuste para letras maxusculas
    ('BOTTOMPADDING', (0,0), (0,0), 25),
    ('GRID', (0,1), (-1,-1), 2, colors.black),

])
t.setStyle(style)
story = []
story.append(t)
pdf.build(story)
