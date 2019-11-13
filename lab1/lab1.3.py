#код потребує python3.8 або новіше
#виконав Хом'як Ігор
#this code requires python3.8 or newer to run
#It doesn't work with python3.7 or earlier versions because of assignment inside condition of if statement (line 11)
#written by Ihor Khomyak

import math

if x:=re.search("(-)?[1-9]\d*)?\d(\.\d+$)?(,\d+$)?", input("x= "))):
	if x.group(4):
		x = float(x.group(1)+x.group(2)) + float('0.' + x.group(4)[1:])
	else:
		x = float(x.group(0))

if x > -3:
    x = (x*x + 9) / (math.log(x+3))
else:
    x = 9 - 1.1*x - x*x
x = round(x, 14)
print("f(x) = ", x)
