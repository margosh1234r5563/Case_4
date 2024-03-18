import ru_local as ru

print(ru.CREATURES)
number_creatures_list = []
amount_orders_list = []

cost_basilisk = 200 / 2
cost_striga = 3000 * 6.6
cost_creature = [50, 50, 150, cost_basilisk, cost_striga]

for n in range(1, 6):
    number_creatures, amount_orders = input().split()
    number_creatures_list.append(number_creatures)
    amount_orders_list.append(amount_orders)

if int(amount_orders_list[4]) > 1:
    print(f'{ru.WARNING}')
else:
    amount_money = 0
    for s in range(len(cost_creature)):
        amount_money += int(cost_creature[s]) * int(number_creatures_list[s])

    counter = 0

    n = amount_money
    counter = 0

    while n >= 25:
        n = n - 25
        counter = counter + 1
    while n >= 10:
        n = n - 10
        counter = counter + 1
    while n >= 5:
        n = n - 5
        counter = counter + 1
    while n >= 1:
        n = n - 1
        counter = counter + 1

    print(f'{ru.MONEY_FOR_ORDERS} {amount_money}')
    print(f'{ru.MINIMAL_MONEY} {counter}')



