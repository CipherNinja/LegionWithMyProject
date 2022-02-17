#formulae C = (f-32)*(5/9)
def name (f):
	celcious = (f-32)*(5/9)
	print ("your answer in celcius is :: ", round(celcious,3),"celcious")

i = float(input("ENTRE YOUR VALUE IN FAHRENHITE :: "))
name(i)

def callme (c):
	FAHRENHITE = c*9/5 + 32
	print("your answer in FAHRENHITE is :: ", round(FAHRENHITE,3),"FAHRENHITE")

j = float(input("ENTRE YOUR VALUE IN celcious"))
callme(j) 