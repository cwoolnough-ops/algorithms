# merge sort function seperates the list into single digit lists then uses the merge helper function to recreate a sorted list
def merge_sort(list):
    #base case. a list with one element is sorted so return
    if len(list) <= 1:
        return list
    #splits the list into two halves
    middle_index = len(list) // 2
    left_list = list[:middle_index]
    right_list = list[middle_index:]
    # functiion is called recursively to each half of the list, continues untill base case is met ie:one element list
    left_sorted = merge_sort(left_list)
    right_sorted = merge_sort(right_list)
    # call merge helper function to sort the 1 digit lists into one sorted list
    return merge(left_sorted, right_sorted)
# helper function for merge sort.
def merge(left, right):
    merged = []
    # loop untill one list is out of values
    while (left and right):
        #compare first elements in either list, add the smaller element to merged list then remove it from its current list
        if len(left[0]) < len(right[0]): # "len" is used as we are comparing length of strings in our test case. remove len for integer inputs
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)
    #once a lists elements are exhausted add the list with values to the end of the merged list
    if left:
        merged += left
    if right:
        merged += right
    return merged
# test case to sort 
list = []
while True:
    line = input("write input")
    #logic for getting multiline inputs
    if line:
        list.append(line)
    else:
        break
# the first input is the total number of inputs, ie a throwaway value that shouldnt be sorted
list = list[1:]
print(merge_sort(list))