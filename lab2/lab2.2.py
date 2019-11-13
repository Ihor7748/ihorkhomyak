#код потребує python3.8 або новіше
#виконав Хом'як Ігор
#this code requires python3.8 or newer to run
#It doesn't work with python3.7 or earlier versions because of assignment inside condition of if statement (line 9)
#written by Ihor Khomyak

import re

if n:=re.search("-?([1-9]\d*)?\d",input(" n= ")):
	n = int(n)
	a = 0
	k = 0

	while a <= n:
    		k += 1
    		a += k

	print("k =", k-1)
	print("сума =", a-k)
else:
	print("WRONG INPUT! It should be natural number")
