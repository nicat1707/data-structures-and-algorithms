"""
LeetCode 1700 — Number of Students Unable to Eat Lunch (Easy)
Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

Məzmun:
students massivi növbədəki şagirdlərin üstünlüyünü (0 = dairəvi,
1 = kvadrat sendviç), sandwiches massivi isə yığın (stack) şəklindəki
sendviçlərin sırasını göstərir (indeks 0 — yığının başı).

Hər addımda: növbənin önündəki şagird yığının başındakı sendviçi
istəyirsə götürüb ayrılır; istəmirsə növbənin sonuna keçir. Heç bir
qalan şagird yığının başındakı sendviçi istəməyəndə proses dayanır.
Nə qədər şagirdin ac qaldığını (sendviç yeyə bilmədiyini) tapmaq lazımdır.

Yanaşma (Approach) — Sayğaclarla simulyasiya:
Şagirdləri növbə şəklində simulyasiya etmək əvəzinə, sadəcə neçə
şagirdin 0 (dairəvi), neçəsinin isə 1 (kvadrat) istədiyini sayırıq
(count_0, count_1) — çünki növbədəki sıra əhəmiyyətsizdir, yalnız
"kimin nəyi istədiyi" sayı önəmlidir.

Sonra yığındakı sendviçləri başdan sona gəzirik:
- Əgər cari sendviç 0-dırsa və count_0 > 0-dırsa, bir şagird onu yeyir
  (count_0 azalır) və davam edirik.
- Əgər cari sendviç 1-dirsə və count_1 > 0-dırsa, eyni şəkildə davam edirik.
- Əks halda (yəni bu sendviçi istəyən heç bir şagird qalmayıbsa),
  proses dayanır — qalan bütün şagirdlər (count_0 + count_1) ac qalır.

Zaman Mürəkkəbliyi: O(n) — massivlər bir dəfə gəzilir
Yaddaş Mürəkkəbliyi: O(1) — yalnız iki sayğac saxlanılır
"""


def count_students(students, sandwiches):
    count_0 = students.count(0)
    count_1 = students.count(1)

    for sandwich in sandwiches:
        if sandwich == 0 and count_0 > 0:
            count_0 -= 1
        elif sandwich == 1 and count_1 > 0:
            count_1 -= 1
        else:
            break

    return count_0 + count_1


if __name__ == "__main__":
    print(count_students([1, 1, 0, 0], [0, 1, 0, 1]))              # 0
    print(count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # 3
