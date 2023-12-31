# Допустим, вы воспользовались методом строки и получили новую строку:
print("Ваня любит яблоки".replace("Ваня","Алёша"))
print("Алёша любит яблоки")

# Переменные — это способ выдернуть строку Алёша любит яблоки из всего этого процесса и сохранить её в памяти компьютера:
my_variable = "Ваня любит яблоки".replace("Ваня","Алёша")
print(my_variable)

# Переменные удобны, когда одно значение используется многократно:
unit_cost = 20
print("Цена штуки", unit_cost)
print("Цена десятка", 10 * unit_cost)
print("Цена дюжины", 12 * unit_cost)

# Или когда нужно выполнить много действий подряд. Когда мы делаем всё сразу в одной строчке, становится немного непонятно:
print("Сказка о том, как %зверь% съел %еда%. Жил был %зверь% в своей %дом% и ел %еда% Конец.".replace("%зверь%","кролик").replace("%дом%","норке").replace("%еда%","моркву"))


# Переменные позволяют разделить код на несколько строк:
string = "Сказка о том, как %зверь% съел %еда%. Жил был %зверь% в своей %дом% и ел %еда% Конец."
string = string.replace("%зверь%","кролик")
string = string.replace("%дом%","норке")
string = string.replace("%еда%","моркву")
print(string)

# Можно повесить название my_variable на новую штуку:
my_variable = "Алёша лубит яблоки"
my_variable = "Новый текст"
print(my_variable)

# Одна переменная ссылается только на один объект:
variable1 = "Мой текст"
variable2 = "Мой текст"
print(variable1)
print(variable1)

# numbers = 10
#
# while numbers < 100:
#     print(numbers)
#     numbers += 10
# else:
#     print(f'{numbers} работа цыкла завершена')
# message = 'Hello World'
#
# for leater in message:
#     print(leater)

x = 5
y = 10

x = x + y # 15 = 5 + 10
y = x - y # 5 = 15 - 10
x = x - y # 10 = 15 - 5

print(x)
print(y)



x = 5
y = 10

x, y = y, x

print(x)
print(y)
