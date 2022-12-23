-> we go one by one and make switches as we find the smaller element than current.

-> for example-:
- an array [8,3,1,7,0] is there.
- first we compare 8 with 3, as we found that 3 is smaller than 8 so we'll switch it.
- it becomes [3,8,1,7,0]
- then again we check 8 with 1, as 8 > 1, we will switch the elements
- it becomes [3,1,8,7,0]
- again previous stem till lask elemt and we'll get
- it becomes [3,1,7,0,8]
- this will continue untill te whole array is sorted.
- so as we see the number of iteration is same as number of elements and we do it the same number of time as the length of array so the time complexity is O(n^2).

best case -> O(n) array already sorted
worst case & average case -> O(n^2)