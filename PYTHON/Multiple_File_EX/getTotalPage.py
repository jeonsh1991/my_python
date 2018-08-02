def getTotalPage(m,n):
    if m % n == 0:
        print(m//n)
        return m // n
    else:
        print(m//n+1)
        return m // n + 1


getTotalPage(30,10)