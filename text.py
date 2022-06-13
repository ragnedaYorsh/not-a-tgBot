#ДЕБИЛЬНЫЙ КАЛЬКУЛЯТОР v.2

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

while True:
	print(Fore.BLACK)
	print(Back.GREEN)
	what = input("Что делаем? (+, -, /, *, , %): ")

	print(Fore.RED)
	print(Back.CYAN)

	a = float(input("Введи первое число: "))
	b = float(input("Введи второе число: "))

	print(Fore.BLACK)
	print(Back.YELLOW)

	if what == "+":
		c = a + b
		print("Результат: " + str(c))

	elif what == "-":
		c = a - b
		print("Результат: " + str(c))

	elif what == "/":
		if b == 0:
			print("На ноль делить нельзя..., тупица.")
		else:
			c = a / b
			print("Результат: " + str(c))

	elif what == "*":
		c = a * b
		print("Результат: " + str(c))

	#возведение в степень
	elif what == "**": 
  		c = a ** b
  		print("Результат: " + str(c))

	#деление по модулю
	elif what == "%":
  		c = a % b
  		print("Результат: " + str(c))  

	print(Fore.RED)
	print(Back.BLACK)

	dalee = input("Хотите продолжить?(Да, Нет)\n")
	if dalee == "Да":
		print("")
	if dalee == "Нет":
		break	
else:
	print("Выбрана неверная операция(((")