# Main method of quick Sort
def quickSort(a,l,h):
    if l<h:
        p=hopartition(a,l,h)
        quickSort(a,l,p)
        quickSort(a,p+1,h)

# Hoare partition
def hopartition(a,l,h):
    i=l
    j=h
    pivot=a[l]
    # i and j are at the two ends of the array
    while True:
        # Check the value at index i and j with pivot
        # if true, increase i and decrease j
        while a[i]<pivot and i<h:
            i+=1
        while a[j]>pivot and j>l:
            j-=1
        # The loop stop when i >=j
        if i>=j:
            break
        # Swap the value between index i and j
        a[i],a[j]=a[j],a[i]
    return j
    
a=[12,2,31,75,1,5,36,99,71,305,29,301,3]
quickSort(a,0,len(a)-1)
print(a)