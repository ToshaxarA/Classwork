# # Циклы for и while
# for i in range(1, 2000, 2):   # rande (начало, конец, шаг)
#     print(i)

# cars = ["BMW", "COYOTA","MERCEDES", "HONDA"]
# print(cars)

# for car in cars:
#     if "MERCEDES"==car:
#         print(True)
#     else:
#         print(False)

# numbers = [10,1,3,5,100,101,500,111,113,403,607,809,901,307]
# for num in numbers:
#     if num % 2 ==0:
#         print ("число", num, "чётное")
#     else: 
#         print("число", num, "не чётное")

# nums = []
# for n in range(1, 101):
#     nums.append(n)
# print(nums)

#                        Генератор паролей
# import random
# # print(random.randint(1,10))

# # names = ["Nurbolot","Askhat","Nurtilek","Anton"]
# # print(random.choice(names))
# password_generator = "qwertyuiopasdfghjklzxcvbnm123456789"
# how_many_password = int(input("Сколько паролей вам нужно? "))
# Lean_pass = int(input("Длинна паролей: "))

# for j in range(how_many_password):
#     res=""
#     for i in range(Lean_pass):
#         choice = random.choice(password_generator)
#         res+=choice
#     print(res)

# # Цикл while
# num1 = 10
# num2 = 20
# while num1<num2:
#     num1+=1
#     print(num1)

# n = 0
# while True:
#     n+=1
#     print(n, "Geeks")
    # if n == 100:
    #     print("Stop!")
    #     break

# Генерация пароля и его подбор
# import random
# password = random.randint(1111,9999)
# print(password)
# n=1111
# while True:
#     print(n)
#     if password == n:
#         print(n, "is password")
#         break
#     n+=1

# for i in range(10,100,2):
# #     print(i)
# start = 0
# end = 100
# step = 2
# while True:
#     print(start)
#     start+=step
#     if start == end:
#         break
# import requests
# res = requests.get("http://kyzmat24.com/api/users").json()
# # print(res)
# for r in res:
#     # print(r['email'])
#     if r['username'] == "nurbolot":
#         print("Он есть")
#         break




