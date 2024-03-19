import ru_local as ru


def main():
    print(ru.CREATURES)
    amount_orders_list = []

    cost_basilisk = 200 / 2
    cost_striga = 3000 * 6.6
    cost_creature = [50, 50, 150, cost_basilisk, cost_striga]

    for n in range(5):
        amount_orders = input(f'{ru.AMOUNT_1} {ru.CREATURES_AMOUNT[n]}')
        amount_orders_list.append(amount_orders)

    if int(amount_orders_list[4]) > 1:
        print(f'{ru.WARNING_1}')
        amount_orders_list.pop(4)
        amount_orders_list.insert(4, 1)
        amount_money = 0
        for s in range(len(cost_creature)):
            amount_money += int(cost_creature[s]) * int(amount_orders_list[s])
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

    else:
        amount_money = 0
        for s in range(len(cost_creature)):
            amount_money += int(cost_creature[s]) * int(amount_orders_list[s])
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
    amount_orders_items_list = []

    for n in range(1, 5):
        amount_orders_items_1 = int(input(f'{ru.AMOUNT_1} {ru.ITEMS_1_AMOUNT[n - 1]}'))
        amount_orders_items_list.append(amount_orders_items_1)

    print(ru.BLADE_CATEGORY)
    amount_orders_blade_list = []
    number_blade_list = [1, 2, 3, 4]
    for k in range(1, 5):
        amount_orders_blade = int(input(f'{ru.AMOUNT_2} {ru.BLADE_AMOUNT[k - 1]}'))
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
    number_drink_list = [1, 2, 3, 4]
    for k in range(1, 5):
        amount_orders_drink = int(input(f'{ru.AMOUNT_3} {ru.DRINK_AMOUNT[k - 1]}'))
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
        amount_orders = int(input(f'{ru.AMOUNT_4} {ru.ITEMS_2_AMOUNT[n - 7]}'))
        amount_orders_items_list.append(amount_orders)

    a = int(cost_blade)
    b = int(cost_drink)
    phase = 0
    cost_items = [22, 100, 5, 1, 1, 1, 10, 30, 10]
    amnt_mny_itms = [0] * len(cost_items)
    number_items_list = [1, 2, 3, 4, a, b, 7, 8, 9]
    for s in range(len(cost_items)):
        amnt_mny_itms[s] = cost_items[s] * number_items_list[s]

    for i in range(len(amnt_mny_itms)):
        while amount_money >= 0:
            amount_money -= amnt_mny_itms[i]
            phase += 1

    print(ru.QUOTE_2) if amount_money >= sum(amnt_mny_itms) else print(f'{ru.OFFENCE}, Деньги закончились на {phase}')

    def debt(amount_money, amnt_mny_itms):
        if amount_money >= sum(amnt_mny_itms):
            return None
        return abs(amount_money - sum(amnt_mny_itms))

    print(f'Ваш долг: {debt(amount_money, amnt_mny_itms)}')


if __name__ == '__main__':
    main()