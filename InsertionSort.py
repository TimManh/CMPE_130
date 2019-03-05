def insertSort(a):
    for i in range(len(a)-1):
        current=i
        j=i+1
        while a[i]>a[j] and i>=0:
            a[i],a[j]=a[j],a[i]
            i-=1
            j-=1
        i=current
array=[1,7,9,2,3]
insertSort(array)
print(array)

