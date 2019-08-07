print("Metallic Ratio Generator")
print("")

num = input("How many integers would you like? ")
Coef = input("What coefficient would you like? ")

fibo = [0,1]
for n in range(1,int(num)):
	fibo.append(int(int(Coef)*fibo[-1]) + fibo[-2])
print(fibo)
