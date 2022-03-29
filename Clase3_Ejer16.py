from random import randint

def ppt(op):
    if op==1:
        r="piedra"
    elif op==2:
        r="papel"
    elif op==3:
        r="tijera"
    return r

ganadas=0
ganadasMaquina=0
while ganadas<3 and ganadasMaquina<3:
    opUsuario=int(input("Ingrese una opcion:\n1.-Piedra\n2.-Papel\n3.-Tijera\n"))
    opMaquina=randint(1,3)
    if opUsuario>3 or opMaquina<1:
        print("Ingrese una opcion valida")
        continue 
    print("El usuario eligio: ", ppt(opUsuario))
    print("La máquina eligio: ", ppt(opMaquina))
    if (opUsuario==1 and opMaquina==3)or(opUsuario==2 and opMaquina==1)or(opUsuario==3 and opMaquina==2):
        print("Gana el usuario")
        ganadas+=1
    elif opUsuario==opMaquina:
        print("Es un empate")
    else:
        print("Gana la máquina")
        ganadasMaquina+=1
    print("Ganadas Maquina: ",ganadasMaquina)
    print("Ganadas Usuario: ",ganadas,"\n")
