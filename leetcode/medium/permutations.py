"""
LeetCode 46 — Permutations (Medium)
Link: https://leetcode.com/problems/permutations/

Məzmun:
Fərqli tam ədədlərdən ibarət massiv (nums) verilir. Bu ədədlərin
bütün mümkün permutasiyalarını (yerdəyişmələrini) tapmaq lazımdır.
Cavab istənilən sırada qaytarıla bilər.

Yanaşma (Approach) — Backtracking (Geriyə İzləmə):
"path" adlı bir siyahıda hazırda qurduğumuz permutasiyanı saxlayırıq.
Hər addımda hələ path-ə əlavə edilməmiş bir ədədi seçib path-ə
əlavə edirik, sonra rekursiv olaraq davam edirik.

- Əgər path-in uzunluğu nums-un uzunluğuna bərabərdirsə, deməli tam
  bir permutasiya qurulub — onu nəticələrə əlavə edirik.
- Əks halda, hələ istifadə olunmamış hər ədəd üçün: onu path-ə
  əlavə edirik (choose), rekursiv çağırış edirik (explore), sonra
  onu path-dən çıxarırıq (un-choose / backtrack) ki, digər
  variantları da sınaya bilək.

Bu "seç → yoxla → geri qaytar" prinsipi bütün mümkün kombinasiyaları
sistematik şəkildə gəzməyə imkan verir.

Zaman Mürəkkəbliyi: O(n * n!) — n! permutasiya var, hər birini
                     qurmaq O(n) vaxt aparır
Yaddaş Mürəkkəbliyi: O(n) — rekursiya dərinliyi və path üçün
                      (nəticələri saxlamaq üçün əlavə yaddaş çıxılmaqla)
"""


def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True

            backtrack()

            path.pop()
            used[i] = False

    backtrack()
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permute([0, 1]))
    # [[0,1],[1,0]]
