def conversionF(farenheit):
	"""Converts Farenheit to Celsius"""
	celsius = (farenheit- 32) * (5/9)
	return celsius 
def conversionC(celsius):
	"""Converts Celsius to Farenheit"""
	farenheit = (9/5) * celsius + 32
	return  farenheit

select = input("select mode F/C ")
if select == "F":
	temp = input("input Farenheit ")
	print("")
	print(str(conversionF(int(temp))) + " Degrees Celsius")
elif select == "C":
	temp = input("input Celsius ")
	print("")
	print(str(conversionC(int(temp))) + " Degrees Farenheit")
else:
	print("invalid input")
