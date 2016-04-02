lst = []
while True:
	try:
		num = input("enter a number or Enter to finish: ")
		if num is not '':
			lst.append(int(num))
		else:
			print(lst)
			print("count = %d, sum = %d, lowest = %d, highest = %d, mean = %f" %(len(lst), sum(lst), min(lst), max(lst), sum(lst)/len(lst)))
	except ValueError as err:
		print(err)