def A067863_checker(N):
    total = 0
    a = str(7 ** N)
    for j in xrange(len(a)):
        total += int(a[j])
    
    if (total % N) == 0:
        return True

    else:
        return False



def A067863(N):
    result = []
    for i in xrange(1, N):
        if A067863_checker(i):
            result.append(i)
    return result
