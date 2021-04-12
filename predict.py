def		main():
	try:
		with open("parameters.txt") as parameters_file:
			param_list = parameters_file.read().splitlines()
	except Exception as e:
		print("Can't open file `parameters.txt`. Make sure to train the model first.")
		exit(1)
	if (len(param_list) != 2):
		print("parameters.txt not well formatted.")
		exit(1)
	try:
		param_list = list(map(float, param_list))
	except Exception as e:
		print("Parameter is not a float.")
		exit(1)
	theta0, theta1 = param_list[0], param_list[1]
	try:
		mileage = float(input("Please enter the mileage: "))
	except Exception as e:
		print("Not a float")
		exit(1)
	if (mileage < 0):
		print("Mileage can't be negative.")
		exit(1)
	print(f"This car is worth {mileage * theta1 + theta0}€")


if __name__ == "__main__":
	main()
