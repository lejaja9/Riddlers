#January 14 Riddler Classic https://fivethirtyeight.com/features/when-the-riddler-met-wordle/

words_answer = []

with open('1_14_22_Riddler_Classic.txt', 'r') as file:
    for line in file:
        words_answer.append(line.rstrip())

words_all = []

with open('1_14_22_Riddler_Classic_allwords.txt', 'r') as file:
    for line in file:
        words_all.append(line.rstrip())

#function to find green, yellow, and white letters
def decode(guess, real_word):
    ans = ['W', 'W', 'W', 'W', 'W',]
    letter_count = {}
    #first pass for green letters
    for i in range(5):
        if guess[i] == real_word[i]:
            ans[i] = 'G'
        else:
            if real_word[i] in letter_count:
                letter_count[real_word[i]] += 1
            else:
                letter_count[real_word[i]] = 1
    #second pass for yellow letters
    for i in range(5):
        if ans[i] == 'G':
            continue
        else:
            if guess[i] in letter_count and letter_count[guess[i]] > 0:
                ans[i] = "Y"
                letter_count[guess[i]] -= 1
    return tuple(ans)

#function to find constellations
def constellations(guess_word, list_of_words):
    constellations = {}
    for word in list_of_words:
        #print(word)
        if decode(guess_word, word) in constellations:
            constellations[(decode(guess_word, word))].append(word)
        else:
            constellations[decode(guess_word, word)] = [word]
    return constellations

def subconstellations(guess_word, list_of_words):
    constellation = constellations(guess_word, list_of_words)
    subconstellations_count = 0
    counter = 0
    for key in constellation:
        if len(constellation[key]) == 1:
            subconstellations_count += 1
            continue
        else:
            temp = 0
            for word in list_of_words:
                if len(constellations(word, constellation[key])) > temp:
                    temp = len(constellations(word, constellation[key]))
                    #max_word = word
            subconstellations_count += temp
            #print(key, max_word)
            counter += 1
            print(counter)
    return subconstellations_count
