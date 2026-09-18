"""
LeetCode 3 — Longest Substring Without Repeating Characters (Medium)
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Məzmun:
Bir sətir (s) verilir. Təkrarlanan simvol olmayan ən uzun ardıcıl
alt-sətrin (substring) uzunluğunu tapmaq lazımdır.

Yanaşma (Approach) — Sliding Window (Sürüşən Pəncərə):
İki göstərici (left, right) ilə sətir üzərində "pəncərə" gəzdiririk.
Hər simvolun sətirdə son harada görüldüyünü bir dictionary-də (seen)
saxlayırıq.

- right göstəricisi sağa doğru irəliləyir və s[right] simvolunu oxuyur.
- Əgər bu simvol artıq seen-də varsa VƏ onun mövqeyi cari pəncərənin
  (left-dən sonra) daxilindədirsə, deməli təkrar var — left göstəricisini
  o simvoldan bir sonrakı mövqeyə keçiririk (pəncərədən çıxarırıq).
- Hər addımda cari pəncərənin uzunluğunu (right - left + 1) hesablayıb
  ən böyük nəticə ilə müqayisə edirik.

Bu üsulla sətri yalnız bir dəfə gəzirik, hər simvola bir dəfə baxılır.

Zaman Mürəkkəbliyi: O(n) — sətir bir dəfə gəzilir (n = sətrin uzunluğu)
Yaddaş Mürəkkəbliyi: O(min(n, m)) — m mümkün simvolların sayı
                       (dictionary-də saxlanılan simvollar üçün)
"""


def length_of_longest_substring(s):
    seen = {}  # simvol -> son görüldüyü indeks
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
    print(length_of_longest_substring("bbbbb"))      # 1 ("b")
    print(length_of_longest_substring("pwwkew"))     # 3 ("wke")
