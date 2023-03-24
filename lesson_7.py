# Лямбда функции / lambda functions  lambda:argment = expression   превращает переменную в некоторое подобие функции
#  Нельзя подсказывать значение параметров по умолчанию
# def mult_two(number:int) --> int:
#     return number*number
# print(mult_two(10))

# lambda_mult_two = lambda number: number*number
# print(lambda_mult_two(10))

# print((lambda number: number*number)(10))

##############

# def add(num1:int=10, num2:int=10) ->int:
#     return num1+num2
# print(add(5,6))

# lambda_add = lambda num1, num2: num1+num2
# print(lambda_add(30,30))
# print(lambda_add())

# print((lambda num1, num2: num1+num2)(30,30))
 ########################

# numbers = [10,20,30,40,50]
# new_numbers = []

# def mult_two_list(nums:list) -> list:
#     for n in numbers:
#         new_numbers.append(n*2)
#     return new_numbers

# print(mult_two_list(numbers))

 # Класс map работает с функцией и  итерируемым объектом
# numbers = [10,20,30,40,50]
# lambda_new_numbers = list(map(lambda nums: nums*2, numbers))
# print(lambda_new_numbers)


# numbers = [10,20,30,40,50]
# print(list(map(lambda nums: nums*2, numbers)))

# print(list(map(lambda nums: nums*2, [10,20,30,40,50]))

################################

# nums = [1,2,3,4,5,6,7,8,9,10]
# chet = []

# def chet_numbers(numbers:list) -> list:
#     for n in numbers:
#         if n%2 ==0:
#             chet.append(n)
#     return chet
# print(chet_numbers(nums))

# lambda_filter_nums=list(filter(lambda numbers: numbers%2==0, nums))
# lambda_filter_nums=set(filter(lambda numbers: numbers%2==0, nums))
# print(lambda_filter_nums)
# класс filter - это map с условием

# print(list(filter(lambda numbers: numbers%2==0, [1,2,3,4,5,6,7,8,9,10])))  # Однострочное исполнение

# *Args, Kwargs   - упаковка и распаковка в кортеж безконечного количества аргументов
# print("Hello","World","Geeks","Python")
# print("Hello world!")

# def welcome(*name:str):
#     # print(name)
#     for n in name:
#         print("Здравствуйте", n)
# welcome ("Kurmanbek!", "Anton", "Anna", "Nurbolot")

# def student_mean_point(name:str,*points:int) ->str:
#     print(name,round(sum(points)/len(points)))    #round - округляет вверх всё, что >= 0,5
# student_mean_point("Nurbolot", 4,4,5,3,2,3,4,2)
# student_mean_point("Urumat", 4,4,5,3,2,3,4,2,2,4,4,4,3,2)

# **Kwargs  -  передача бесконечного количества аргументов в виде словарей 
# def translate(**words):
#     print(words)
# translate(Apple = "Яблоко", Phone = "Телефон", )

