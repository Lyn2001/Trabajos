jornada =48
hTrabajadas=48
pagoHora=2
pagoExtra=3.5

if hTrabajadas<=jornada:
    salario=hTrabajadas*pagoHora
else:
    salario=(jornada*pagoHora)+((hTrabajadas-jornada)*pagoExtra)

print("Su pago total es de: ",salario)