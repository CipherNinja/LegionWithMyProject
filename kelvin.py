#-----------------------------------------------------------------------------------------|
#                                           /\                                            |     
#                                          /  \                                           |
#                                         /    \                                          |
#                                        /      \                                         |
#                                       /        \                                        |
#                                      /          \                                       |
#                                     /            \                                      |
#-------------------------------------|-------------|-------------------------------------|
#C = K - 273.15                       |_____________| ****Created by >>> Priyesh Pandey   |
#K = C + 273.15                       |_____________| *Language Used >>> Python           |
#1kelvin = -272.15 celcius            |             |        **Dated >>> February 13 2022 |
#-------------------------------------|-------------|-------------------------------------|

def name (k):
	formulae = k - 273.15
	print("your answer in celcius is :--> ",round(formulae,3),"~ celcius")
kelvin =input("Your Value In kelvin :--> ")
kelvin = int(kelvin)
if kelvin == "a":
	print("your command 'a' is not available due to security regions")
if kelvin == "b":
	print("your command 'b' is not available due to security regions")
if kelvin == "c":
	print("your command 'c' is not available due to security regions")
if kelvin == "d":
	print("your command 'd' is not available due to security regions")
if kelvin == "e":
	print("your command 'e' is not available due to security regions")
if kelvin == "f":
	print("your command 'f' is not available due to security regions")
name (kelvin)




def name (c):
	formulae = c + 273.15
	print("your answer in kelvin is :--> ",round(formulae,3),"~ kelvin")
celcius = int(input("Your Value In Celcius :--> "))
name (celcius)
