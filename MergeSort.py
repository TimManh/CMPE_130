def mergeSort(a):
    n=len(a)
    if n<=1:
        return a
    L=mergeSort(a[:round(n/2)])
    R=mergeSort(a[round(n/2):])
    return merge(L,R)
def merge(L,R):
    i=0
    j=0
    newA=[]
    while i<len(L) and j< len(R):
        if L[i]<R[j]:
            newA.append(R[j])
            j+=1
        else:
            newA.append(L[i])
            i+=1
    while i <len(L):
        newA.append(L[i])
        i+=1
    while j< len(R):
        newA.append(R[j])
        j += 1
    return newA

array=[15,32,1,42,21]
b=mergeSort(array)
print(b)