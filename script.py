money=int(input("Введите сумму"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB=int(round((per_cent['ТКБ']*0.01)*money))
SKB=int((per_cent['СКБ']*0.01)*money)
VTB=int((per_cent['ВТБ']*0.01)*money)
SBER=int((per_cent['СБЕР']*0.01)*money)
deposit=[TKB,SKB,VTB,SBER]
print(deposit)
max_sum=max(deposit)
print('Максимальная сумма, которую вы можете заработать-',max_sum)


