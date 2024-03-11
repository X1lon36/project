import random

print("Здравствуйте, прошу вас выбрать книгу которую хотите преобрести")

book = input('Введите название книги: ')


# выводит стоимость книги

price = int(random.randint(500 , 1200))

print(f"Вы выбрали книгу: {book} , её цена: {price} .")

# Запрашивает сумму у потребителя

sum = int(input('Введите вашу сумму денег: '))

# Вычисляет 

low = (price - sum)

high = (sum - price)


if sum < price:

    print(f'необходимо доплатить: {low}')
elif sum == price:
    print('Спасибо, приходите ещё!')
elif sum > price:
    print(f'Заберите свою сдачу: {high}')

print("\n\n")

input("Для закрытия нажмите Enter!")

