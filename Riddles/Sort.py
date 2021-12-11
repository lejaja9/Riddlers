numbers = [7,6,5,4,3,2,1,2,3,4,5,6,7]

#Merge Sort
def merge_sort(list):
    if len(list) == 0 or len(list) == 1:
        return list

    mid = (len(list))//2

    def merge(list1, list2):
        ans = []
        while len(list1) > 0 and len(list2) > 0:
            if list1[0] < list2[0]:
                ans.append(list1[0])
                list1.pop(0)
            else:
                ans.append(list2[0])
                list2.pop(0)
        if len(list1) > 0:
            ans += list1
        else:
            ans += list2
        return ans

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)

#Quick Sort
#with extra memory
def quick_sort(list):
    if len(list) <= 1:
        return list
    left = []
    right = []
    pivot = list[-1]
    for i in range(len(list)-1):
        if list[i] <= pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

#in place
def quick_sort(list, start, end):
    if end <= start:
        return

    def helper(array, l, r):
        pivot = array[r]
        p1 = l
        p2 = r-1
        while p1 <= p2:
            while list[p1] <= pivot and p1 <= p2:
                p1 += 1
            while list[p2] > pivot and p1 <= p2:
                p2 -= 1
            if p1 <= p2:
                list[p1], list[p2] = list[p2], list[p1]

        list[p1], list[r] = list[r], list[p1]

        return p1

    p = helper(list, start, end)
    quick_sort(list, start, p-1)
    quick_sort(list, p+1, end)
    return list

print(quick_sort(numbers, 0, len(numbers)-1))
