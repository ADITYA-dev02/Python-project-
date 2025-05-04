
def append1(lst, x):
    lst.append(x)
    return lst

def extend1(lst, items):
    lst.extend(items)
    return lst

def pop0(lst):
    if lst:
        return lst.pop()
    return None

def remove1(lst, x):
    if x in lst:
        lst.remove(x)
    return lst