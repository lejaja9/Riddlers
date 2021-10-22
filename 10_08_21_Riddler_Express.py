#Oct 8 Riddler Express https://fivethirtyeight.com/features/can-you-evade-your-evil-twin/
import numpy as np
from scipy.optimize import minimize

def f(x):
    y = ((10000000)*(x/(x+10)))-x
    return -y

x0 = np.array([1000]) #guess
ans = minimize(f, x0, method = "Nelder-Mead", options = {'disp': True})
print(str(ans.x))