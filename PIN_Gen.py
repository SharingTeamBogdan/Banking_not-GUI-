import random
def Gen():
	s='1234567890'
	x=0
	PIN=""
	while(x<4):
		char=random.choice(s)
		PIN+=char
		x+=1
	return PIN