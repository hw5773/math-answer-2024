import logging

def bubble(lst):
    logging.debug("Bubble sort function")
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                tmp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = tmp
    return lst

def insertion(lst):
    logging.debug("Insertion sort function")
    n = len(lst)
    for j in range(1, n):
        i = 0
        while lst[j] > lst[i]:
            i += 1
        m = lst[j]

        for k in range(j-i):
            lst[j-k] = lst[j-k-1]
        lst[i] = m
    return lst

def merge(l1, l2):
    logging.debug("Merge sort function")
    ret = []

    while l1 != [] and l2 != []:
        if l1[0] < l2[0]:
            ret.append(l1.pop(0))
        else:
            ret.append(l2.pop(0))

        if l1 == []:
            while l2 != []:
                ret.append(l2.pop(0))
        elif l2 == []:
            while l1 != []:
                ret.append(l1.pop(0))

    return ret

def mergesort(lst):
    n = len(lst)
    if n > 1:
        m = n / 2
        l1 = []
        l2 = []
        for i in range(n):
            if i < m:
                l1.append(lst[i])
            else:
                l2.append(lst[i])
        return merge(mergesort(l1), mergesort(l2))
    else:
        return lst
