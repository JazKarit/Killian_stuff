text_to_display = "Hello."
print(text_to_display)
response = input("How are you?")

if response == "good":
	print("Nice!")
	response = input("What have you done today?")
	print("That's good")
elif response == "not good":
	 print("that sucks")
	 response = input("is there anything I can do to make you feel better?")
	 if response == "no":
		     print("I'm sorry")
else:
	print("what?")

age = input("Anyway, I haven't seen you in a while. How old are you?")

if int(age) <7:
	print("Wow! How have you even loaded this program!")
elif int(age) >=7 and int(age) <13:
	print("That's nice! I hope that school is going well!")
elif 
elif int(age) >=150:
	print("Wow!" + str(age)+"!How are you still alive?")
else:
	print("Okay")

