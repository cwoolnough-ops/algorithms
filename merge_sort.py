def merge_sort(list):
    if len(list) <= 1:
        return list

    middle_index = len(list) // 2
    left_list = list[:middle_index]
    right_list = list[middle_index:]

    left_sorted = merge_sort(left_list)
    right_sorted = merge_sort(right_list)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    while (left and right):
        if len(left[0]) < len(right[0]):
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)
    if left:
        merged += left
    if right:
        merged += right
    return merged
list = []
while True:
    line = input("write input")
    if line:
        list.append(line)
    else:
        break
list = list[1:]
print(merge_sort([list]))