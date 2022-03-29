ticket = int(input('Введите количество билетов: '))
sum_tic = 0.0
for i in range(ticket):
    age = int(input('Введите возраст: '))
    if age < 18:
        sum_tic = sum_tic + 0
    elif 18 <= age < 25:
        sum_tic = sum_tic + 990
    else: sum_tic = sum_tic + 1390
    if ticket > 3:
        sum_tic = sum_tic * 0.9
print('Итого'+ ' ' + str(round(sum_tic)) + ' ' + 'рублей')


