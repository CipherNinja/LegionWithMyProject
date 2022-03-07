import math as c 
class triangle:
	def perimetre(self):
		per = sum(self.sides)
		return per 

	def area_of_triangle(self):
		Ar = 1/2*(self.base*self.height)
		print('Area of triangle is : ',Ar)
	def ressultant_of_triangle(self):
	 	resultant = c.sqrt(self.height**2 + self.base**2 + ((self.height*self.base)*2)*c.cos(c.pi/2))
	 	print("Hypotenous of triangle is ",round(resultant,4))

	def __init__(self,sides,base,height):
		self.height = height
		self.base = base
		self.sides = sides

t1 = triangle([2,3,4],0,0)
passed = t1.perimetre()
print("Perimetre of triangle is : ",passed)
#---------CY-NINJA-----------------CY-NINJA-----------------------we can use ony one of t1 and t2 at a time in this t1 is silent 
#----------------------CY-NINJA-----------------------------------if you want to use t1 then comment out t2 
#---------CY-NINJA-----------------CY-NINJA-----------------------this step was optional
t2 = triangle(2,3,4)
passed2 = t2.area_of_triangle()
print(passed2)

i = float(input(('Entre height of triangle : ')))
j = float(input(('Entre base of triangle : ')))

t3 = triangle(0,i,j)
passed3 = t3.ressultant_of_triangle()
print(passed3)
#--------------------------------------------FOLLOW ME ON INTAGRAM @priyesh_pandey91 and @cypherninja1010
