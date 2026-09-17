"""
Bubble Sort — Sıralama Alqoritmi

Məzmun: Qonşu elementləri müqayisə edərək, sırası səhv olanları
yerini dəyişməklə siyahını artan sıraya düzür.

Yanaşma (Approach):
Hər addımda siyahı boyunca gedib qonşu elementləri müqayisə edirik.
Əgər soldakı sağdakından böyükdürsə, yerlərini dəyişirik.
Bu prosesi heç bir dəyişiklik olmayana qədər təkrarlayırıq.

Zaman Mürəkkəbliyi: O(n^2) — ən pis və orta hal
Yaddaş Mürəkkəbliyi: O(1) — əlavə yaddaş tələb olunmur (in-place)
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(data))  # [11, 12, 22, 25, 34, 64, 90]
