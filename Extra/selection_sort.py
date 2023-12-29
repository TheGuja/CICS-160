def put_biggest_at_the_end(aList, upToHere):
    if upToHere > 0:
        indexOfBiggest = 0

        for index in range(upToHere + 1):
            if (aList[index] > aList[indexOfBiggest]):
                indexOfBiggest = index

        temp = aList[upToHere]
        aList[upToHere] = aList[indexOfBiggest]
        aList[indexOfBiggest] = temp

def selection_sort(aList):
    biggestIndexToLookAt =  len(aList) - 1

    while (biggestIndexToLookAt !=0):
        put_biggest_at_the_end(aList, biggestIndexToLookAt)
        biggestIndexToLookAt = biggestIndexToLookAt - 1

    return aList

if __name__ == "__main__":
    l = [7, 6, 5, 4, 3, 2]
    selection_sort(l)
    print(l)