import random

def randnum(fnum):
	lines=open(fnum).read().splitlines()
	return random.choice(lines)

print(randnum('sozler.txt'))