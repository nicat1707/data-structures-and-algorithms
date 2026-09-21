"""
LeetCode 9 — Palindrome Number (Easy)
Link: https://leetcode.com/problems/palindrome-number/

Məzmun:
Bir tam ədəd (x) verilir. Bu ədədin palindrom olub-olmadığını
(soldan sağa və sağdan sola oxunduqda eyni olub-olmadığını)
yoxlamaq lazımdır.

Yanaşma (Approach) — Yarısını tərsinə çevirmək:
Əvvəlcə mənfi ədədləri dərhal "palindrom deyil" kimi qaytarırıq,
çünki mənfi işarə sətrin əvvəlində olur, amma sonunda yoxdur
(məs. -121 tərsinə 121- olur, bu bərabər deyil).

Sonra ədədi string-ə çevirib sətri tərsinə çeviririk və orijinalla
müqayisə edirik — bu, ən sadə və başa düşülən yanaşmadır.

(Qeyd: daha "riyazi" yanaşma ədədin yalnız yarısını rəqəm-rəqəm
tərsinə çevirib qalan yarısı ilə müqayisə etməkdir ki, bu, string-ə
çevirmədən, O(1) əlavə yaddaşla edilə bilər — amma aşağıdakı sadə
versiya oxunaqlılıq üçün üstünlük təşkil edir.)

Zaman Mürəkkəbliyi: O(d) — d, ədədin rəqəm sayıdır
Yaddaş Mürəkkəbliyi: O(d) — ədədin string versiyası saxlanılır
"""


def is_palindrome(x):
    if x < 0:
        return False

    s = str(x)
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome(121))    # True
    print(is_palindrome(-121))   # False
    print(is_palindrome(10))     # False
