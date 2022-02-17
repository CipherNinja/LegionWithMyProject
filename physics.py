

print("This Program Helps you to get correct value of B_Energy theory")


m = float(input("entre mass of satellite :: "))
r = float(input("entre radius :: "))
i = input("chose 'k' for kinetic energy and 'p' for potential energy of satelite")
if i == "k":
	print((round((6.67)*(-1*(10**11))*(6*10**24)*m)/(2*r),3),"is the Kinetic Energy of your satelite")
elif i == "p":
    print(round((-1*(6.67)*(-1*(10**11))*(6*10**24)*m)/(2*r),3),"is the Potential Energy of your satelite")
else :
	print("This Program is just a prototype it is still under development")
	


    

