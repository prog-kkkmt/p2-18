#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К6_1. Техника работы с числами

Задание 1. 
 Составить и выполнить по 3 примера использования модулей для работы
с дробными числами (fractions), для точных вычислений (decimal).
Задание 2. 
 Подготовить инструкцию по использованию модулей fractions, decimal.
'''

from decimal import Decimal, getcontext
from fractions import Fraction as frac
from fractions import Fraction

#{==== MENU ====}

def menu():
	print("0. Выход")
	print("1. Модуль \"decimal\"")
	print("2. Модуль \"fractions\"")

#{==== MENU for Decimal ====}
def menuDecimal():
	print("0. Назад")
	print("1. Зачем нужен \"decimal\"")
	print("2. Точность \"decimal\"")
	print("3. Округление \"decimal\"")
	
def whatForDec():
	#{ -- Example 1 -- }
	print("1. Зачем нужен \"decimal\"")
	print("Вобщем \"decimal\" нужен для того, чтобы вычислять более точные значения")
	print("Если сложить числа 0.1 и 0.2, то получится:")
	print(">>> 0.1 + 0.2 = ", 0.1 + 0.2)
	print()
	n1 = Decimal(0.1)
	n2 = Decimal(0.2)
	print("Но, воспользовавшись модулем (decimal), при сложении этих чисел, мы получим: ")
	print(">>> Decimal(0.1) + Decimal(0.2) = ", n1 + n2)
	print("-----------------------------------------------------------")
	print()

def accuracyDec():
	#{ -- Example 2 -- }
	print("2. Точность \"decimal\"")
	print("Decimal(number) можно устанавливать точность. Т.е, кол-во знков после запятой.")
	print("Для этого нужно прописать следующие:")
	print()
	print("Подключить модуль")
	print(">>> from decimal import Decimal, getcontext")
	print()
	print("Установим точность 2")
	print(">>> getcontext().prec = 2")
	getcontext().prec = 2
	print(">>> print(Decimal(\"4.341\")/1) = ", Decimal("4.341") / 1)
	print(">>> print(Decimal(\"4.341\")/4) = ", Decimal("4.341") / 4)
	print()
	print("Установим точность 3")
	print(">>> getcontext().prec = 3")
	getcontext().prec = 3
	print(">>> print(Decimal(\"4.341\")/1) = ", Decimal("4.341") / 1)
	print(">>> print(Decimal(\"4.341\")/4) = ", Decimal("4.341") / 4)
	print("---------------------------------------------------------------")
	print()
	
def roundingDec():
	#{ -- Example 3 -- }
	print("3. Округление \"decimal\"")
	print("Decimal(number), можно округлять. Для этого нужно прописать следующее:")
	print()
	print("Установим точность округления")
	print(">>> getcontext().prec = 4")
	getcontext().prec = 4
	print()
	print("number = Decimal(\"2.12345678\")")
	number = Decimal("2.123456789")
	print()
	print("Округляем число number")
	print(">>> print(number.quantize(Decimal(\"1.000\")))", number.quantize(Decimal('1.000')))
	print(">>> print(number.quantize(Decimal(\"1.00\")))", number.quantize(Decimal('1.00')))
	print(">>> print(number.quantize(Decimal(\"1.0\")))", number.quantize(Decimal('1.0')))
	print(">>> print(number.quantize(Decimal(\"1\")))", number.quantize(Decimal('1')))
	print(">>> print(number.quantize(Decimal(\"10\")))", number.quantize(Decimal('10')))
	print()
	print("Но если мы введем:")
	print(">>> print(number.quantize(Decimal(\"1.0000\")))")
	print("То будет следующая ошибка: ", end="")
	print("decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]")
	print()
	print("Чтобы избежать ее, необходимо поменять точность округления")
	print(">>> getcontext().prec = 5")
	getcontext().prec = 5
	print()
	print("Теперь ошибки не будет")
	print(">>> print(number.quantize(Decimal(\"1.000\")))", number.quantize(Decimal('1.000')))
	print("-----------------------------------------------------------")

#{==== MENU for Fractions ====}

def whatForFrac():
	#{ -- Example 1 -- }
	print("1. Зачем нужен \"fractions\"")
	print("Этот модуль пригодится в тех случаях, когда вам необходимо выполнить вычисления")
	print("с дробями, или когда результат должен быть выражен в формате дроби.")
	print(">>> from fractions import Fraction as frac")
	print(">>> from fractions import Fraction")
	print()
	
	print(">>> print(Fraction(\'33.33\')")
	print(Fraction('33.33'))
	print()
	
	print(">>> print(Fraction(33.33)")
	print(Fraction(33.33))
	print()
	
	print("Модуль Fraction особенно полезен, потому что он автоматически уменьшает дробь.")
	print("Выглядит это вот так:")
	print(">>> Fraction(153, 272)")
	print(Fraction(153, 272))
	print()
	
	print("Кроме того, вы можете выполнять бинарные (двоичные) операции над дробью также")
	print("просто, как вы используете int или float . Просто добавьте две фракции:")
	print(">>> Fraction(1, 2) + Fraction(3, 4) = Fraction(5, 4)")
	print(Fraction(1, 2) + Fraction(3, 4))
	print()
	
	print("Теперь давайте попробуем возвести дробь в степень:")
	print(">>> Fraction(1, 8) ** Fraction(1, 2)")
	print(Fraction(1, 8) ** Fraction(1, 2))
	print()
	
	print("-----------------------------------------------------------")
	print()

#{==== MAIN ====}

def main():
	n = -1
	n_loc = -1
	while (n):
		print()
		menu()
		n = int(input())
		
		if (n == 1):
			print()
			while (n_loc):
				menuDecimal()
				n_loc = int(input())
				print()
				
				if (n_loc == 1):
					whatForDec()
				elif (n_loc == 2):
					accuracyDec()
				elif (n_loc == 3):
					roundingDec()
			n_loc = -1
		elif (n == 2):
			whatForFrac()
			n_loc = -1
	
if (__name__ == "__main__"):
	main()
