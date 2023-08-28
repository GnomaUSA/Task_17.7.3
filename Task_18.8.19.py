amount_ticket = int(input ("Введите количество билетов:\t"))
total_sum = []
for age in range(amount_ticket):
   age = int(input("Введите возвраст посетителя:\t"))
   if 0< age < 18:
      print("Билет бесплатный")
   if 18 <= age < 25:
      total_sum.append(int(990))
      print("Цена билета 990 рублей")
   if 25<= age <100:
      total_sum.append(int(1390))
      print("Цена билета 1390 рублей")
   if age <= 0 or age >= 100:
      raise ValueError("Не может быть!")
      print(ValueError)
print("Стоимость билетов:\t",sum(total_sum))
if amount_ticket >3:
   discount = sum(total_sum) - sum(total_sum)//100*10
   print("Цена с учетом скидки:\t", discount)
   print("Ваша скидка составляет:\t", sum(total_sum)//100*10)
