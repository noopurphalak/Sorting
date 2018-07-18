def merge(li1, li2):
    c = li1 + li2
    return sorted(c)


def mergeSort(li):
    if len(li) == 1:
        return li
    breakup = len(li) // 2
    l1 = li[0: breakup]
    l2 = li[breakup:]

    l1 = mergeSort(l1)
    l2 = mergeSort(l2)

    return merge(l1, l2)


if __name__ == "__main__":
    sorted_list = mergeSort([14, 33, 27, 10, 35, 19, 42, 44])
    print("Sorted List: " + str(sorted_list))
