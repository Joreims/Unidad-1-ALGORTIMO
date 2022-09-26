#Disminuir un numero hasta cero
def disminuir(num):
    if(num==0): print(0)
    else: 
        print(num)
        disminuir(num-1)

num = int(input("Dime un # "))
disminuir(num)