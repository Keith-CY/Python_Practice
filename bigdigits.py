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
		line += digits[int(digit)][i]
		line += '  '
	print(line)
