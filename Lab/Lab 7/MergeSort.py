#2.1 The complexity of pop(0) of a built-in list is O(n), because when the first element is deleted, the rest of the elements have to be shifted one space in memory.
import time

def mergeSort(aList):

    if (len(aList) < 2):
        return (aList)
    else:
        a = aList[0 : len(aList) // 2]
        b = aList[len(aList) // 2: len(aList)]
        aButSorted = mergeSort(a)
        bButSorted = mergeSort(b)

        return (merge(aButSorted, bButSorted))
        
def merge(listA, listB):
    newList = []
    indexA = 0
    indexB = 0

    while (indexA < len(listA) and indexB < len(listB)):
        if (listA[indexA] < listB[indexB]):
            newList.append(listA[indexA])
            indexA += 1
        else:
            newList.append(listB[indexB])
            indexB += 1

    while indexA < len(listA):
        newList.append(listA[indexA])
        indexA += 1

    while indexB < len(listB):
        newList.append(listB[indexB])
        indexB += 1

    return newList

if __name__ == "__main__":
    start_time = time.time()

    aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    bList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    merge(aList, bList)

    print("--- %s seconds ---" % (time.time() - start_time))