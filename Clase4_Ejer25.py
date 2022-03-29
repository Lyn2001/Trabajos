def imprimir (tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print(" ]")

def asteriscos(tabla,simbolo):
    if len(tabla)%2==0:
        print("La longitud debe de ser impar")
    else:
        for i in range(len(tabla)):
            for j in range(len(tabla)):
                if i==len(tabla)//2 or j==len(tabla)//2 or i==j or i+j==len(tabla)-1:
                    tabla[i][j]=simbolo


def llenarVacio(n):
    tabla=[]
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[" "]
    return tabla

tabla=llenarVacio(8)
#imprimir(tabla)
asteriscos(tabla,"*")
imprimir(tabla)