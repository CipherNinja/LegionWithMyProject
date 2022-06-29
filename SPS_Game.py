import random

computer = ['stone','paper','scissor']
computer_turn = random.choice(computer)
human_choice = str(input('\nEntre your choice : '))

if human_choice == computer_turn:
	print("Your Game Is Tied ")

elif human_choice == "stone" and computer_turn == "scissor":
	print('\nYOU WIN THE GAME')
	print('your choise is ',human_choice)
	print('computer choise is ',computer_turn)
elif human_choice == "paper" and computer_turn == "stone":
	print('\nYOU WIN THE GAME')
	print('your choise is ',human_choice)
	print('computer choise is ',computer_turn)
elif human_choice == "scissor" and computer_turn == "paper":
	print('\nYOU WIN THE GAME')
	print('your choise is ',human_choice)
	print('computer choise is ',computer_turn)
else:
	for i in range(0,6):
		print("\n You Are Loser ")
	print('your choise is ',human_choice)
	print('computer choise is ',computer_turn)
