age = int(input("Введите ваш возраст: "))
knowledge = input("Знаете ли вы Python? (да/нет): ")
exp = input("Есть ли опыт работы? (да/нет): ")
age_sum = 18 - age

if age >= 18 and knowledge == "да" and exp == "да":
    print("Вы приняты!")
elif age >= 18 and knowledge == "да" and not exp == "да":
    print("Возможная стажировка")
elif age >= 18 and not knowledge == "да":
    print("Нужно подучиться")
else:
    print("Приходите через", age_sum, "лет")