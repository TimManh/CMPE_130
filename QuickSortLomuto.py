def luQuickSort(a,l,h):
    if l<h:
        p=partition(a,l,h)
        luQuickSort(a,l,p-1)
        luQuickSort(a,p+1,h)
def partition(a,l,h):
    pi=a[h]
    i=l
    for j in range(l,h):
        if a[j]<pi:
            a[i],a[j]=a[j],a[i]
            i+=1
    a[i],a[h]=a[h],a[i]
    return i
a=[12,2,31,75,1,5,36,99,71,305,29,301]
luQuickSort(a,0,len(a)-1)
print(a)