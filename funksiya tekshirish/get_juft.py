def get_even(l):
    newlist = []
    for item in l:
        if item%2 == 0:
            newlist.append(item)
    return newlist