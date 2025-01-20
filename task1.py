# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
x=0
y=0
z=0
with open('task1.txt', "r", encoding='utf-8') as f:
   file=f.read()

line_count = sum(1 for line in open('task1.txt'))
for line in file:
   x += len(line.split())
for char in file:
   if char != ' ':
      z+=1


#print(x)
#print(z)
print('Средняя длина слова в русской литературе - 6 символов. 152/6 =', x/6, 'что близко к правде)')
print('Кол.во строк:',line_count)
print('кол.во слов во всем тексте файла:',len(file)-line_count-z)
print('Общее количество символов:',len(file)) #с учетом /n
#print((file))
