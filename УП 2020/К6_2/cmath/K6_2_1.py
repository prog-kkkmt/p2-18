#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К6_2. Техника работы с числами
	cmath
'''

import cmath
     
def main():
	print("Сложные функции")
	print("cmath.polar(complex(1.0, 1.0)) =", cmath.polar(complex(1.0, 1.0)) )	# returns (1.4142135623730951, 0.7853981633974483)
	 
	print("cmath.phase(complex(1.0, 1.0)) =", cmath.phase(complex(1.0, 1.0)) )	# returns 0.7853981633974483
	 
	print("abs(complex(1.0, 1.0)) =", abs(complex(1.0, 1.0)) )	# returns 1.4142135623730951
	
	print("cmath.sqrt(complex(25.0, 25.0)) =", cmath.sqrt(complex(25.0, 25.0)) )	# returns (5.49342056733905+2.2754493028111367j)
	 
	print("cmath.cos(complex(25.0, 25.0)) =", cmath.cos(complex(25.0, 25.0)) )	# returns (35685729345.58163+4764987221.458499j)
	print()



if (__name__ == "__main__"):
	main()
