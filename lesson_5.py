# Множеста set, frozenset  не упорядоченные данные, уникальные значения
# emails ={'geeks@edu.kg', 'kurmanbek@gmail.com','nur@gmail.com','Geeks@edu.kg'}
# print(emails)

# st = {10,1.0,1,True,False,"Hello",(0,1,2,3)}
# print(st)

# strange_app = set('Tiktok')
# print(strange_app)

# company={'Google','Meta','Netflix'}
# company.add('Geeks')
# print(company)
# company.remove('Meta')
# print(company)
# company.pop()
# print(company)

# nums1 = [10,20,30,40,50]
# nums2 = [30,40,50,60,70]
# print(set(nums1+nums2))
# nums3 = {10,20,30,40,50,"20"}
# print(nums3)

# frzn_set = frozenset({10,20,30,30,20,40,'kj'})
# print(frzn_set)


# import dis
# dis.dis("{1,2,3,4,5}")
# dis.dis("frozenset({1,2,3,4,5})")


# Dict - словари. Неупорядоченная структура данных, позволяющая хранить пары "Ключ" - "Значение".
# nums=[40,50,10,20,5]
# print(len(nums))
# student ={'name':'Nurbolot', 'age':'18'}
# print(len(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('job','Python developer')  #Добавляет значение в словарь
# student.pop('age')  #Удаляет по ключу
# print(student)
# student.popitem() #Удаляет последний элемент словаря
# print(student)
# student['name'] = 'Anton'
# print(student)


# osh ={
#     'name':'Osh',
#     'year':3023,
#     'population':200000
# }
# print(osh.keys())
# print(osh.values())
# print(osh.items())

# for k,v in osh.items():
#     print(k,v)

contact = {'MCHS':112}
while True:
    command = input("1 - посмотреть, 2 - добавить, 3 - удалить, 4 - обновить: ")
    if command == "1":
        print(contact)
    elif command == "2":
        add_name = input("Введите имя: ")
        add_number = input("Введите номер: ")
        contact.setdefault(add_name,add_number)
        print("Контакт успешно добавлен!")
    elif command == "3":
        del_name = input("Введите имя удаляемого контакта: ")
        contact.pop("del_name")
        print("Контакт успешно удалён!")
    elif command == "4":
        update1 = input("Введите контакт, который хотите обновить: ")
        # new_name = input("Введите новое имя: ")
        new_phone = input("Введите новый телефон: ")
        contact[update1]=new_phone
        print("Успешно обновлено!")


