#!/usr/bin/python

n=int(input("How many number? : "))
i=0
num=0
while i < n:
    num+=float(input("Enter Number : "))
    i+=1

avg=num/float(n)
print (avg)
