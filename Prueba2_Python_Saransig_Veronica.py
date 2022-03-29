num=100
# r=("FizzBuzz")
# re=("Fizz")
# res=("Buzz")
for i in range(1,num+1,1):
    if i%3==0 and i%5==0:
        print (i, "FizzBuzz")
        #r = str(i) + " "+ r 
    elif(i%3==0):
        print(i,"Fizz")
        #re = str(i) +" " + re 
    elif(i%5==0):
        print(i, "Buzz")
        #res = str(i) +" "+ res 
# print(r)    
# print(re)
# print(res)