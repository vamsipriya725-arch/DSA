#.....without function..........
a = [3,8,5,1]
for b in range(len(a)):
    c = b
    for d in range(b + 1, len(a)):
        if a[d] < a[c]:
            c = d
    a[b], a[c] = a[c], a[b]

print(a)

#....With Function.........
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini = i

        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j

        arr[i], arr[mini] = arr[mini], arr[i]
    return arr
arr = [3, 8, 5, 1]
print(selection_sort(arr))
