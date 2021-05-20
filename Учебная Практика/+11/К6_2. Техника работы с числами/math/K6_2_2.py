#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К6_2. Техника работы с числами
	math
'''

import math
 
def getsin(x):
    multiplier = 1
    result = 0
    for i in range(1,20,2):
    	result += multiplier*pow(x,i)/math.factorial(i)
    	multiplier *= -1
    	
    return result
     
def main():
	print("Арифметические функции")
	print("sin(pi/2) =", getsin(math.pi/2)) # returns 1.0
	print("math.pow(3, 2) =", math.pow(3,2))
	print("math.pow(9, 0.5) =", math.pow(9,0.5))
	print("math.sqrt(9) =", math.sqrt(9))
	print("math.factorial(5) =", math.factorial(5))
	
	print("Округление:")
	print("math.ceil(1.001) =", math.ceil(1.001) )    # returns 2
	print("math.floor(1.001) =", math.floor(1.001) )   # returns 1
	print("math.factorial(10) =", math.factorial(10) )  # returns 3628800
	print("math.gcd(10,125) =", math.gcd(10,125) )    # returns 5
	 
	print("math.trunc(1.001) =", math.trunc(1.001) )   # returns 1
	print("math.trunc(1.999) =", math.trunc(1.999) )   # returns 1
	print()
	
	print("Тригонометрические функции")
	print("math.sin(math.pi/4) =",math.sin(math.pi/4) )    # returns 0.7071067811865476
	print("math.cos(math.pi) =",math.cos(math.pi) )      # returns -1.0
	print("math.tan(math.pi/6) =",math.tan(math.pi/6) )    # returns 0.5773502691896257
	print("math.hypot(12,5) =",math.hypot(12,5) )       # returns 13.0
	print("math.atan(0.5773502691896257) =",math.atan(0.5773502691896257) ) # returns 0.5235987755982988
	print("math.asin(0.7071067811865476) =",math.asin(0.7071067811865476) ) # returns 0.7853981633974484
	print()
	
	print("Гиперболические функции")
	print("math.sinh(math.pi) =", math.sinh(math.pi) )    # returns 11.548739357257746
	print("math.cosh(math.pi) =", math.cosh(math.pi) )    # returns 11.591953275521519
	print("math.cosh(math.pi) =", math.cosh(math.pi) )    # returns 0.99627207622075
	 
	print("math.asinh(11.548739357257746) =", math.asinh(11.548739357257746) )   # returns 3.141592653589793
	print("math.acosh(11.591953275521519) =", math.acosh(11.591953275521519) )   # returns 3.141592653589793
	print("math.atanh(0.99627207622075) =", math.atanh(0.99627207622075) )     # returns 3.141592653589798
	print()

	print("Логарифмические функции")
	print("math.exp(5) =", math.exp(5))                      # returns 148.4131591025766
	print("math.e**5  =", math.e**5 )                       # returns 148.4131591025765
	 
	print("math.log(148.41315910257657) =", math.log(148.41315910257657))     # returns 5.0
	print("math.log(148.41315910257657, 2) =", math.log(148.41315910257657, 2))  # returns 7.213475204444817
	print("math.log(148.41315910257657, 10) =", math.log(148.41315910257657, 10)) # returns 2.171472409516258
	 
	print("math.log(1.0000025) =", math.log(1.0000025))              # returns 2.4999968749105643e-06
	print("math.log1p(0.0000025)  =", math.log1p(0.0000025) )           # returns 2.4999968750052084e-06
	print()



if (__name__ == "__main__"):
	main()
