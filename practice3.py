#1
hour = int(input("Введите час (0-23): "))

if hour >=6 and hour <= 11:
    print("Доброе утро")
elif hour >= 12 and hour <=17:
    print("Добрый день")
elif hour >= 18 and hour <= 23:
    print("Добрый вечер")
else:
    print("Доброй ночи")

#2
password = "python123"
pas = input("Введите пароль: ")

if pas == password:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#3
number = int(input("Введите число: "))

if number > 0 and number != 0:
    print("Положительное")
    if number % 2 == 0:
        print("Четное")
    else:
        print("Не четное")
elif number < 0:
    print("Отрицательное")
else:
    print("Ноль")

age = int(input("Введите возраст: "))
has_license = input("Есть права? (да/нет): ")

if age >= 18 and has_license == "да":
    print("Можешь ездить!")
elif age >= 18 and has_license == "нет":
    print("Возраст подходит, но нет прав")
elif age < 18 and has_license == "да":
    print("Права есть, но ещё молодой")
else:
    print("Ни возраста, ни прав")