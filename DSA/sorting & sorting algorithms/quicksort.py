def quicksort(arr):
    elements = len(arr)
    
    if elements < 2:
        return arr
    current_position = 0 

    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              arr[i],arr[current_position] = arr[current_position],arr[i]

    arr[0],arr[current_position] = arr[current_position],arr[0]
    
    left = quicksort(arr[0:current_position])
    right = quicksort(arr[current_position+1:elements]) 

    arr = left + [arr[current_position]] + right
    return arr

test = [8,3,1,0,7,10,2]
print(quicksort(test))