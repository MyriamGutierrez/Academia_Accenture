import math

num_lados_str = raw_input ("Introduce la cantidad de lados del poligono: ")
mide_x_lado_str = raw_input ("Introduce cuanto mide cada lado (cada lado mide lo mismo): ")

num_lados = int(num_lados_str)
mide_x_lado = int(mide_x_lado_str)
perimetro = num_lados * mide_x_lado

print "El perimetro del poligono es: ", perimetro
num_tan = 180/num_lados
math.radians(num_tan)
apotema = (mide_x_lado / (2 * math.tan(math.radians(num_tan))))

area = (apotema * mide_x_lado) / 2

print "El area del poligono es :", area 