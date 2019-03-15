def max_heapify(a, n, i): 
    # Initialize the left and right node
    large_num = i 
    l = 2 * i + 1     
    r = 2 * i + 2    
  
    #Compare the value of root node with child node 
    if l < n and a[i] < a[l]: 
        large_num = l 
  
    if r < n and a[large_num] < a[r]: 
        large_num = r 
  
    # Swap the child node with root node if child is greater
    # than root
    if large_num != i: 
        a[i],a[large_num] = a[large_num],a[i] # swap 
  
        # Recursive method to heapify the root
        max_heapify(a, n, large_num) 
  
def heapSort(a): 
    n = len(a) 
  
    # Create maxheap
    for i in range(n, -1, -1): 
        max_heapify(a, n, i) 
  
    # Swap the root with the last node
    for i in range(n-1, 0, -1): 
        a[i], a[0] = a[0], a[i]
        max_heapify(a, i, 0) 
a=[12,21,31,41,11,9]
heapSort(a)
print(a)
