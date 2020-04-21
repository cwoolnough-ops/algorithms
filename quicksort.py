# quickosrt runs in bigO(n*logn) runtime, however if passed on a sorted list quickosrt will be bigO(n**2) 
# we get around this by picking a random pivot element
from random import randrange
def quicksort(list, start, end):
    #base case for recursion (a list with 1 element is sorted)
    if start >= end:
        return
    # pick a value from list randomly, assign the value at the index to be the pivot, move the pivot to the end of the list
    pivot_idx = randrange(start, end + 1)
    pivot_idx_value = list[pivot_idx]
    list[pivot_idx], list[end] = list[end], list[pivot_idx]
    #mark the first element of the list, when elements in the list are less tham the pivot swap their placements and 
    #move the mark the next element  
    current_lowest = start
    for i in range(start, end):
        if list[i] < pivot_idx_value:
            list[current_lowest], list[i] = list[i], list[current_lowest]
            current_lowest += 1
    # move our pivot element to the location of our mark (current_lowest) before the pivot will be less than values
    # after the pivot will be greater than values
    list[end], list[current_lowest] = list[current_lowest], list[end]
    #call quicksort recursively on the less than and greater than sides of the list excluding the pivot element
    quicksort(list, start, current_lowest - 1 )
    quicksort(list, current_lowest + 1, end)
# test case
list = [5, 3, 1, 7, 4, 6, 2, 8]
quicksort(list, 0, len(list) -1)
print(list)