def swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp


def selectionSort(li):
    for i in range(1, len(li)):
        holePosition = i - 1
        iterativePosition = i
        minNumber = li[holePosition]
        minHolePosition = holePosition

        while iterativePosition != len(li):
            if li[iterativePosition] < minNumber:
                minNumber = li[iterativePosition]
                minHolePosition = iterativePosition
            iterativePosition += 1
        if holePosition != minHolePosition:
            swap(li, holePosition, minHolePosition)
    print("Sorted List: " + str(li))


if __name__ == "__main__":
    selectionSort([14, 33, 27, 10, 35, 19, 42, 44])
