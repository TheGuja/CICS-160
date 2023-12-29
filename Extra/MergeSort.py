import time

def mergeSort(aList):

    if (len(aList) < 2):
        return (aList)
    else:
        a = aList[0 : len(aList) // 2]
        b = aList[len(aList) // 2 : len(aList)]
        a_sorted = mergeSort(a)
        b_sorted = mergeSort(b)

        return a_sorted
        # return merge(a_sorted, b_sorted)
        
def merge(listA, listB):
    newList = []

    while (len(listA) > 0 and len(listB) > 0):

        if (listA[0] < listB[0]):
            newList.append(listA[0])
            listA.pop(0)
        else:
            newList.append(listB[0])
            listB.pop(0)

    newList.extend(listA)
    newList.extend(listB)

    return newList

if __name__ == "__main__":
    aList = [7, 6, 5, 4, 3, 2]
    newList = mergeSort(aList)
    # sorted_list = mergeSort(aList)
    print(newList)
    # print(sorted_list)