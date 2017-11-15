my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
zoo_animals = ['elephant', 'zebra', 'tiger', 'lion']
zoo_animals.append('cheetah')
int_iteracion = 0
print len(zoo_animals)
for list in zoo_animals:
	int_iteracion += 1
	if (int_iteracion < len(zoo_animals)):
		if (zoo_animals[int_iteracion] == 'lion'):
			zoo_animals[int_iteracion] = 'sharck'

zoo_animals.remove('zebra')
new_list = []
i = 0
for i in range(1, len(my_list)-1):
	if (my_list[i] % 2) != 0 :
		new_list.append(my_list[i])
					

print new_list

print zoo_animals
