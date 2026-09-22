"""
LeetCode 643 — Maximum Average Subarray I (Easy)
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Məzmun:
n elementdən ibarət tam ədədlər massivi (nums) və bir ədəd (k) verilir.
Uzunluğu k olan ardıcıl alt-massiv (subarray) tapmaq lazımdır ki, onun
orta qiyməti (average) ən böyük olsun və bu qiyməti qaytarmaq lazımdır.

Yanaşma (Approach) — Sabit Ölçülü Sürüşən Pəncərə (Fixed-Size Sliding Window):
Əvvəlcə ilk k elementin cəmini hesablayırıq — bu bizim başlanğıc
pəncərəmizdir (current_sum) və eyni zamanda indiyədək ən böyük cəmdir
(max_sum).

Sonra pəncərəni sağa doğru bir-bir sürüşdürürük:
- Pəncərəyə sağdan yeni daxil olan elementi cəmə əlavə edirik.
- Pəncərədən soldan çıxan elementi cəmdən çıxırıq.
Hər addımdan sonra cari cəmi max_sum ilə müqayisə edib böyüyünü saxlayırıq.

Bütün massivi gəzib bitirdikdən sonra, tapılan ən böyük cəmi k-ya
bölərək orta qiyməti hesablayırıq.

Zaman Mürəkkəbliyi: O(n) — massiv bir dəfə gəzilir
Yaddaş Mürəkkəbliyi: O(1) — yalnız bir neçə dəyişən saxlanılır
"""


def find_max_average(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / k


if __name__ == "__main__":
    print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print(find_max_average([5], 1))                       # 5.0
