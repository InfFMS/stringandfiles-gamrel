# Напишите программу, которая просит пользователя ввести несколько предложений
# (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "\("_")/".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.
print('...')
new = input()
with open ('test2.txt', 'w', encoding='utf-8') as f:
  f.write(new)
with open('test2.txt', "r", encoding='utf-8') as f:
  file = f.read()
new = file.upper()
new1 = new.replace(' ', '"\\("_")/"')
with open ('test2.txt', 'w', encoding='utf-8') as f:
  f.write(new1)
with open('test2.txt', "r", encoding='utf-8') as f:
  file = f.read()
  print(file)