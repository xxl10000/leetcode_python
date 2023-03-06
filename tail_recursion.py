def myPow(a, b):
    if b == 1:
        return a
    if b % 2:
        #return a * myPow(a, b // 2) ** 2
        return a * myPow(a, b - 1) 
        
    else:
        #return myPow(a, b// 2) ** 2
        return myPow(a * a, b//2)

# total * a^b 表示 pow(a, b), total 表示当tailPow参数里面a,b变化total的值

def tailPow(a, b, total = 1):
    #print(a, b, total)
    if b == 1:
        return total * a
    if b % 2:
        return tailPow(a, b - 1, total * a)
    else:
        
        return tailPow(a * a, b //2, total) 

#将尾递归改成循环
def iterPow(a, b):
    res = 1
    while b > 0:
        if b % 2 :
            b -= 1
            res *= a
        else:
            a *= a
            b //= 2
    return res

print(iterPow(2, 11))
print(tailPow(2, 10))