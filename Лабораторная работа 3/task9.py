salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
month = 10

while month > 0:
    delta = spend - salary
    money_capital += delta
    spend *= 1 + increase
    month -= 1

print(round(money_capital))
