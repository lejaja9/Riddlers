# Riddlers!

Hi! Here is my repository for [538's weekly Riddler puzzles](https://fivethirtyeight.com/tag/the-riddler/) and more! The files in this repo are my code for either 538's bite-sized *Riddler Express* and/or their more challenging *Riddler Classic* in addition to any riddles I come across (usually while running or chatting with my run friends). I explain my code for each riddle below. Enjoy!

* **Riddles.py**
    ⋅⋅* While on a run, my friend gave me a teaser: approximate pi given a random number generator. Whatttttt?!?! Luckily, another friend casually mentioned that it was "throwing darts on a dartboard." For the next few miles, I was tortoured by this question, and near the end of the run it hit me: Area = pi*r^2. If r = 1, area would just equal pi. So back to throwing darts... if I were to throw darts onto a unit square that encompasses a circle, the probability that the dart would be in the circle would be (area of circle)/(area of square)... some quick maths gave the proportion Probabilty(dart in circle) = pi/4. I used a random generator to generate (x,y) points in an 18x18 square (because my favorite number is 9). If the point was less than 9 units away from the center (9,9), the point was in the circle. 

