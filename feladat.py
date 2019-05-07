
def isprim(a):
    if a < 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(2, a // 2):
        if a % i == 0:
            return False
    return True

def oszto(x,y):
    for i in range(x+1,1,-1):
            if x%i==0 and isprim(i)==True:
                return i

print(oszto(8,6))
