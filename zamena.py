# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
a=0
with open('task2.txt', "r", encoding='utf-8') as f:
   file=f.read()
#print((file))
w='Python'
c = file.count(w)
new = file.replace('Python', 'Питон')

with open ('test.txt', 'w', encoding='utf-8') as f:
  f.write(new)
with open('test.txt', "r", encoding='utf-8') as f:
      file = f.read()
print((file))
print('количестве произведённых замен:',c)
