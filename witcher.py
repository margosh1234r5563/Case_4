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
    print(f'{ru.WARNING_1}')
    amount_orders_list.pop(4)
    amount_orders_list.insert(4, 1)
    amount_money = 0
    for s in range(len(cost_creature)):
        amount_money += int(cost_creature[s]) * int(number_creatures_list[s])
        mny_nmbr = amount_money
        counter = 0
        while mny_nmbr >= 25:
            mny_nmbr = mny_nmbr - 25
            counter = counter + 1
        while mny_nmbr >= 10:
            mny_nmbr = mny_nmbr - 10
            counter = counter + 1
        while mny_nmbr >= 5:
            mny_nmbr = mny_nmbr - 5
            counter = counter + 1
        while mny_nmbr >= 1:
            mny_nmbr = mny_nmbr - 1
            counter = counter + 1
            print(f'{ru.MONEY_FOR_ORDERS} {amount_money}')
            print(f'{ru.MINIMAL_MONEY} {counter}')
else:
    amount_money = 0
    for s in range(len(cost_creature)):
        amount_money += int(cost_creature[s]) * int(number_creatures_list[s])
        mny_nmbr = amount_money
        counter = 0
        while mny_nmbr >= 25:
            mny_nmbr = mny_nmbr - 25
            counter = counter + 1
        while mny_nmbr >= 10:
            mny_nmbr = mny_nmbr - 10
            counter = counter + 1
        while mny_nmbr >= 5:
            mny_nmbr = mny_nmbr - 5
            counter = counter + 1
        while mny_nmbr >= 1:
            mny_nmbr = mny_nmbr - 1
            counter = counter + 1
            print(f'{ru.MONEY_FOR_ORDERS} {amount_money}')
            print(f'{ru.MINIMAL_MONEY} {counter}')

print(ru.ITEMS_1)
number_items_list = []
amount_orders_items_list = []

for n in range(1, 5):
    number_items, amount_orders_items = input().split()
    number_items_list.append(number_items)
    amount_orders_items_list.append(amount_orders_items)

print(ru.BLADE_CATEGORY)
amount_orders_blade_list = []
number_blade_list = []
for k in range(1, 5):
    number_blade, amount_orders_blade = map(int, input().split())
    number_blade_list.append(number_blade)
    amount_orders_blade_list.append(amount_orders_blade)

if sum(amount_orders_blade_list) > 1:
    print(ru.QUOTE_1)
cost_blade = 0

for number_blade, amount_orders_blade in zip(number_blade_list, amount_orders_blade_list):
    match number_blade:
        case 1:
            cost_blade += 200 * amount_orders_blade
        case 2:
            cost_blade += 100 * amount_orders_blade
        case 3:
            cost_blade += 200 * amount_orders_blade
        case 4:
            cost_blade += 1500 * amount_orders_blade
        case _:
            print(ru.WARNING_2)


print(ru.DRINK_CATEGORY)
amount_orders_drink_list = []
number_drink_list = []
for k in range(1, 5):
    number_drink, amount_orders_drink = map(int, input().split())
    number_drink_list.append(number_drink)
    amount_orders_drink_list.append(amount_orders_drink)
cost_drink = 0

for number_drink, amount_orders_drink in zip(number_drink_list, amount_orders_drink_list):
    match number_drink:
        case 1:
            cost_drink += 5 * amount_orders_drink
        case 2:
            cost_drink += 10 * amount_orders_drink
        case 3:
            cost_drink += 1 * amount_orders_drink
        case 4:
            cost_drink += 400 * amount_orders_drink


print(ru.ITEMS_2)
for n in range(7, 10):
    number_items, amount_orders = input().split()
    number_items_list.append(number_items)
    amount_orders_items_list.append(amount_orders)

cost_items = [22, 100, 5, 1, 10, 30, 10]

amnt_mny_itms = 0
phase = 1
cost_items.insert(5, 1)
cost_items.insert(6, 1)
number_items_list.insert(5, cost_blade)
number_items_list.insert(6, cost_drink)
for s in range(len(cost_items)):
    while amount_money >= amnt_mny_itms:
        amnt_mny_itms += int(cost_items[s]) * int(number_items_list[s])
    else:
        phase += 1
result = print(ru.QUOTE_2) if amount_money >= amnt_mny_itms else print({ru.OFFENCE},
                                                                       f'Деньги закончились еще на {phase})')
