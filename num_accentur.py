num = raw_input ("Introduce el numero de altura de la piramide : ")
num_int = int(num)
espacios = num_int - 1
asteriscos = 1
for lines in range(num_int):
	while (espacios >= 0):
		print '%s%s' % ( (' '*espacios), ('*'*asteriscos))
		espacios -= 1
		asteriscos += 1
		
