# Задание 1
#Что произойдет при вводе следующих команд. Напишите ответ в виде комментария.
#Например: 
int("578")#строка 578 из string превратится в integer
int(673.3123)#673.3123 из float превратится в integer
float(512)#512 из int превратится во float 
int(float(str(192)))# 192 из int преобразуется в строку, затем во float и в итоге вернётся в свой изначальный тип integer
float(173)+5 # результат действия сложения 173 (int) преобразованного во float и 5(int) будет равен 178.0 во float
str(193.000000000001) # 193.000000000001 из float превратится в текст string



# Задание 2 
# Что такое конкатенация? Объясните следующие две строки кода:
var7='Calling ' + str(911) 
"""
Конкатенация - операция склеивания строк типа string. 
В данном случае строка текста 'Callin ' склеивается с 
числом 911, ставшим текстом.
"""
var8='abc' + 'xyz' # Склеиваются две текстовых переменных string

# Задание 3
# Какие переменные можно складывать(без изменения их типа данных) и что при этом получится?
a = 589
b = 932.901
c = 'Hello world'
d = '892.01'

"""
Складывать можно a + b, так как они имеют тип str и float, результат будет во float 1521.9009999999998;
Ещё можно сложить c + d, так как они по сути текст типа string, результат будет в str "Hello world892.01"
При сложени

"""
#Задание 4
# Дополнительное задание:
# 4) Напишите одну строку кода, которая использует только вышеуказанные
# переменные, и после которой print(a, b, c, d) выведет следующее: Hello world589 892.01
# 932.901589 1481.01

a=c+str(a);c=str(b)+str(int(a[11:14]));b=d;d=float(a[11:14])+float(d)
print(a, b, c, d)