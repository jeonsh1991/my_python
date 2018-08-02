def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
        print(result)
    return result


num = int(input("구구단:"))
GuGu(num)