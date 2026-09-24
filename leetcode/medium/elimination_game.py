"""
LeetCode 390 — Elimination Game (Medium)
Link: https://leetcode.com/problems/elimination-game/

Məzmun:
[1, n] aralığındakı bütün tam ədədlərdən ibarət artan sıralı siyahı (arr)
verilir. Aşağıdakı alqoritm tətbiq olunur:
- Soldan sağa: birinci ədədi və ondan sonra hər ikinci ədədi silmək.
- Sağdan sola: qalan ədədlər arasında ən sağdakını və ondan sonra
  hər ikinci ədədi silmək.
- Bu addımları (sol→sağ, sağ→sol növbələşərək) bir ədəd qalana qədər
  təkrarlamaq.
Son qalan ədədi tapmaq lazımdır.

Yanaşma (Approach) — Massivi real qurmadan, sərhədləri izləmək:
n böyük ola bildiyi üçün (məs. milyonlarla), real siyahı yaradıb
elementləri silmək çox yavaş olardı (O(n) yaddaş və vaxt). Bunun
əvəzinə yalnız aralığın "sol sərhədini" (head) və "addım ölçüsünü"
(step) izləyirik — qalan ədədlərin sayı (remaining) da lazımdır.

Hər tur:
- Əgər soldan sağa gedən tursa VƏ ya qalan ədədlərin sayı taxdırsa
  (remaining tək ədəddirsə), sol sərhəd dəyişir (head += step).
  (Sağdan-sola gedən turda sol sərhəd yalnız remaining tək olduqda dəyişir,
  çünki cüt sayda element qalanda ən soldakı ədəd "silinməyən" tərəfdə qalır.)
- Qalan ədədlərin sayı yarıya bölünür (remaining //= 2).
- Addım ölçüsü ikiqat artır (step *= 2), çünki hər turdan sonra
  qalan ədədlər arasındakı məsafə ikiqat olur.
- İstiqamət növbələşir.

Bir ədəd qalana qədər (remaining == 1) davam edirik, sonda head cavabdır.

Zaman Mürəkkəbliyi: O(log n) — hər addımda qalan ədədlərin sayı yarıya bölünür
Yaddaş Mürəkkəbliyi: O(1) — yalnız bir neçə dəyişən saxlanılır
"""


def last_remaining(n):
    head = 1
    step = 1
    remaining = n
    left_to_right = True

    while remaining > 1:
        if left_to_right or remaining % 2 == 1:
            head += step

        remaining //= 2
        step *= 2
        left_to_right = not left_to_right

    return head


if __name__ == "__main__":
    print(last_remaining(9))  # 6
    print(last_remaining(1))  # 1
