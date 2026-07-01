age = int(input("Сколько тебе лет? "))

if age >= 18:
    print("Ты совершеннолетний")
else:
    print("Ты несовершеннолетний")

score = int(input("Введи свою оценку (0-100): "))

if score >= 90:
    print("Отлично!")
elif score >= 70:
    print("Хорошо")
elif score >= 50:
    print("Удовлетворительно")
else:
    print("Нужно подтянуть знания")