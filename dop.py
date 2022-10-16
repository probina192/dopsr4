from random import randint
arr=[]
arrSize=int(input("Введите размерность массива: "))
f=input("Хотите ввести элемента массива? y/n ")
if (f=="y"):
    for i in range (arrSize):
        arr.append (int(input()))
elif (f=="n"):
    for i in range (arrSize):
        arr.append (randint(0,10))
else:
    print ("Ошибка")
    exit ()
arrmin=min(arr)
print ("Входной массив")
print (arr)
delta=int(input("Введите дельта "))
res=0 #количество элементов которые отличаются на дельта от минимального
for i in range (arrSize):
    if (arr[i]-arrmin==delta):
        res+=1
print ("Результат")
print (res)