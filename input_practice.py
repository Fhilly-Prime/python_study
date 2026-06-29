#задание 1

name = input("Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
birth_year = 2026 - age
age_2030 = 2030 - birth_year

print("Привет, " + name + "!")
print("Тебе " + str(age) + " лет")
print("Год твоего рождения: " + str(birth_year))
print("В 2030 году тебе будет: " + str(age_2030))

#задание 2
goods = input("Введите название товара: ")
price = input("Введите стоимость товара: ")
count = input("Введите количество товара: ")
total = int(price) * int(count) 

print("Товар: " + goods.title())
print("Цена: " + price + " рублей")
print("Количество: " + count)
print("Итого: " + str(total) + " рублей")