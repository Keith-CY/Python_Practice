import random

article = ["the", "a"]
theme = ["cat", "dog", "man", "woman"]
verbal = ["sang", "ran", "jumped"]
adv = ["loudly", "quietly", "well", "badly"]
for i in range(int(input("rows: "))):
	poem_type = random.randint(0,1)
	if poem_type:
		s = random.choice(article) + " " + random.choice(theme) + " " + random.choice(verbal) + " " + random.choice(adv)
	else:
		s = random.choice(article) +" " + random.choice(theme) +" " + random.choice(verbal)
	print(s)