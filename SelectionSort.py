def selSort(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]> a[j]:
                a[i],a[j]=a[j],a[i]
array = [14, 1, 3, 2, 5,21,300,27,75]
selSort(array)
print(array)
