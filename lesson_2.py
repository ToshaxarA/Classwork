# Методы строк
# name = "kurmanbek"
# print(name.upper())  # Все с большой буквы
# print(name.title())  # Первая буква с большой буквы, остальные 
# print(name.count('k')) # Считает что-либо

# print('gEEkS'.title())
# print('gEEkS'.upper())

# Индексы, срезы строк

# it = "Geeks"
#     # 01234
# print(it[0])
#     # Срез
# it_company = "Google"
# print(it_company[3])
# print(it_company[4])
# print(it_company[0:2])
# print(it_company[3:6])

# print(10+4.0)
# print(5.0+10)

# print(True+1)
# print(False+2)

# print(True+1.0)

# print(10 + int("5"))
# print(float(3)+int("100"))

# print("10"+"10")
# print(int("10")+int("10"))

# name = "Nurobolot"
# age = 18
# language = "Python"
# developer = True
# height = 176.3
# # Форматирование print(f)
# print("Hello, I'm " + name + "and my age " + str(age) + ". My language is " + language)
# print("Hello, I'm", name, "and my age ", age,". My language is ",language)
# print(f"Hello, I'm {name} and my age {age}. My langguage is {language}")

# name = input("Введите своё имя: ")
# print ("Здравствуйте", name)

# num1=input("Num1: ")
# num2=input("Num2: ")
# print(int(num1)-int(num2))

# mil = float(input("Введите расстояние в милях: "))
# print("Ответ: ", round(mil*1.60934,2), "km")

# Операторы сравнения
# print(4==4) # 4 равно 4?
# print("Hello" == "hello")

# print(400 != 400)  # != не равно
# print(500 != 400)

# print(10>1)
# print(4>40)

# print(40<7)
# print(50<100)

# print(10>=10)
# print(3>=4)

# print(10<=10)
# print(3<=8)

# Операторы условия
# num1 = 100
# num2 = 20
# if num1>num2:
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# number_1 = int (input("Первое число: "))
# operator = input("Введите один из знаков +, -, *, /: ")
# number_2 = int (input("Второе число: "))
# if operator == "+":
#     print("Ответ: ", number_1+number_2)
# elif operator == "-":
#     print("Ответ: ", number_1-number_2)
# elif operator == "*":
#     print("Ответ: ", number_1*number_2)
# elif operator == "/":
#     print("Ответ: ", number_1/number_2)
# else:
#     print("Введите корректный оператор")

# login = input("Login: ")
# password = input("Password: ")
# if login == "geeks" and password == "geeks2023":
#     print("Welcome!")
# else: 
#     print("Не правильно")

# if login == "geeks":
#     if password == "geeks2023":
#         print("Welcome")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect login")

# Диапазоны
price = int(input("Цена: "))
if price <40:
    print("Cheap")
elif price>=50 and price<=70:
    print("Normal")
elif price>70 and price <=100:
    print("Дорого")
else:
    print("Пипец как дорого")
