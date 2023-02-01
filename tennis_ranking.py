import math
number_tournaments = int(input())
entry_points = int(input())
points_won = 0
tournaments_won = 0

for x in range(number_tournaments):
    finish = input()

    if finish == "W":
        points_won += 2000
        tournaments_won += 1
    elif finish == "F":
        points_won += 1200
    elif finish == "SF":
        points_won += 720

print(f"Final points: {entry_points + points_won}")
print(f"Average points: {math.floor(points_won / number_tournaments)}")
print(f"{tournaments_won / number_tournaments * 100:.2f}%")


