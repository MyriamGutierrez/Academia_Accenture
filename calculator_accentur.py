# -*- coding: utf-8 -*-
class Calculator:

    def sumar(self, a, b):
        print (a + b)

    def restar(self, a, b):
        print (a - b)

    def multp(self,a,b):
        print (a * b)

    def divi(self,a,b):
		print (a / b)

if __name__ == "__main__":
	operacion_str = raw_input ("Seleccione que tipo de opracion quiere hacer (1 == suma, 2 == resta, 3 == multiplicación y 4 == divición)  : ")
	operacion_int = int(operacion_str)

	a_str = raw_input ("ingrese valor de a : ")

	a_int = int(a_str)

	calc = Calculator()


	if (operacion_int == 1):
		calc.sumar(a_int,15)

	elif (operacion_int == 2):
		calc.restar(a_int,15)

	elif (operacion_int == 3):
		calc.multp(a_int,15)

	else:
		calc.divi(a_int,15)