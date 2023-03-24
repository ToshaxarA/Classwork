# Функции / Functions
# def calc():
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1+num2)

# def welcome():
#     name = input("Ваше имя: ")
#     print("Здравствуйте", name)
# welcome()

# def add(num1, num2):   #Параметры функции add
#     print(num1+num2)
# add(10,40)  #Вызов функции add и передача параметров
# add(100,40)
# add(10,400)
# add(160,470)

# def chet_nechet(lst:list) -> str:
#     for num in lst:
#         if num %2 == 0:
#             print(num, "чётное")
#         else:
#             print(num, "нечётное")
#     print(num)

# numbers = [1, 3, 10, 1001, 400, 403, 102, 101, 607, 808, 888, 678, 109]
# chet_nechet([10,20,22,225,4,4,47,848])

# def add(num1:int, num2:int) -> int:
#     print(num1+num2)
# def sub(num1:int, num2:int) -> int:
#     print(num1-num2)
# def mult(num1:int, num2:int) -> int:
#     print(num1*num2)
# def div(num1:int, num2:int) -> int:
#     print(num1/num2)
# def main(number1:int, number2:int, operator:str)->int:
#     if operator == "+":
#         add(number1,number2)
#     elif operator == "-":
#         sub(number1,number2)
#     elif operator == "*":
#         mult(number1,number2)
#     elif operator == "/":
#         div(number1,number2) 
#     else:
#         print("Такого оператора не существует")
# main(10,20,'*')
# main(10,20,'/')
# main(10,20,'+')
# main(10,20,'-')
# main(10,20,'sdfdf')
# print()
# def get_name(name:str="Default"):
#     """Инструкция для функции"""                     #Инструкция для функции
#     print(name)
# get_name()
# len()
# "Hello".count()

# return   - оператор - красный, в операторах не надо ставить скобки, после return ничего не работает. В одной функции работает только один return.

# def add(num1:int=1, num2:int=1) -> int:
#     return num1 + num2
# print(add(20,20))
# def hello():
#     while True:
#         print("Hello")
#         return "Hello"
# hello()

# Исключения / Exeptions      except можно без указания класса ошибок. 
# while True:
#     try:
#         num1 = int(input("Первое число: "))
#         num2 = int(input("Второе число: "))
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("Деление на ноль!")
#     except ValueError:
#         print("Пишите только цифры!")
