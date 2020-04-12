# 快速排序
def quickSort(a,start,end):
    if start >= end:
        return
    i = start
    j = end
    temp = a[i]
    while (i < j):
        while (i < j and a[j] >= temp):
            j -= 1
        if (i < j):
            a[i] = a[j]
            i += 1
        while (i < j and a[i] <= temp):
            i += 1
        if (i < j):
            a[j] = a[i]
            j -= 1
    a[i] = temp
    quickSort(a, start, i-1)
    quickSort(a, i+1, end)

a = [3,5,2,1,9,5,6,8,7]
quickSort(a,0,len(a)-1)
print(a)