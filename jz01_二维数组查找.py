def find(target, array):
    rows = len(array)-1
    columns = len(array[0]) - 1
    i, j = rows, 0
    while i >= 0 and j <= columns:
        if array[i][j] < target:
            j += 1
        elif  array[i][j] > target:
            i -= 1
        else:
            return True
    return False

target = 5
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(find(target, array))