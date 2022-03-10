nums = [5, 3, 6, 4, 1, 2, 8, 7]
def MergeSort(num):
    if len(num) <= 1:
        return num
    mid = int(len(num) / 2)
    L_list, R_list = MergeSort(num[:mid]), MergeSort(num[mid:]);
    i, j = 0, 0;
    result = []
    while i < len(L_list) and j < len(R_list):
        if (L_list[i] < R_list[j]):
            result.append(R_list[j]);
            j += 1;
        else:
            result.append(L_list[i]);
            i += 1;
    result += R_list[j:] + L_list[i:];
    return result;
print(MergeSort(nums))
