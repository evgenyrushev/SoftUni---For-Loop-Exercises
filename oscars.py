actor_name = input()
academy_points = float(input())
judges = int(input())

for x in range(judges):
    judge_name = input()
    points_given = float(input())

    academy_points += len(judge_name) * points_given / 2

    if academy_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!")
