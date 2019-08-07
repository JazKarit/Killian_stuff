escaped = False
done = False
rod = False
print("\t You find yourself in a room with a locked door. \n You are sitting in a comfortable chair that is part of a circle of three other chairs. \n To your left is a fireplace with a roaring fire, with many odd trinkets on it's mantel.\n To your right is a bookshelf with many books, as well as 3 portraits of famous historical figures. \n To your back is an ornate piano.  On a small coffee table in front of you, there is a note, as well as a strange box.")
while(not escaped):
	action = input("What do you do? ")
	if action == "examine note":
		print("The note reads,\" Greetings. As you can see, you are trapped in this strange room. Next to this note, you will find a \n puzzle box. The key to your escape is in this box. You will need to solve each of this room's puzzles. Good luck,\" \n Many of the letters are colored red.")
	elif action == "examine colored letters":
		print("The colored letters are: e, r, A, o, a, s, r, s, m, e, b, i, c")
	elif action == "examine fireplace":
		action2 = input("Which part of the fireplace would you like to examine? ")
		if action2 == "mantel":
			print("The mantel has 2 trinkets, a bottle with a wooden shell surrounding it, and another box.")
			solve = input("Would you like to attempt to solve a puzzle? y/n ")
			if solve == "y":
				select = input("Which puzzle would you like to solve")
				if select == "bottle":
					if rod == False:
						print("the wooden casing arround the bottle")
			if action2 == "hearth":
				print("There is a fire crackling away in the hearth. There also appears to be a number sequence at the back, but it is obscured by the flames.")
	elif action == "examine door":
		print("The door is locked using a combination lock")
		unlock = input("Would you like to unlock it? y/n ") 
		if unlock == "y":
			code = input("Please enter a 6-digit code ")
			if code == "578421":
				escaped = True
				print("You escaped!")
			else:
				print("The door remained locked.")
	elif action == "examine box":
		print("The box is carved from a very light and fragile wood. It has")
		solve = input("What will you do?")
		if solve == "smash":
			print("you throw the box into the floor.\n\n It's smashed to pieces, it's  wood scattering across the floor.It reveals a smaller box inside with an entirely new puzzle")
	else:
		print("Invalid command")

