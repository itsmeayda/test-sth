def cakeinQuera(n) :
    lst = [1,2,3,4,6,12]
    for i in lst :
        if n in lst :
            return "YES"
        else :
            return "NO"

n = int(input())
print(cakeinQuera(n))