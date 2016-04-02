zero = ["*****","*   *","*   *","*   *","*****"]
one = ["  *  ","  *  ","  *  ","  *  ","  *  "]
two = ["*****","    *","*****","*    ","*****"]
three = ["*****","    *","*****","    *","*****"]
four = ["*   *","*   *","*****","    *","    *"]
five = ["*****","*    ","*****","    *","*****"]
six = ["*****","*    ","*****","*   *","*****"]
seven = ["*****","    *","    *","    *","    *"]
eight = ["*****","*   *","*****","*   *","*****"]
nine = ["*****","*   *","*****","    *","*****"]

num = input("enter a number: ")
digits = [zero, one, two, three, four, five, six, seven, eight, nine]
for i in range(5):
	line = ''
	for digit in num:
		part = ''
		for x in digits[int(digit)][i]:
			if x == "*":
				part += digit
			else:
				part += ' '
		line = line + part + '  '
	print(line)
