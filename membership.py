

def sortering(array):
    i = 1
    while i < (len(array)):
        int1 = i
        while (int1 > 0) and (array[int1] < array[int1-1]):
            temporar = array[int1]
            array[int1] = array[int1-1]
            array[int1-1] = temporar
            int1 -= 1
        i += 1
    return array


def isMember(key, array):
    L=0
    R=len(array)-1
    X = (L+R)//2
    while array[X] !=  key and  L <= R:
        if array[X] < key:
            L=X+1
        else:
            R=X-1
        X = (L+R)//2
    return (array[X] == key)

def binarysortsearchmember(key,array):
    sortedArray = sortering(array)
    print(sortedArray)
    return(isMember(key,sortedArray))


