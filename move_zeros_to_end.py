"""
Дан массив целых чисел длины 
n
n. Требуется на месте (без использования дополнительного массива) переместить все нули в конец массива, сохранив исходный порядок ненулевых элементов.
"""


def ventil(a):
    n = len(a)
    left, right = 0, n - 1
    while left < right:
        if a[left] == 0 and a[right] != 0:
            temp = a[right]
            a[right] = a[left]
            a.insert(right - 1, temp)
            a.pop(left)
        elif a[right] == 0 and a[left] != 0:
            continue 

        left+=1
        right-=1
    return a

n = int(input())
a = list( map( int, input().split()) )

print(*ventil(a), sep =' ')
