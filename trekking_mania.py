groups = int(input())

musala = 0
monblan = 0
kili = 0
k2 = 0
everest = 0

people = 0

for x in range(groups):
    people_per_group = int(input())

    if people_per_group <= 5:
        musala += people_per_group
    elif people_per_group <= 12:
        monblan += people_per_group
    elif people_per_group <= 25:
        kili += people_per_group
    elif people_per_group <= 40:
        k2 += people_per_group
    else:
        everest += people_per_group
people = musala + monblan + kili + k2 + everest

musala = musala / people * 100
monblan = monblan / people * 100
kili = kili / people * 100
k2 = k2 / people * 100
everest = everest / people * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kili:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")
