def sub_aarr(a,size):
    max_ending_here=0
    max_so_far=0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far



arr=[-2,-3,4,-1,-2,1,5,-3]
g=sub_aarr(arr,len(arr))
print(g)
