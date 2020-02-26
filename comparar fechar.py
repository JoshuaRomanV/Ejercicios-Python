from datetime import date
from dateutil import relativedelta

Primer_fecha = date(1, 2, 16)

Segunda_fecha = date(2020, 1, 1)

diferencia = relativedelta.relativedelta(Primer_fecha, Segunda_fecha)

año = diferencia.years
mes = diferencia.months
dia = diferencia.days

print(f"La diferencia es {año} año(s), {mes} mes(es) , {dia} dia(s)")