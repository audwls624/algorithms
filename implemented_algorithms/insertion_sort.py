def insertion_sort(target_list):
    for i in range(1, len(target_list)):
        for j in range(i, 0 -1):
            if target_list[j] < target_list[j-1]:
                target_list[j], target_list[j-1] = target_list[j-1], target_list[j]
            else:
                break
    return target_list
    