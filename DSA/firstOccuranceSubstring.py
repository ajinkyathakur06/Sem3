#find out first occurrences of a substring in a string
#find out all occurrences of a substring in a string

def first_occurrence_substring(string, substring):
    array = string.split(' ')
    for i in range(len(array)):
        if array[i] == substring:
            return i

    return -1

def all_occurrences_substring(string, substring):
    array = string.split(' ')
    occurrences = []
    for i in range(len(array)):
        if array[i] == substring:
            occurrences.append(i)

    return occurrences


print("First occurrence of substring:", first_occurrence_substring("an hello world , hello universe ", "hell"))
print("All occurrences of substring:", all_occurrences_substring("an hello world , hello universe ", "hello"))