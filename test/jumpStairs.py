def climbStairs(n):
    if 0 <= n <= 2:
        return n
    a = 1
    b = 2
    for i in range(3, n + 1):
        temp = a + b
        a = b
        b = temp
    return temp    #return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(100))