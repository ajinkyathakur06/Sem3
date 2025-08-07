#Input: Sorted array
#Output: True if there is a pair with the given sum, else False

def checkPair(arr, n, sum):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                print(str(arr[i]) + " + " + str(arr[j]) + " = " + str(sum))
                return True
    return False

def checkPairAI(arr, n, sum):
    left = 0
    right = n - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == sum:
            return True
        elif current_sum < sum:
            left += 1
        else:
            right -= 1
            
    return False

arr = [5,9,2,1,0,7,15]
sum = 12
if checkPair(arr, len(arr), sum):
    print("Pair found")
else:
    print("No pair found")


sorted_arr = [1, 2, 5, 7, 9, 15]
sum = 12
if checkPairAI(sorted_arr, len(sorted_arr), sum):
    print("Pair found in sorted array")
else:
    print("No pair found in sorted array")