# Riddlers!

Hi! Here is my repository for [538's weekly Riddler puzzles](https://fivethirtyeight.com/tag/the-riddler/) and more! The files in this repo are my code for either 538's bite-sized *Riddler Express* and/or their "slow puzzle movement" *Riddler Classic* in addition to any riddles I come across (usually while running or chatting with my run friends). I explain my logic for each riddle below. Enjoy!

* **[Riddles.py](Riddles)**
    * 10/25 Riddle
        * *If a stick of length x is broken into three pieces, what is the probability that the three pieces can be used to construct a triangle?*
        
            So I actually came across this problem (not on a run, for once) while browsing through Math Stack Exchange, and it ate at me throughout the day until I had an "a-ha" moment while making myself a mid-day snack in the kitchen (cereal, to be exact).
            ![](Vizes/1025/1025line1.png)
            Let's assume, for simplicity's sake, that the length of the stick is 1. *Thus, in order for the pieces to construct a triangle, the longest piece has to be less than the length 1/2*. Now, let's assume that we randomly first break the stick at a point on the left half of the stick. If the first point is on the very left edge of the stick, there is no "sweet spot" where the second point could be and still form a triangle, because any subsequent point will result in one segement greater than the length of 1/2.
            ![](Vizes/1025/1025line2.png)
            Let's move toward the center and see what happens. If the first break is at the "1/4th point" of the line, we see a highlighted "sweet spot" on the right half of the line of length 1/4 in which if the second breaking point is in that spot, the pieces form a triangle.
            ![](Vizes/1025/1025line3.png)
            Let's move even closer, now to the "3/4th point" of the line. We can see now that the "sweet spot" increases even more to length 3/4... are we starting to see a pattern?
            ![](Vizes/1025/1025line4.png)
            As the breaking point moves by x into the center, the space of the "sweet spot" increases by  x (in fact, it stretches out from the center of stick by length x). Thus, I integrated x from 0 to 0.5 (because we are only considering points on the left half of the stick) and multiplied the answer by 2 (to account for the fact that the first point can be either on the left half or right half of the stick). I found the probability to be **1/4**.
            ![](Vizes/1025/1025integral.png)
    * 10/20 Riddle
        * While on a run, my friend gave me a teaser: approximate pi given a random number generator. *Whatttttt?!?!* For the next few miles, I was tortured by this question, and thankfully someone mused: "It's just throwing darts on a board." It hit me: Area = pi*r^2. If r = 1, area would just equal pi. In a 2x2 square (or as I found out, any square), the probability a dart would be in the circle is pi/4.
        From there, I used a random generator to generate (x,y) points in an 18x18 square (because my favorite number is 9). If the point was less than 9 units away from the center (9,9), the point was in the circle. If more than 9 units away, it was not. 
            ```python
            x = np.random.uniform(0, 18)
            y = np.random.uniform(0, 18)
            distance = np.sqrt((x-9)**2 + (y-9)**2)
            if distance < 9:
                nume += 1
            ```
            Simple algebra yieled the answer: pi = 4*(darts in circle)/(total number of throws).
            To be clear, I am still very scared to see whats in store next week at run club.

* **[10/15/21 Riddler Express](https://fivethirtyeight.com/features/can-you-hit-these-riddles-out-of-the-park/)**
    * Since the first team to 4 wins wins, and Team A wins p% of the time, I created a recursive function that ends when one team hits 4 wins and weigh a Team A win at p% and a Team B win at (1-p)%. The answer is **5.8125**.
    This question can also be solved via binomial distribution: the probability that the series ends after 4 games is (4C0) * (p)^4 * (1-p)^0 + (4C0) * (p)^0 * (1-p)^4 (so 4-0 or 0-4), or 0.125 if p = 0.5. We can do this for 5, 6, and 7 games and find the weighted average, which will also yield the answer 5.8125. Kudos to anyone with the patience to do this by hand!

* **[10/08/21 Riddler Express](https://fivethirtyeight.com/features/can-you-evade-your-evil-twin/)**
    * We know that the jackpot is worth $10m, each ticket costs $1, and 10 other tickets will be winning tickets (from the time travelers). Thus, our payout is the function f(x) = ($10m/(10+x))-x. We can easily take the first derivative, or alternatively I maximized the function with SciPy to find that the optimal number of tickets is **9990** with a payout of $9,980,010. With that kind of money, the first thing I would buy is a new house for my mom... and then I would buy a slightly bigger house for myself.

* **[09/24/21 Riddler Classic](https://fivethirtyeight.com/features/can-you-climb-your-way-to-victory/)**
    * For this Riddler, I ran 10 million Monte Carlo simulations to find the answer of **48**. Knowing that there were 3 events for the 8 contestants, I shuffled the 3 lists and had each index represent a contestant:
        ```python
        list1 = shuffle(list(range(1,9)))
        list2 = shuffle(list(range(1,9)))
        list3 = shuffle(list(range(1,9)))
        for i in range(8):
            score = list1[i]*list2[i]*list3[i]
        ```
        For an example, my three lists of [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8] could be shuffled into  [6,7,1,3,4,2,8,5], [5,2,6,3,4,7,1,8], [8,6,4,5,1,3,2,7]. Thus, player 1 (at index 0) would have a final score of 6x5x8 = 240 and player 2 (at index 1) would have a final score of 7x2x6 = 84. I would do this for every player and return the minimum and maximum scores. I found the maximum of the minimum (winning) scores to be 48 and the minimum of the maximum (losing) scores to be 60.
        I made a heatmap and bar charts to show the distribution of scores from my simulations.
        
        Heatmap:
        ![](Vizes/0924/0924heatmap.png)
        Distribution of Winning Scores:
        ![](Vizes/0924/0924winscorebarh.png)
        Distribution of Losing Scores:
        ![](Vizes/0924/0924losescorebarh.png)

* **[08/13/21 Riddler Express](https://fivethirtyeight.com/features/are-you-clever-enough/)**
    * To solve this Riddler, we need to use binomial distribution. 
    Lets say among the 9 other people, 1 is in the top 90% (so 8 are in the bottom 90%). The probability that exactly other 1 person is in the top 90% is (9C1) * (0.9)^8 * (0.1)^1, or around 38.7%. With you and the 1 other person in the top 90% (a little Bayes' here), the probability you are the top Riddler is 38.7% * 1/2 = 19.4%. To reiterate, with 1 other person in the top 90%, you have a 19.4% change of being the top Riddler. I calculated these probabilities given that 0, 1, 2, 3, ..., 9 others in the group are in the top 90%, summed the probabilities, and found an answer of approximately **65.13%**. The key line of my code is seen here:
        ```python
        percent_cleverest = (math.comb(9,i)*((0.9)**(9-i)*(0.1**(i)))*(1/(1+i)))
        ```

* **[07/30/21 Riddler Express](https://fivethirtyeight.com/features/will-riddler-nation-win-gold-in-archery/)**
    * At first glance, we can see that the expected score of Riddler Nation is 24. Isn't that convenient! At second glance, however, I realized that the distribution of scores may not be symmetric: for an example, a 99% chance of scoring 0 and a 1% chance of scoring a 2400 also yields an expected score of 24, but no way the odds of each team winning are 50-50.
    I found the 27 permutations for the series of 3 shots and counted the total number of permutations below, at, and above 24 points (10, 6, and 11). Because we know that the ties go into another 3 shots, the answer is 11/21, or the number of permutations that Riddler Nation scores above 24 divided by the number of all non-tying outcomes.

* **[07/30/21 Riddler Express](https://fivethirtyeight.com/features/can-you-hop-across-the-chessboard/)**
    * This Riddler may have the 'Express' suffix, but I promise you that coding this algorithm was not express at all!
    I created a matrix of the chess pieces and all the possible moves for each piece, as seen below:
        ```python
        matrix = [
        ['K', 'BL', 'b', 'BL', 'K', 'r', 'b', 'r'],
        ['n', 'r', 'n', 'n', 'p', 'n', 'K', 'b'],
        ['r', 'BL', 'n', 'BL', 'p', 'r', 'p', 'r'],
        ['BL', 'BL', 'p', 'r', 'BL', 'n', 'BL', 'BL'],
        ['n', 'n', 'n', 'b', 'BL', 'b', 'r', 'b'],
        ['q', 'r', 'n', 'p', 'BL', 'n', 'r', 'q'],
        ['BL', 'BL', 'r', 'p', 'b', 'p', 'b', 'q'],
        ['K', 'b', 'q', 'n', 'p', 'r', 'n', 'n']]
        #initial position is matrix[6][4], bishop
        b_moves = [[1,1], [1,-1], [-1,-1], [-1,1]]
        r_moves = [[1,0], [-1,0], [0,1], [0,-1]]
        n_moves = [[-1,2], [-2,1], [-2,-1], [-1,-2], [1,-2], [-2,1], [2,1], [1,2]]
        p_moves = [[-1,-1], [-1,1]]
        q_moves = b_moves+r_moves
        ```
        I then wrote a DFS helper function which took the initial Bishop and moved it in every way possible. From there, I took each piece from the new square that the bishop could have moved into and moved that new piece in every way possible. I kept doing this until a piece either moved into the King's square or a black piece's square. I found three paths to reach a King:
        * 1. [(6, 4, 'Bishop'), (5, 3, 'Pawn'), (4, 2, 'Knight'), (5, 0, 'Queen'), (4, 1, 'Knight'), (2, 2, 'Knight'), (1, 4, 'Pawn'), (0, 5, 'Rook'), (0, 4, 'King')]
        * 2. [(6, 4, 'Bishop'), (5, 3, 'Pawn'), (4, 2, 'Knight'), (5, 0, 'Queen'), (4, 1, 'Knight'), (2, 2, 'Knight'), (1, 0, 'Knight'), (0, 2, 'Bishop'), (1, 3, 'Knight'), (2, 5, 'Rook'), (3, 5, 'Knight'), (1, 6, 'King')]
        * 3. [(6, 4, 'Bishop'), (5, 3, 'Pawn'), (4, 2, 'Knight'), (5, 0, 'Queen'), (4, 1, 'Knight'), (2, 2, 'Knight'), (1, 0, 'Knight'), (0, 2, 'Bishop'), (1, 1, 'Rook'), (1, 2, 'Knight'), (0, 0, 'King')]


* **[07/16/21 Riddler Express and Classic](https://fivethirtyeight.com/features/can-you-win-the-penalty-shootout/)**
    * **Express:**
    For the sake of simplicity, let's assume that the length of the stick is 1. When Fatch fetches the stick (say that 10 times fast), we know that the top portion will be painted black and the bottom portion white. We can denote the black area with length x and the white area with length 1-x (note that black + white = 1).
    We want to know the probability Fetch and Fitch fetch the stick by biting in the same colored area, which will be black-black, (x)^2, or white-white, (1-x)^2, so x^2 + (1-x)^2. Because Fatch bites the stick at a random point, we know that the length of x (and thus the length of 1-x) will be distributed uniformly from 0 to 1. We can integrate the equation above from the interval (0,1) (I lost my handy TI-84 so I put it into SciPy) to find our answer of **0.667**.
    
    	![](Vizes/0716expressintegral.png "Photo credits goes to WolframAlpha")
    
    	I found this problem three times as difficult as usual due to the fact that I had to (1) do the math, (2) keep up with the names of Fatch, Fetch, and Fitch         (which somehow are *way* more confusing than Kim, Khloe, and Kourtney), and (3) decide whether I would integrate by hand, WolframAlpha, SciPy, or spend the         effort trying to find my TI-84.
    * **Classic**
    The math for this Riddler looked scary, and it was getting late, so I decided to run simulations to get the answer. As you can see in my code, the hardest part was coding the stop conditions... with my initial 'if statements', I kept missing edge cases. After calling my good friend for help, we figured out that a more straightfoward process would be not to find every case in which the shootout would end but to use a general case, which ended up being if *goal difference > goals remaining*. We can see this in my code:
        ```python
        if (team_a-team_b > 0 and team_a-team_b > b_kicks_left) or (team_a-team_b < 0 and team_b-team_a > a_kicks_left):
            return (a_count+b_count)
        ```
        Because there is the case of overtime (tied after 5 rounds, or 10 shots), I had to add a second condition to account for this:
        ```python
        if (a_count + b_count) > 10:
        if team_a != team_b:
            return (a_count+b_count)
        ```
        I ran 10 million simulations and found the average number of shots to be around **10.47**. Go Tottenham Hotspurs!

* **[07/09/21 Riddler Express](https://fivethirtyeight.com/features/can-you-solve-this-astronomical-enigma/)**
    * **Express:**
    For this brute force solution, I used Math's GCD function to find pairs of numbers between 1 and 20 that were relatively prime. I then threw the pair of numbers into my years function, which would find keep finding multiples of each number in the pair until the difference between two multiples was 1, which would result in an interference.
        ```python
        def years(num1, num2):
            sum1 = 0
            sum2 = 0
            while abs(sum1-sum2) != 1:
                if sum1 <= sum2:
                    sum1 += num1
                else:
                    sum2 += num2
            return [num1, num2, max(sum1, sum2)]
        ```
        I found the answer to be **153 years**, when one brood of cicadas emerges every 19 years and the other emerges every 17 years. I made a table (below) to show the latest possible interference for every pair cicada broods:
        ![](Vizes/0709scatter.png)
