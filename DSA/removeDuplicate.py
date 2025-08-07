#remove duplicates from an array

def removeDuplicates(arr):
    unique_elements = []
    for ele in arr:
        if ele not in unique_elements:
            unique_elements.append(ele)
    return unique_elements

arr = [1, 2, 2, 3, 4, 4, 5]
print("Original array:", arr)
unique_arr = removeDuplicates(arr)
print("Array after removing duplicates:", unique_arr)