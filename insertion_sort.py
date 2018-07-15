def insertionSort(li):
    for i in range(1, len(li)):
        valueToInsert = li[i]
        holePosition = i

        while holePosition > 0 and (li[holePosition - 1] > li[holePosition]):
            li[holePosition] = li[holePosition - 1]
            holePosition = holePosition - 1
            li[holePosition] = valueToInsert
    print("Sorted List: " + str(li))


if __name__ == "__main__":
    insertionSort([14, 33, 27, 10, 35, 19, 42, 44])
