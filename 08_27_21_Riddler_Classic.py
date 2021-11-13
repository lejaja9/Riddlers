#August 27 Riddler Classic https://fivethirtyeight.com/features/can-you-draft-a-riddler-fantasy-football-dream-team/

import math

#James Harrison is #92 and thus Hames Jarrison has #29
def move(my_position, two_nine_position, speed):
    #start at (0,50)
    #Hames Jarrison starts at (0,0)
    dx = my_position[0]-two_nine_position[0]
    dy = my_position[1]-two_nine_position[1]
    distance = math.sqrt(dx**2 + dy**2)

    my_position[0] -= dx*(speed/distance)
    my_position[1] -= dy*(speed/distance)
    return my_position

def run(my_speed, me = [0, 50], Hames_Jarrison = [0,0]):
    speed = my_speed*0.001

    while me[0] <= Hames_Jarrison[0]:
        me = move(me, Hames_Jarrison, speed)
        Hames_Jarrison[0] += 0.001
    return Hames_Jarrison[0]


#binary search
low = 1.09
high = 1.5

while (high-low) > 0.000001:
    mid = (low+high)/2
    pos = run(mid, [0, 50], [0,0])
    #print(mid, pos)
    if pos > 100:
        low = mid
    else:
        high = mid
print(low, high)

#1.2807822227478027 1.2807830047607422