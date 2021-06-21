def fibanocci(n):
    fbnc= []
    while len(fbnc)<n:
        if len(fbnc)==0 or len(fbnc)==1:
            fbnc.append(1)
        else:
            fbnc.append(fbnc[len(fbnc)-2]+fbnc[len(fbnc)-1])
    return fbnc
    
def in_fibanocci(n):
    if n<4:
        return True
    elif n in fibanocci(n):
        return True
    else:
        return False
print(fibanocci(55))
print(in_fibanocci(4807526976))
