import datetime

ano = '2007'
mes = '02'
dia = '28'

try:
    datetime.datetime(year=int(ano), month=int(mes), day=int(dia))
except ValueError:
    print("Rapaz")

