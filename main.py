# Netology: input

# name = input("Type your name: ")
# print("Привет", name)

# Сначала нужно импортировать
# класс datetime из модуля datetime, после чего создать объект datetime. Модуль предоставляет метод now()

import datetime

dt = datetime.datetime.now()
current_time = dt.time()
# onlyd = datetime.datetime.date()
dt_now = datetime.datetime.utcnow()

attr = dir(datetime)
print(attr)

print ("dt: ", dt, "time: ", current_time, "UTC: ", dt_now)

date_string = "02/19/23"
date_obj = datetime.datetime.strptime(date_string, '%m/%d/%y')

print(date_obj)

print(type(5))
print(type(5.8))

sum = 0
array = [45000, 7, -934, 0, 2839]
for i in array:
   sum += i
print(sum)

print(17/2) #обычное деление - результат 8.5
print(17//2) #целочисленное деление - результат 8, целая часть при делении
print(17%2) #деление с остатком - результат 1, остаток при делении

str1 = 'Hello, '
str2 = 'world!'
print(str1+str2)

a = None
print(type(a))
