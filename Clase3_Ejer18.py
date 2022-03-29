from random import randint

v=True
aciertos=0
while v:
    op=randint(1,4)
    num1=randint(1,10)
    num2=randint(1,10)  
    if op==1:
        res=num1*num2
        print(num1,"*",num2,"=")
        resUsuario= int(input("Ingrese su respuesta: "))
        if resUsuario==res:
            print("Correcto")
            aciertos+=1
        else:
            print("Incorrecto, la respuesta era: ",res)
            v=False
    elif op==2:
        res=num1//num2
        print(num1,"/",num2,"=")
        resUsuario= int(input("Ingrese su respuesta: "))
        if resUsuario==res:
            print("Correcto")
            aciertos+=1
        else:
            print("Incorrecto, la respuesta correcta era: ",res)
            v=False
    elif op==3:
        res=num1-num2
        print(num1,"-",num2,"=")
        resUsuario= int(input("Ingrese su respuesta: "))
        if resUsuario==res:
            print("Correcto")
            aciertos+=1
        else:
            print("Incorrecto, la respuesta correcta era: ",res)
            v=False
    elif op==4:
        res=num1+num2
        print(num1,"+",num2,"=")
        resUsuario= int(input("Ingrese su respuesta: "))
        if resUsuario==res:
            print("Correcto")
            aciertos+=1
        else:
            print("Incorrecto, la respuesta correcta era: ",res)
            v=False
print("Obtuvo un total de aciertos de: ",aciertos)