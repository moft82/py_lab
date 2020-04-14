#!/usr/bin/python

n=int(input("Fobonacci number : "))
i=2
F1=F2=1
if n == 1:
    print(F1)
    print("F1 : {}" .format(F1))
elif n==2:
    print(F1, F2)
    print("F2 : {}" .format(F2))
else :
    print("{}, {}".format(F1,F2), end=''),
    while i < n :
        temp=F1
        F1=F2
        F2=temp+F1
        print(", {}".format(F2), end='')
        i+=1
    
    print("\nF{} : {}".format(n,F2))
