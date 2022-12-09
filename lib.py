def fEbanachi(n):
    import numpy as np
    numbx = np.zeros(n)
    numby = np.zeros(n)
    fib1 = fib2 = 1
    numbx[0] = fib1
    numbx[1] = fib2
    for i in range(2,n):
        fib1, fib2 = fib2, fib1 + fib2
        numbx[i]=fib2
    for i in range(n):
        numby[i]=i+1
    list = numbx.tolist()
    for i in range(len(list)):
        list[i]=int(list[i])
    return list

def calc(a,b,znak):
    if znak == '+':
        return  a+b
    elif znak == '-':
        return  a-b
    elif znak == '*':
        return  a*b
    else:
        return  a/b

def sort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(0,length-i-1):
            if array[j] > array [j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


