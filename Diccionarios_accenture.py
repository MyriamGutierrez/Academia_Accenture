zoo_animals = {'Unicorn': 'Cotton Candy House',
				'Sloth': 'Rainforest Exhibit',
				'Bengala Tiger': 'Jungle House',
				'Atlantic Puffin': 'Artic Exhibit',
				'Rockhopper Penguin': 'Artic Exhibit'}

birdays = {'Myriam Gutierrez': '25-01-1995',
				'Alejandra Abreu': '10-02-1995',
				'Scarlet Gonzales': '05-08-1995',
				'Jessica Garza': '09-12-1995',
				'Alejandra Weigend': '13-04-1995'}

del zoo_animals['Sloth']
del zoo_animals['Bengala Tiger']
zoo_animals ['Rockhopper Penguin'] = 'Rainforest Exhibit'

print zoo_animals

print birdays

name = raw_input ("Cual es el nombre de la persona : ")

print birdays.get(name)

palabra = raw_input ("Ingresa el string: ")


dic_letras = {}
for n in palabra:
    keys = dic_letras.keys()
    if n in keys:
        dic_letras[n] += 1
    else:
        dic_letras[n] = 1


print dic_letras

