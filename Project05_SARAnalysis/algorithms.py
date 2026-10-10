def iterative_binary_search(values, target):
    l, h = 0, len(values) - 1
    while l <= h:
        m = (l + h) // 2
        if values[m] == target:
            return m
        if values[m] < target:
            l = m + 1
        else:
            h = m - 1
    return -1

def recursive_binary_search(values, target, l, h):
    if l > h:
        return -1
    m = (l + h) // 2
    if values[m] == target:
        return m
    if values[m] < target:
        return recursive_binary_search(values, target, m + 1, h)
    return recursive_binary_search(values, target, l, m - 1)

def sequential_search(values, target):
    for i, val in enumerate(values):
        if val == target:
            return i
    return -1
