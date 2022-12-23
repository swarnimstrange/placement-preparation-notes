-> as the name suggest merge and sort so there something we want to divide and then merge to sort it.

-> so merge sort basically works on divide and conquer algorithm in which it divides elemets as a singl element and then goes on merging and sorting them one by one until the array is fuly merged and sorted.

-> for eg -> [8,3,1,7,0,10,2]

- next step
[8], [3], [1], [7], [0], [10], [2] 

- next step we start join them as wel as compare
[8], [1,3], [0,7], [2,10]

- next step 
[1,3,8] [0,2,7,10]

- final step
[0,1,2,3,7,8,10]

as we are comparing the elemets n number of time and the merging step take log n.
so in total the time complexity is O(n*logn) 
but the space complexity.