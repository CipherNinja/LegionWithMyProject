class calculator:
	def __init__(self,add1:int,add2:int,subtract1:int,subtract2:int):
		self.add1 = sum(add1) + sum(add2)
		self.subtract1 = sum(subtract1)-sum(subtract2)
	def ADDITON_SUBTRACTION(self):
		try:
			i = input('\nChose " + " for ADDITION and " - " for SUBTRACTION : ')
			if i == "+":
				return '\nADDITION : ',self.add1
			elif i == "-":
				return '\nSUBTRACTION : ',self.subtract1

		except Exception as e:
			return '\n HEY CHECK IF YOU HAVE GIVEN WRONG OPERATOR',e
		else:
			print('\n THANKS FOR CHOSING US ')

try:
	vid = calculator([22,33],[43.423],[122,123],[123,123])
	hey = vid.ADDITON_SUBTRACTION()
	print(hey)
except Exception as e:
	print('\n You got this error : ',e)
else:
	print('\nWORKING')

class multiply_and_divide:
	try:
		def __init__(self, arg1:int, arg2:int):
			self.arg1 = arg1 * arg2
			self.arg2 =  arg1 / arg2
		def multiply_divide(self):
			try:
				i = input('\nChose * for multiplication and / for division : ')
				i = str(i)
				if i == '*':
					return '\nMULTIPLICATION : ', self.arg1
				elif i == "/":
					return '\nDVISION : ',self.arg2

			except Exception as e:
				print('\nCheck if OPERATOR is not a integer/float ')
			else:
				return '\nTHANKS FOR CHOSING US '
	except Exception as e:
		print('\nYou Have Give a WRONG input : '," PLEASE GIVE INTEGER AS input")
	else:
		print('\nTHANKS for CHOSING us ! ')

try:
	vid = multiply_and_divide(3,3)
	hey = vid.multiply_divide()
	print(hey)
except Exception as e:
	print('\n You got this error : ')
else:
	print('\nWORKING')

import math as c
class square_root_and_powers:
	try:
		def __init__(self,demand,arg,arg2,raised):
			self.demand = demand
			self.arg = c.sqrt(arg)  #--------demanding integer is 1
			self.arg2 = c.pow(arg2,raised) #---------demanding integer is 2
		def engine(self):
			if self.demand == 1:
				return self.arg ,' root'
			elif self.demand == 2:
				return self.arg2 , ' power'
			else:
				print('seems like a wrong input is GIVEN')
	except Exception as e:
		print('\n CHECK IF YOU HAVE GIVEN WRONG input ALWAYS USE INTEGER : ')
		print('\n Your error is ', e)
	else:
		print('THANKS FOR USING THIS PROGRAMME')

try:
	print('program to find square_root_and_powers ')
	i_want = int(input('\n ENTER 1 FOR SQUARE_ROOT AND 2 FOR POWER'))
	value = int(input('\n WHAT IS YOUR VALUE '))
	power = int(input('\n HOW MUCH IS THE POWER FOR YOUR VALUE'))
	if i_want == 1:
		key = square_root_and_powers(1,value,0,0)
		word = key.engine()
		print(word)
	elif i_want == 2:
		key = square_root_and_powers(2,0,value,power)
		word = key.engine()
		print(word)

except Exception as e:
	print('\n YOU GOT ERROR IN INPUT METHOD CHECK :')
	print(e)
else:
	if  i_want > 2 or i_want < 1:
		print('PLEASE CHOSE A VALUE BTW 1 AND 2 ONLY ')
		
