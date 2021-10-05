def calculator(prevAnswer):

	if prevAnswer == 0:
		num1 = int(input("Please enter first number: "))
		num2 = int(input("Please enter second number: "))

	if prevAnswer != 0:
		num1 = prevAnswer
		num2 = int(input("Please enter second number: "))		
	
	operator = input("Please enter operator (+, -, *, /): ")

	# do math
	if operator == "+":
		answer = num1 + num2
		print(answer)

	elif operator == "-":
		answer = num1 - num2
		print(answer)

	elif operator == "*":
		answer = num1 * num2
		print(answer)

	elif operator == "/":
		answer = num1 / num2
		print(answer)

	else:
		print("Invalid operator.")
		calculator(num1, num2, operator)

	choice = input("New calculation? (y/n): ")
	if choice == "y":
		importAnswer = input("Use previous answer as first number? (y/n): ")
		if importAnswer == "y":
			calculator(answer)

		if importAnswer == "n":
			calculator(0)


	elif choice == "n":
		quit()


calculator(0)