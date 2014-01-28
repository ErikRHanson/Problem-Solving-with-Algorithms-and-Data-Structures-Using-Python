import random


def attempt(strlen):
	alphabet = "abcdefghijklmnopqrstuvqxyz "
	value = ""
	for letter in range(strlen):
		value = value + alphabet[random.randrange(27)]

	return value

def score(goal, teststring):
	numSame = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numSame = numSame + 1
	return numSame / len(goal)

def main():

	goalstring = "methinks it is like a weasel"
	newstring = attempt(28)
	bestscore = 0
	beststring = ""
	newscore = score(goalstring, newstring)
	loopcount = 0
	while newscore < 1:
		if newscore > bestscore:
			print (newscore, newstring)
			bestscore = newscore
			beststring = newstring
		newstring = attempt(28)
		newscore = score(goalstring, newstring)

		if loopcount % 1000000 == 0:
			print (bestscore, beststring)
		loopcount = loopcount + 1

main()
