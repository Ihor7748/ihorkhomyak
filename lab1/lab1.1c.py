#код потребує python3.8 або новіше
#виконав Хом'як Ігор
#this code requires python3.8 or newer to run
#It doesn't work with python3.7 or earlier versions because of assignment inside condition of if statement (line 10)
#written by Ihor Khomyak

import re

a = input("a= ")
if re.search("-?([1-9]\d+)?\d(\.\d+$)?(,\d+$)?",a):
	if m:=re.search("(-?\d+),(\d+)",a):
		a = float(m.group(1)) + float("0."+ m.group(2))
	else:
		a = float(a)
	b= a * a
	b *= b
	b *= b
	b *= b
	b /= a
	print("a⁴= ", b)
else:
	print("  WRONG INPUT!\n It should be a real number")

