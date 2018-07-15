def swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp


def bubbleSort(li):
    while True:
        swapped = False
        for i in range(1, len(li)):
            if li[i - 1] > li[i]:
                swap(li, i - 1, i)
                swapped = True

        if not swapped:
            print("Sorted List: " + str(li))
            break


if __name__ == '__main__':
    bubbleSort([14, 33, 27, 35, 10])
