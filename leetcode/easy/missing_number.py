"""
LeetCode 268 — Missing Number (Easy)
Link: https://leetcode.com/problems/missing-number/

Məzmun:
[0, n] aralığında n fərqli ədəddən ibarət massiv (nums) verilir
(yəni massivin uzunluğu n, amma dəyərlər 0-dan n-ə qədərdir).
Bu aralıqda massivdə çatışmayan tək ədədi tapmaq lazımdır.

Yanaşma (Approach) — Cəmlərin fərqi (Gauss düsturu):
Əgər massivdə heç nə çatışmasaydı, 0-dan n-ə qədər bütün ədədlərin
cəmi olardı: n * (n + 1) / 2 (bu, məşhur Gauss düsturudur).

Bizim massivdə isə bir ədəd çatışmır, ona görə massivdəki bütün
elementlərin həqiqi cəmi bu "gözlənilən cəm"-dən azdır. Fərq elə
çatışmayan ədədin özüdür:

    çatışmayan ədəd = gözlənilən_cəm - massivin_cəmi

Bu üsul massivi sortlamağa və ya əlavə strukturda saxlamağa ehtiyac
qoymur — yalnız bir dəfə gəzib cəmi hesablamaq kifayətdir.

Zaman Mürəkkəbliyi: O(n) — massiv bir dəfə gəzilir
Yaddaş Mürəkkəbliyi: O(1) — əlavə yaddaş tələb olunmur
"""


def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))                   # 2
    print(missing_number([0, 1]))                       # 2
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))   # 8
