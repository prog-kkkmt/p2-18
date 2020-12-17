# Выполнил:Степаненко Кирилл Алексеевич
# Группа: П2-18
# Decimal- вычисления с заданной точностью
# Модуль Decimal незаменим, если нужно считать деньги: с его помощью вы сможете подсчитать точную сумму, вплоть до копеек.

# При работе с числами с плавающей точкой (то есть float) мы сталкиваемся с тем, что в результате вычислений мы получаем не совсем верный результат:

number = 0.1 + 0.1 + 0.1
print(number)       # 0.30000000000000004

# Проблему может решить использование функции round(), которая округлит число.
# Однако есть и другой способ, который заключается в использовании встроенного модуля decimal.
# Ключевым компонентом для работы с числами в этом модуле является класс Decimal.
# Для его применения нам надо создать его объект с помощью конструктора.
# В конструктор передается строковое значение, которое представляет число:

from decimal import Decimal

number = Decimal("0.1")

# После этого объект Decimal можно использовать в арифметических операциях:

from decimal import Decimal

number = Decimal("0.1")
number = number + number + number
print(number)  # 0.3

# В операциях с Decimal можно использовать целые числа:

number = Decimal("0.1")
number = number + 2

# Однако нельзя смешивать в операциях дробные числа float и Decimal:

number = Decimal("0.1")
number = number + 0.1   # здесь возникнет ошибка

# С помощью дополнительных знаков мы можем определить, сколько будет символов в дробной части числа:

number = Decimal("0.10") # Строка "0.10" определяет два знака в дробной части, даже если последние символы будут представлять ноль. Соответственно "0.100" представляет три знака в дробной части.
number = 3 * number
print(number)       # 0.30