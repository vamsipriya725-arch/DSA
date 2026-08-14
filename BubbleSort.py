a = [3,8,5,1]
for b in range(len(a)):
    for c in range(len(a) - b - 1):
        if a[c] > a[c + 1]:
            a[c], a[c + 1] = a[c + 1], a[c]

print(a)

#......With Function.........
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
