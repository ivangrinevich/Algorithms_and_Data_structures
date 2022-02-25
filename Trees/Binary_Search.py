from array import array


def search(arr, elem):
    result = array('i')
    result.fromlist([0] * 3)
    left = 0
    right = len(arr)
    while left < right:
        middle = (right + left) // 2
        if arr[middle] == elem:
            result[0] = 1
            break
        elif elem > arr[middle]:
            left = middle + 1
        else:
            right = middle
    result[1] = left_border(arr, elem)
    result[2] = right_border(arr, elem)
    print(*result)


def left_border(arr, elem):
    left = 0
    right = len(arr)
    while left < right:
        middle = (left + right) // 2
        if elem <= arr[middle]:
            right = middle
        else:
            left = middle + 1
    return left


def right_border(arr, elem):
    left = 0
    right = len(arr)
    while left < right:
        middle = (left + right) // 2
        if elem < arr[middle]:
            right = middle
        else:
            left = middle + 1
    return left


n = int(input())
elements = array('i')
elements.fromlist([int(i) for i in input().split()])
num_of_requests = input()
requests = array('i')
requests.fromlist([int(i) for i in input().split()])
for request in requests:
    search(elements, request)
