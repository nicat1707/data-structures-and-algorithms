"""
LeetCode 75 — Sort Colors (Medium)
Link: https://leetcode.com/problems/sort-colors/

Məzmun:
0, 1, 2 rəqəmlərindən ibarət massiv verilir (qırmızı, ağ, mavi rəngləri
təmsil edir). Massivi in-place (əlavə yaddaş işlətmədən) elə sırala ki,
eyni rənglər bir-birinin yanında olsun: əvvəl bütün 0-lar, sonra 1-lər,
sonra 2-lər.

Yanaşma (Approach) — Dutch National Flag alqoritmi:
Üç göstərici saxlayırıq: low, mid, high.
- low-dan əvvəl olan hissə: yalnız 0-lar
- high-dan sonra olan hissə: yalnız 2-lər
- low ilə mid arası: yalnız 1-lər
- mid ilə high arası: hələ yoxlanılmamış elementlər

mid göstəricisi ilə massivi bir dəfə gəzirik:
- arr[mid] == 0 olsa, onu low ilə yerini dəyişirik, low və mid irəli gedir
- arr[mid] == 1 olsa, sadəcə mid irəli gedir
- arr[mid] == 2 olsa, onu high ilə yerini dəyişirik, high geri gedir (mid sabit qalır)

Zaman Mürəkkəbliyi: O(n) — massiv bir dəfə gəzilir
Yaddaş Mürəkkəbliyi: O(1) — in-place, əlavə yaddaş işlədilmir
"""


def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


if __name__ == "__main__":
    print(sort_colors([2, 0, 2, 1, 1, 0]))  # [0, 0, 1, 1, 2, 2]
    print(sort_colors([2, 0, 1]))            # [0, 1, 2]
