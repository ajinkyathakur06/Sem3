def add_lists(l1, l2):
    result = []
    carry = 0
    max_length = max(len(l1), len(l2))

    for i in range(max_length):
        if i < len(l1):
            carry += l1[i]
        if i < len(l2):
            carry += l2[i]
        result.append(carry % 10)
        carry //= 10
    if carry > 0:
        result.append(carry)
    return result

l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
output = add_lists(l1, l2)
print(output)  # Output should be [8,9,9,9,0,0,0,1]