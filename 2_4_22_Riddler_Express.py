#February 5 Riddler Express https://fivethirtyeight.com/features/a-riddle-that-will-make-you-scream/

cast_list = ['Cox', 'Arquette', 'Berry', 'Campbell', 'Holland']

def permute(cast):
    guesses = []

    def helper(cume, i):
        if len(cume) == 3:
            guesses.append(cume.copy())
            return
        for j in range(i, len(cast)):
            cume.append(cast[j])
            helper(cume, j+1)
            cume.pop()

    helper([], 0)
    ans = []
    for guess in guesses:
        temp = 0
        if 'Cox' in guess:
            temp += 1
        if 'Arquette' in guess:
            temp += 1
        if 'Campbell' in guess:
            temp += 1
        if temp >= 2:
            ans.append(guess)

    return ans

print(len(permute(cast_list)))