# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
import re
z=0
c=0
a=''
C=''
with open('task5.txt', "r", encoding='utf-8') as f:
  file = f.read()
  new = re.sub(r'[^\w\s]', '', file)
with open('test.txt', 'w', encoding='utf-8') as f:
  f.write(new)
  f.write(' ')
with open('test.txt', "r", encoding='utf-8') as f:
  file = f.read()
  for char in file:
    if char != ' ':
      z += 1
      a+=char
    if char == ' ':
      if c<z:
        c=z
        C=a
      z=0
      a=''
c = str(c)
#print(C,c)
with open ('test3.txt', 'w', encoding='utf-8') as f:
  f.write('Самое длинное слово:')
  f.write(C)
  f.write("\n")
  f.write('Его длина:')
  f.write(c)
with open('test3.txt', "r", encoding='utf-8') as f:
  file = f.read()
  print(file)