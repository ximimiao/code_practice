def quiksort(array, left, right):
    key = array[left]
    low = left
    high = right
    if left<right:
        while low < high:
            while low <high and array[high]>=key:
                high -=1
            array[low] = array[high]
            while low <high and array[low]<key:
                low+=1
            array[high] = array[low]

        array[low] = key
        quiksort(array, left, low - 1)
        quiksort(array, low + 1, right)
s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
quiksort(s,0,len(s)-1)
print(s)