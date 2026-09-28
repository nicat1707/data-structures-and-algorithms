"""
LeetCode 283 — Move Zeroes (Easy)
Link: https://leetcode.com/problems/move-zeroes/

Məzmun:
Tam ədədlərdən ibarət massiv (nums) verilir. Bütün 0-ları massivin
sonuna keçirmək lazımdır, amma 0 olmayan elementlərin öz aralarındakı
nisbi sırası dəyişməməlidir. Bunu in-place (massivin surətini çıxarmadan)
etmək tələb olunur.

Yanaşma (Approach) — İki Göstərici (Two Pointers):
Bir göstərici (write) "növbəti sıfır olmayan elementin yazılacağı yeri"
göstərir. İkinci göstərici (read) isə massivi soldan sağa gəzir.

- read göstəricisi hər elementə baxır.
- Əgər element 0 deyilsə, onu write mövqeyi ilə yerini dəyişirik
  (swap), sonra write göstəricisini bir addım irəli çəkirik.
- Element 0-dırsa, heç nə etmirik, sadəcə read irəli gedir.

Beləliklə, bütün sıfır olmayan elementlər ardıcıllığı pozulmadan
massivin başına yığılır, sıfırlar isə avtomatik olaraq sona keçir.

Zaman Mürəkkəbliyi: O(n) — massiv bir dəfə gəzilir
Yaddaş Mürəkkəbliyi: O(1) — in-place, əlavə yaddaş işlədilmir
"""


def move_zeroes(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
    print(move_zeroes([0]))                # [0]
