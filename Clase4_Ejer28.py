dic={}

# indice="nombre"
# valor="Veronica"

#de las dos maneras funciona...
# dic[indice]=valor
#dic.setdefault(indice,valor)

menu=True
while menu:
    op=int(input("Elija una opcion\n1.-Agregar\n2.-Salir\n"))
    if op==1:
        indice=input("Ingrese el indice: ")
        valor=input("Ingrese el valor: ")
        dic[indice]=valor
        print(dic)
    elif op==2:
        menu=False
    else:
        print("Ingrese una opcon valida")
# print(type(dic))

