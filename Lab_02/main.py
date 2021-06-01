#Работа со строками
#1
string1 = "Python is a top programming language."
string2 = "  Enjoy to learn it!"
#2
string3 = string1+string2
print(string3)
#3
print(len(string1))
print(string1.title())
print(string1.lower())
print(string1.upper())
print(string2.rstrip())
print(string2.lstrip())
print(string2.strip())
print(string1.strip('P'))
#4
ch = string1[4]
print(ch)
#5
chm = string1[1:3]
print(chm)
#6
chm1 = string1[1:]
chm2 = string1[:3]
chm3 = string1[:]
chm4 = string1[1:5:2]
print(chm1)
print(chm2)
print(chm3)
print(chm4)
#7
#string1[2] = 'o' - TypeError: ‘str’ object does not support item assignment

#Работа с числами
#1
a = 30
b = 2
#2
print(a/b)
print(a%b)
print(a**b)
#3 - TypeError: can only concatenate str (not "int") to str
#param1 = "string" + 15
#print(param1)

#Преобразование данных
#1
param2 = "string" + str(15)
print(param2)
#2
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)


#Форматирование строк
#1-2
a = 1/3
print("{:7.3f}".format(a))
#3
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a,b))
print("{:10.3e} {:10.3e}".format(a,b))
#4
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = {:7.3f}".format(n3))

#Списки
#1
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(list1)
#2
print(dir(list))
#3
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list)
#4
list1[0] = 1
list1[1] = 2
print(list1)
#5
list1.append(100)
print(list1)
#6
list1.insert(2, 3)
print(list1)
#7
list1.remove(list1[0])
print(list1)
#8
list1.remove(list1[-1])
print(list1)

#Сортировка элементов списка
#1
list1.sort(reverse=True)
print('Sorted desc list: ', list1)
#2
sorted(list1, reverse=True)
print(list1)
#3
list2 = [3, 5, 6, 2, 33, 6, 11]
lis = sorted(list2)
print("Original list: ", list2)
print("Sorted list: ", lis)

#Кортежи
#1
print(dir(tuple))
#2
help(tuple.index)
help(tuple.count)
#3
seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq)
#4
print(seq.count(8))
print(seq.index(44))
#5
listseq = list(seq)
#6
print(type(listseq))
#7
listseq.append(999)
print(listseq)

listseq.insert(2, 3)
print(listseq)

listseq.remove(listseq[-1])
print(listseq)

#Словари
#1-2
D = {'food':'Apple', 'quantity':4, 'color':'Red'}
print(D['food'])
D['quantity'] += 10
print(D)
#3-4
dp = {}
dp['name'] = input("Enter name: ")
dp['age'] = int(input("Enter age: "))
print(dp)

#Вложенность хранения данных
#1
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 25}
#2
print('Имя: '+rec['name']['firstname']+', Фамилия: '+ rec['name']['lastname'])
print('Имя: '+rec['name']['firstname'])
print("Список должностей: {job}".format(**rec))
#3
rec['job'].append('janitor')
print(rec['job'])
#4
print("Имя и фамилия: {0}: \n Список должностей: {1} \n Возраст: {2}".format(rec['name'],rec['job'],rec['age'] ))