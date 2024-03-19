import ru_local as ru

money = int(input('Какой твой бюджет, бродяга? '))
print(ru.ITEMS)
number_items_list = []
amount_orders_items_list = []

for n in range(1, 5):
    number_items, amount_orders_items = input().split()
    number_items_list.append(number_items)
    amount_orders_items_list.append(amount_orders_items)

cost_items = [22, 100, 5, 1]
amnt_mny_itms = 0
phase = 1
for s in range(len(cost_items)):
    while money >= amnt_mny_itms:
        amnt_mny_itms += int(cost_items[s]) * int(number_items_list[s])
        result_1 = None if money >= amnt_mny_itms else print({ru.QUOTE}, f'Твой долг составил {amnt_mny_itms - money}')
        break
    else:
        phase += 1
result_2 = print(f'{ru.OFFENCE}. Деньги закончились еще на {phase})') if result_1 != None else print(None)
print(ru.BLADE_CATEGORY)
amount_orders_blade_list = []
number_blade_list = []
for k in range(1, 5):
    number_blade, amount_orders_blade = map(int, input().split())
    number_blade_list.append(number_blade)
    amount_orders_blade_list.append(amount_orders_blade)
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

print(cost_blade)


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
amnt_mny_itms_final = 0
for s in range(len(cost_items)):
    amnt_mny_itms_final += int(cost_items[s]) * int(number_items_list[s])
    spendings = amnt_mny_itms_final + cost_blade + cost_drink
    amnt_mny_itms_final += cost_blade
print(amnt_mny_itms_final)
print(money - amnt_mny_itms_final)
