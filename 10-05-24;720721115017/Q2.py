def value(A, ar_size): 
    
     
    for i in range(ar_size): 
        
         
        count = 0
        for j in range(ar_size): 
        
            if(A[i] == A[j]): 
                count += 1
        if(count == 1): 
            return A[i] 
    return -1
  
nums = [2, 2,1] 
n = len(nums) 
print(value(nums,n))

nums1=[4,1,2,1,2]
n = len(nums1) 
print(value(nums1,n))

nums2=[1]
n=len(nums2)
print(value(nums2,n))

