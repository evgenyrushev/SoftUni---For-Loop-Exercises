import sys
n = int(input())
max_number = -sys.maxsize
amount = 0

for i in range(n):
    numbers = int(input())

    if numbers > max_number:
        max_number = numbers

    amount += numbers

amount -= max_number

if max_number == amount:
    print(f"Yes\nSum = {max_number} ")
else:
    print(f"No\nDiff = {abs(max_number - amount)}")
