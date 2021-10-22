#July 16 Riddler Express and Riddler Classic https://fivethirtyeight.com/features/can-you-win-the-penalty-shootout/
import scipy.integrate as integrate



def f(x):
    return (x**2)+(1-x)**2

ans = integrate.quad(f, 0, 1)
print(ans)

def penalty_simulation(p = 0.7):
    team_a = 0
    a_kicks_left = 5
    a_count = 0

    team_b = 0
    b_kicks_left = 5
    b_count = 0

    while True:
        #kick
        team_a_kick = np.random.uniform(0,1)
        a_count += 1
        a_kicks_left -= 1
        if team_a_kick < p:
            team_a += 1
        #check score
        if (a_count + b_count) <= 10:
            if (team_a-team_b > 0 and team_a-team_b > b_kicks_left) or (team_a-team_b < 0 and team_b-team_a > a_kicks_left):
                return (a_count+b_count)
        #kick
        team_b_kick = np.random.uniform(0,1)
        b_count += 1
        b_kicks_left -= 1
        if team_b_kick < p:
            team_b += 1
        #check score
        if (a_count + b_count) <= 10:
            if (team_b-team_a > 0 and team_b-team_a > a_kicks_left) or (team_b-team_a < 0 and team_a-team_b > b_kicks_left):
                return (a_count+b_count)
        if (a_count + b_count) > 10:
            if team_a != team_b:
                return (a_count+b_count)

    # while True:
    #     print(count, team_a, team_b)
    #     team_a_kick = np.random.uniform(0,1)
    #     count += 1
    #     if team_a_kick < p:
    #         team_a += 1
    #     GD = abs(team_a-team_b)
    #     if (count == 7 and GD == 3) or (count == 9 and GD == 2):
    #         print(count, team_a, team_b)
    #         return count
    #     team_b_kick = np.random.uniform(0,1)
    #     count += 1
    #     if team_b_kick < p:
    #         team_b += 1
    #     GD = abs(team_a-team_b)
    #     if (count == 6 and GD == 3) or (count == 8 and GD == 2) or (count >= 10 and count%2 == 0 and GD == 1):
    #         print(count, team_a, team_b)
    #         return count

ans = []
for i in range(10000000):
    ans.append(penalty_simulation())
print(sum(ans)/10000000)