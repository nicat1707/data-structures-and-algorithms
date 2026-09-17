"""
Stack (Yığın) — Veri Yapısı

Məzmun: LIFO (Last In, First Out) prinsipi ilə işləyən strukturdur —
sonuncu əlavə edilən element birinci çıxarılır.

Yanaşma (Approach):
Python list-i üzərində append() və pop() metodları ilə həyata keçirilir.

Zaman Mürəkkəbliyi: O(1) — push və pop əməliyyatları
Yaddaş Mürəkkəbliyi: O(n) — n element saxlanılır
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())   # 3
    print(s.peek())  # 2
