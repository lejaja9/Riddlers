#Project Euler Question 88 https://projecteuler.net/problem=88
import math
import collections

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False    

    return True


def factorization(upper_limit):
    factors = [[], [], [[2]], [[3]], [[2,2], [4]], [[5]]]
    minimal_product_n = [float('Inf')]*(upper_limit+1)
    minimal_product_n[0] = 0
    minimal_product_n[1] = 0
    minimal_product_n[2] = 4
    for n in range(6, upper_limit+1):
        n_factorization = [[n]]
        n_set = []
        if isPrime(n):
            factors.append(n_factorization)
            continue
        else:
            for i in range(2, math.floor(n/2)+1):
                #print(n, i)
                if n%i == 0:
                    for first_factor in factors[i]:
                        for second_factor in factors[int(n/i)]:
                            temp = first_factor + second_factor
                            # if n == 32:
                            #     print(temp)
                            if collections.Counter(temp) not in n_set:
                                n_set.append(collections.Counter(temp))
                                n_factorization.append(temp)
                                #update minimal product-sum number
                                leading_ones = n - sum(temp)
                                k = leading_ones + len(temp)
                                minimal_product_n[k] = min(minimal_product_n[k], n)
            factors.append(n_factorization)
    return minimal_product_n, factors

minimal_product, factorize = factorization(24000)
print(sum(set(minimal_product[:12001])))



#debug
# debug_dict = {}
# with open('Riddles/Euler_88_debut.txt', 'r') as file:
#     for line in file:
#         line = line.strip()
#         index = line.find(' ')
#         debug_dict[int(line[:index])] = int(line[index+1: ])

# for i in range(1, 10000):
#     if test[i] != debug_dict[i]:
#         print(i, debug_dict[i], test[i])
