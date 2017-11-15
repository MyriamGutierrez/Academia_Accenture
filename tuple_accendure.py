my_tuple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []


for i in range(0, len(my_tuple)):
	if (my_tuple[i] % 2) == 0 :
		new_list.append(my_tuple[i])

new_tuple = tuple(new_list)

print (new_tuple)