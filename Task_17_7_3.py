per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму, которую вы планируете положить под проценты: "))
deposit = list(map(lambda value: money * value / 100, per_cent.values()))
print("Накопленные средства за год:", deposit)
max_value = max(deposit)

print(f"Максимальная сумма, которую вы можете заработать — {max_value}")