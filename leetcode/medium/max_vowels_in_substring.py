"""
LeetCode 1456 — Maximum Number of Vowels in a Substring of Given Length (Medium)
Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Məzmun:
Bir sətir (s) və bir ədəd (k) verilir. s sətrinin uzunluğu k olan
bütün alt-sətirləri (substring) arasında ən çox sait hərf (a, e, i, o, u)
olanının sait sayını tapmaq lazımdır.

Yanaşma (Approach) — Sabit Ölçülü Sürüşən Pəncərə (Fixed-Size Sliding Window):
Əvvəlcə sətrin ilk k simvolundan ibarət pəncərədəki sait sayını hesablayırıq —
bu bizim başlanğıc nəticəmizdir (max_count).

Sonra pəncərəni sağa doğru bir-bir sürüşdürürük:
- Pəncərəyə sağdan yeni daxil olan simvol saitdirsə, sayğacı 1 artırırıq.
- Pəncərədən soldan çıxan simvol saitdirsə, sayğacı 1 azaldırıq.
Hər addımdan sonra cari sayı max_count ilə müqayisə edib böyüyünü saxlayırıq.

Bu üsulla hər dəfə bütün pəncərəni yenidən saymırıq — yalnız daxil olan
və çıxan bir simvola baxırıq, buna görə çox sürətlidir.

Zaman Mürəkkəbliyi: O(n) — sətir bir dəfə gəzilir (n = sətrin uzunluğu)
Yaddaş Mürəkkəbliyi: O(1) — yalnız bir neçə sayğac saxlanılır
"""


def max_vowels(s, k):
    vowels = set("aeiou")

    # İlk pəncərədəki sait sayı
    current_count = sum(1 for char in s[:k] if char in vowels)
    max_count = current_count

    # Pəncərəni sağa sürüşdür
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_count += 1
        if s[i - k] in vowels:
            current_count -= 1

        max_count = max(max_count, current_count)

    return max_count


if __name__ == "__main__":
    print(max_vowels("abciiidef", 3))  # 3 ("iii")
    print(max_vowels("aeiou", 2))      # 2
    print(max_vowels("leetcode", 3))   # 2
