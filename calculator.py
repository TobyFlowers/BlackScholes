import math
from scipy.stats import norm
import numpy as np

def calculatePrice(St, K, r, t, o): #for a call
    d1 = solveD1(St, K, r, t, o)
    t1 = norm.cdf(d1)*St 
    t2 = norm.cdf(solveD2(d1, t,o))*K*math.pow(math.e,(-1*r*t))
    return t1-t2


def paritySolver(P_call, St, K, r, t): #solve for put price
    return -(St - P_call - K*math.pow(math.e,(-1*r*t)))

def solveD1(St, K, r, t,o):
    n = (np.log(St/K)) + (r + np.square(o)/2)*t
    d = o*np.sqrt(t)
    return n/d

def solveD2(d1, t, o):
    return d1 - o*np.sqrt(t)

print(calculatePrice(100,100,0.1,1,0.2))
print(paritySolver(calculatePrice(100,100,0.1,1,0.2), 100,100,0.1,1))


