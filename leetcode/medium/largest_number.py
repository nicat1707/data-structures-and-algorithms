"""
LeetCode 179 — Largest Number (Medium)
Link: https://leetcode.com/problems/largest-number/

Məzmun:
Mənfi olmayan tam ədədlərdən ibarət siyahı (nums) verilir. Bu ədədləri
elə düzmək lazımdır ki, onları bir-birinin ardınca yazdıqda ən böyük
mümkün ədəd (string şəklində) alınsın.

Yanaşma (Approach) — Xüsusi müqayisə ilə sıralama:
Adi ədəd sıralaması burada işləmir, çünki 9 > 30, amma "930" > "309".
Ona görə ədədləri string-ə çeviririk və iki string-i müqayisə edəndə
"hansı sıra ilə birləşdirsək daha böyük ədəd alınır" sualına cavab
axtarırıq: a+b ilə b+a-nı müqayisə edirik (məs. "9"+"30"="930" ilə
"30"+"9"="309" — 930 > 309 olduğu üçün "9" "30"-dan əvvəl gəlməlidir).

Bu müqayisə qaydasına əsasən bütün siyahını sıralayırıq, sonra
hamısını birləşdiririk. Əgər nəticə "000...0" kimi çıxarsa (bütün
elementlər 0-dırsa), cavab "0" olmalıdır — bunu ayrıca yoxlayırıq.

Zaman Mürəkkəbliyi: O(n log n) — sıralama zamanı hər müqayisə O(k)
                     vaxt aparır (k = ədədin string uzunluğu)
Yaddaş Mürəkkəbliyi: O(n) — string-lərin saxlanması üçün
"""

from functools import cmp_to_key


def largest_number(nums):
    strs = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1  # a, b-dən əvvəl gəlməlidir
        elif a + b < b + a:
            return 1
        return 0

    strs.sort(key=cmp_to_key(compare))

    result = "".join(strs)

    # Bütün elementlər 0-dırsa, "000" yox, "0" qaytarmalıyıq
    return "0" if result[0] == "0" else result


if __name__ == "__main__":
    print(largest_number([10, 2]))          # "210"
    print(largest_number([3, 30, 34, 5, 9]))  # "9534330"
    print(largest_number([0, 0]))             # "0"
