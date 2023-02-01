n = int(input())
paycheck = int(input())


for _ in range(n):
    x = input()

    if x == "Facebook":
        paycheck -= 150
    elif x == "Instagram":
        paycheck -= 100
    elif x == "Reddit":
        paycheck -= 50

    if paycheck <= 0:
        print("You have lost your salary.")
        break

else:
    print(paycheck)
