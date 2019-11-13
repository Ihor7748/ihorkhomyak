#код потребує python3.8 або новіше
#виконав Хом'як Ігор
#this code requires python3.8 or newer to run
#It doesn't work with python3.7 or earlier versions because of assignment inside condition of if statement (line 9)
#written by Ihor Khomyak

import re

for x in [a:=input("a= "), b:=input("b= "), c:=input("c= "), d:=input("d= ")]:
	if x:=re.search("(-)?([1-9]\d*)?\d(\.\d+$)?(,\d+$)?", input("x= ")):
		if x.group(4):
			x = float(x.group(1)+x.group(2)) + float('0.' + x.group(4)[1:])
		else:
			x = float(x.group(0))
	else:
		print("  WRONG INPUT!\n a,b,c,d - should be a real number")
		exit()


if a == d:
    print("a=d= ", a)
elif b == d:
    print("b=d= ", b)
elif c == d:
    print("c=d= ", c)
else:
    a = d-a
    b = d-b
    c = d-c
    if a > b:
        if a > c:
            print("max(d-a,d-b,d-c)=d-a= ", a)
        elif a == c:
            print("max(d-a,d-b,d-c)=d-a=d-c= ", a)
        else:
            print("max(d-a,d-b,d-c)=d-c= ", c)
    elif a == b:
        if a > c:
            print("max(d-a,d-b,d-c)=d-a=d-b= ", a)
        elif a == c:
            print("max(d-a,d-b,d-c)=d-a=d-b=d-c= ", a)
        else:
            print("max(d-a,d-b,d-c)=d-c= ", c)
    else:
        if b > c:
            print("max(d-a,d-b,d-c)=d-b= ", b)
        elif b == c:
            print("max(d-a,d-b,d-c)=d-b=d-c= ", b)
        else:
            print("d-c= ", c)
