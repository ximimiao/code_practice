def get_n(l,left,right):
    key = l[left]
    low = left
    high = right
    while low<high:
        while low<high and l[high]>key:
            high -= 1
        l[low] = l[high]
        while low<high and l[low]<key:
            low+=1
        l[high] = l[low]
        l[low] = key
    return low

def quick_sort(l,left,right):
    if left<right:
        p = get_n(l,left,right)
        quick_sort(l, left, p - 1)
        quick_sort(l, p+1, right)
    return l

s = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
print(quick_sort(s,0,len(s)-1))