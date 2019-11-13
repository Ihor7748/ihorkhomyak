#код потребує python3.8 або новіше
#виконав Хом'як Ігор
#this code requires python3.8 or newer to run
#It doesn't work with python3.7 or earlier versions because of assignment inside condition of if statement (line 10)
#written by Ihor Khomyak

import re

y = 0
if n:=re.search("-?([1-9]\d*)?\d",input("n= ")) and (x:=re.search("(-)?([1-9]\d*)?\d(\.\d+$)?(,\d+$)?", input("x= "))):
	if x.group(4):
		x = float(x.group(1)+x.group(2)) + float('0.' + x.group(4)[1:])
	else:
		x = float(x.group(0))
	n = int(n.group(0))

	for i in range(1, n):
		y += (2*(x**i) - 1)/(n-1)
	y = round(y, 2)
	print(y)
else:
	print("WRONG INPUT! \n x -should real number, n -should be an natural number")
