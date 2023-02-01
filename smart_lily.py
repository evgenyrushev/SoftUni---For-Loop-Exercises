age_lily = int(input())
washing_machine = float(input())
toy_price = int(input())

money_given = 10
brother_takes = 1
money_from_toys = 0
money_from_gifts = 0

for x in range(1, age_lily + 1):

    if x % 2 == 0:
        money_from_gifts += money_given - brother_takes
        money_given += 10
    else:
        money_from_gifts += toy_price

if money_from_gifts >= washing_machine:
    print(f"Yes! {money_from_gifts - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - money_from_gifts:.2f}")
