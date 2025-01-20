# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
x = ''
with open('task3.txt', "r", encoding='utf-8') as f:
   file1=f.read()
x+=file1
x=x.lower()
c = x.split()
c = sorted(c)
print (c)
x = set(c)
x = sorted(x)
print (x)

from collections import Counter
counts = Counter(c)
print(counts)
