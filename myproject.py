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
	vid = calculator([23,3],[23,4],[320],[32])
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