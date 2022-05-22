alph = 'abcdefghijklmnopqrstuvwxyz'

depth = 4

def level(d, word, dorw):
	if d == depth:
		for c in alph:
			print(word + c + dorw)
			print(word + c + c + dorw)
	elif d < depth:
		for c in alph:
			print(word + c + dorw)
			print(word + c + c + dorw)
			level(d+1, word+c, c+dorw)
	else:
		pass
		
		
level(0, '', '')
	