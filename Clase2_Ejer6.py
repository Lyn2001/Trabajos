sexo="f"
edad=59
cotizaciones=800
aniosServ=26

if aniosServ>=25 and cotizaciones>=750:
    if (sexo=="m" and edad >=60) or (sexo=="f" and edad >=55):
        print("Usted aplica para ser jubilado")
    else:
        print("Usted no aplica pa ser jubilado")
else:
    print("Usted no aplica para ser jubilado")

    
