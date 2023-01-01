def selection_sort(target_list):
    for i in range(len(target_list)):
        min_index = i
        for j in range(i+1, len(target_list)):
            if target_list[min_index] > target_list[j]:
                min_index = j
                target_list[i], target_list[min_index] = target_list[min_index], target_list[i]

    return target_list

print(selection_sort([5,4,3,2,1]))
