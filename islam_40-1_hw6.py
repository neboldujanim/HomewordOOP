unsorted_list = [13, 44, 17, 26, 33, 46, 57, 68, 45, 87, 33, 66]



def bubble_sort(list):
    s = len(list)
    for i in range(0, s-1):
        if list[i] > list[i + 1]:
            list[i], list[i+1] = list[i + 1], list[i]
    print(list)
print(unsorted_list)
bubble_sort(unsorted_list)

import random


def binary_search(Val):
    n = 5000
    resultOK = False
    first = 0
    last = n - 1
    while first < last:
         middle = (first + last) // 2
         if middle == Val:
             first = middle
             last = first
             resultOK = True
             Pos = middle
         elif Val>middle:
             first = middle + 1
         else:
             last = middle - 1


    if resultOK == True:
        print('The element has been found')
        print (Pos)

    else:
        print('The element has not been found')

Val = random.randint(0, 5000)
print(Val)
binary_search(Val)