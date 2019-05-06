
def isprim(val):
    if val<2:
        return False
    for i in range(2,val):
        if val%i==0:
            return False
    return True

def oszto(x,y):
    if x > y:
        temp = x
        x = y
        y = temp
    for i in range(x+1,1,-1):
            if x%i==0 and isprim(i)==True:
                return i

print(oszto(6,8))
