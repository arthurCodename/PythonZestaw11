import random
import numpy as np

def genlista(n):
    return random.sample(range(n), n)

print("Assignment a:" ,genlista(5))

def genlistb(n):
    if n >= 100:
        x = (int)(n/10)
    elif n >=10: 
        x = 9
    else: 
        x= 4 
    numbers = []
    for i in range(0, n):
        if i%x == 0:
            numbers.append(random.randint(0,n))
        else:
            numbers.append(i)
    return numbers

print("Assignment b:" ,genlistb(5))

def genlistc(n):
    return [ele for ele in reversed(genlistb(n))]

print("Assignment c:" ,genlistc(5))

def genlistd(n):
    return np.random.normal(size=n)


print("Assignment d:" ,genlistd(5))


def genliste(n):
    setk = genlista(random.randint(1, n-1))
    arr = []

    for i in range(n):
        arr.append(setk[random.randint(0, len(setk) - 1)])
    return arr

print("Assignment e:" ,genliste(5))