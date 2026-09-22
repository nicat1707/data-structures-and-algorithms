"""
LeetCode 121 — Best Time to Buy and Sell Stock (Easy)
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Məzmun:
prices adlı massiv verilir, prices[i] — i-ci gündə səhmin qiymətidir.
Bir gün alıb, gələcəkdə başqa bir gün satmaqla əldə edilə biləcək
maksimum mənfəəti tapmaq lazımdır. Mənfəət mümkün deyilsə, 0 qaytarılır.

Yanaşma (Approach) — Bir keçidlə minimumu izləmək:
Massivi bir dəfə soldan sağa gəzirik və iki dəyəri yadda saxlayırıq:
- min_price: indiyə qədər gördüyümüz ən aşağı qiymət (ən yaxşı "alış" günü)
- max_profit: indiyə qədər əldə edilə bilən ən böyük mənfəət

Hər gün üçün:
1. Əgər bu günün qiyməti min_price-dan aşağıdırsa, min_price-ı yeniləyirik
   (çünki daha ucuz alış imkanı tapmışıq).
2. Əks halda, bu gün satsaq nə qədər mənfəət əldə edərdik (price - min_price)
   hesablayıb, max_profit ilə müqayisə edib böyüyünü saxlayırıq.

Bu üsulla massivi yalnız bir dəfə gəzməklə, bütün "al-sat" cütlüklərini
yoxlamadan (ki, bu O(n^2) olardı) nəticəni tapırıq.

Zaman Mürəkkəbliyi: O(n) — massiv bir dəfə gəzilir
Yaddaş Mürəkkəbliyi: O(1) — yalnız iki dəyişən saxlanılır
"""


def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            best_profit = max(best_profit, price - min_price)

    return best_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))      # 0
