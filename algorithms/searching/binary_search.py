"""
Binary Search — Axtarış Alqoritmi

Məzmun: Artan sıraya düzülmüş siyahıda bir dəyəri sürətli tapmaq üçün
istifadə olunur. Hər addımda axtarış sahəsini yarıya bölür.

Yanaşma (Approach):
Siyahının ortasındakı elementi axtarılan dəyərlə müqayisə edirik.
Bərabərdirsə tapılıb. Böyükdürsə sol yarıda, kiçikdirsə sağ yarıda
davam edirik. Bu, siyahı bir elementə qədər azalana qədər təkrarlanır.

Zaman Mürəkkəbliyi: O(log n)
Yaddaş Mürəkkəbliyi: O(1) — iterativ versiyada əlavə yaddaş tələb olunmur
"""


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # tapılmadı


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(data, 7))   # 3
    print(binary_search(data, 4))   # -1
