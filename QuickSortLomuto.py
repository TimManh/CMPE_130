# Main method for quick Sort
def loQuickSort(a,l,h):
    if l<h:
        p=partition(a,l,h)
        loQuickSort(a,l,p-1)
        loQuickSort(a,p+1,h)

#Lomuto Partition
def partition(a,l,h):
    # Pivot always the last element of the array
    pi=a[h]
    i=l
    # Iterate j and find value greater than pivot
    # Swap the value and increment i
    for j in range(l,h):
        if a[j]<pi:
            a[i],a[j]=a[j],a[i]
            i+=1
    # Swap the value of i index and last index
    a[i],a[h]=a[h],a[i]
    return i
    
a=[12,2,31,75,1,5,36,99,71,305,29,301]
loQuickSort(a,0,len(a)-1)
print(a)