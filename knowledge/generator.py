# 杨辉三角
def f():
    #if n == 0: return [[1]]
    # res = []
    # res.append([1])
    res = [1]
    #yield res
    while True:
        yield res
        line = [1]
        for j in range(1, len(res)):
            line.append(res[j - 1] + res[j])
        line.append(1)
        res = line[:]
        
    #return res

tri = f()
print(type(tri))
n = 0
for v in f():
    print(v)
    n += 1
    if n > 5:
        break