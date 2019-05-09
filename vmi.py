def isprim(val):
    if val < 2:
        return False
    for i in range(2, val):
        if val % i == 0:
            return False
    return True
