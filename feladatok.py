

def kozos(num1,num2):
    big=0
    small=0
    ko=[]
    if num1>num2:
        big=num1
        small=num2
    else:
        big = num1
        small = num2

    for i in range(1,small+1):
        if num1 % i == 0 and num2 % i ==0 and isprim(i):
            ko.append(i)

    if len(ko)==0:
        return 0
    return ko[0]


print(kozos(6,8))