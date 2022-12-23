def binary_search(input_array, value):
    left = 0
    right = len(input_array)-1
    while(left<=right):
        mid = int((left+right)/2)
        if input_array[mid] == value:
            print(mid)
            break
        elif input_array[mid] < value:
            left = mid+1
        else:
            right = mid-1
    else:
        print("not found")

test_list = [1,3,9,11,15,19,29]
binary_search(test_list, 25)