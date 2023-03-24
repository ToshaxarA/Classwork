#Lists - списки - изменяемый тип данных
name1="Nurbolot"
name2="Anton"
name3="Bayzak"
name4="Adilet"

#names = ["Nurbolot","Anton","Bayzak","Adilet"]
#print(names)

lst=[10, 1.0, "Geeks", False]
#print(lst[2][0:2])
#print(lst[0:2][0])   #Срез

number = 10
number = 11

cities = ["Bishkek","Osh","Naryn", "Talas"]
#print(cities)

#Методы
# cities.append("Batken")   #Добавляет элемент в конец списка 
# print(cities)
# cities.append("Tokmok")   #Добавляет элемент в конец списка 
# print(cities)
# cities.insert(0,"Karakol") #Добавляет элемент по индексу 
# print(cities)
# cities.remove("Bishkek")    # Удаляет элемет по значению
# print(cities)
# cities.pop(0)    # Удаляет элемент по индексу
# print(cities)

# del cities[1:3]   # Оператор del Удаляет элементы из списка по индексу и по срезу
# print(cities)

# cars = ["Toyota", "Honda", "BMW", "Mercedes", "Honda", 1.0]
# # # print(cars.count("Honda"))
# # # print(cars.count("honda"))
# # # print(cars.index("Mercedes"))
# # cars[0]="KIA"
# # print(cars)

# # print(cars[1:4:2])  # третья цифра - шаг, может быть отрицательный, тогда список переворачивается с конца в начало
# # print(cars[::-2])

# cars.sort()
# print(cars)

# numbers = [10, 11, 100, 1, 3, 4, 400, 1001, 0.1, 5.0]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)  #От большего к меньшему
# print(numbers)

# print(max(numbers))  #Максимальное значение
# print(min(numbers))  #Минимальное значение
# print(sum(numbers))  #Сумма элементов
# if 100 in numbers:   #Оператор in
#     print(True)
# else:
#     print(False)

# numbers.clear()
# print(numbers)

# nums1 = [10, 20, 30, 40, 50, int("199")]
# nums2 = [60, 70, 80, 90, 100]
# nums3 = nums2+nums1
# print(nums3)
# nums3.sort()
# print(nums3)

# numbers = [2.0, 10, "Hello", True, [10, 20, 30]]
# print(numbers)

#Truple - Кортежи  не изменяемый тип данных, похожий на список, но неизменный
# tup = (10, 3.0, "Geeks", False)
# print(tup)
# print(tup.count(10))
# print(tup.index("Geeks"))
# print(tup[2])
# print(tup[0:2])

# lst_tup = list(tup)   #преобразование в лист
# print(tup)
# lst_tup.append([1, 2, 3, 4])
# print(lst_tup)
# tup = tuple(lst_tup)  #преобразование в кортеж
# print(tup)

#import dis
#dis.dis("[1,2,3,4]")
#dis.dis("(1,2,3,4)")
tup = (10,)
print(type(tup))


