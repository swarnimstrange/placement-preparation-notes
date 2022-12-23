-> to do a quicksort we chose one of the values in array at random and call it as pivot. To make all value lesser than pivot in left side and all values larger than pivot in right side. once it has happened we treat left side of pivot as an array itself and define a random pivot from that array and do the same process until the array is sorted. do the same with right sde of an array of pivot.

-> for eg. 
[8,3,1,0,7,10,2]

- lets choose 2 as a pivot
- we check all elements if it's larger than pivot or smaller than pivot.
- as we see 8 > 2
- therefore, we move 8 behind 2 and the element in front of 2 in 8 place, so it becomes

-> [10,3,1,0,7,2,8]

- as we see 10 > 2
- therefore, we move it behind of 2 and 7 that is in front of twomove it in front

-> [7,3,1,0,2,10,8]

- as we see 7 > 2, so we apply similar process on it.
- therefore, 7 goes behind 2 and 0 goes in front.

-> [0,3,1,2,7,10,8]

- as we see 0 < 2, so we wont make the switch and will go forward to next element of zero i.e 3
- as we see 3 > 2, therefore we will move it behind 2 and replace it's position with 1 that is in front of it.

-> [0,1,2,3,7,10,8]

- as 1 < 2, so we wont switch and we gotthe elements lesser than 2 in left side of it and larger than 2 in right side of it.

- so the next step would be we will treat left side of 2 as an array and take pivot of it as well and right side of 2 as an array and take pivot of it and perform same operation until we get sorted list.

-> average and best time complexity -: O(nlogn)
-> worst time complexity -: O(n^2)
