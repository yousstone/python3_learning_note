

def normailize(name):
	new_name = ''
	for index ,char in enumerate(name):
		if index == 0:
			new_name += char.upper()
		elif index >= 1:
			new_name += char.lower()
	return new_name
print(normailize('adam'))

	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normailize,L1))
print(L2)	


L3 = ['lisa', 'michael','jordan']
print(list(map(lambda name: name.capitalize(),L3)))

