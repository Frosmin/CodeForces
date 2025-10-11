# ...existing code...
lista = [1,2,3,4,5,6,7,8,9]
# ...existing code...

from typing import List

NEG_INF = float('-inf')

class SegmentTreeMax:
    """
    Segment Tree (iterativo) para máximo en rango [l, r] 0-indexado.
    Build: O(n), query/update: O(log n)
    """
    def __init__(self, data: List[int]) -> None:
        n = len(data)
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.tree = [NEG_INF] * (2 * self.size)
        # hojas
        self.tree[self.size:self.size + n] = data
        # construir
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l: int, r: int) -> int:
        if l > r:
            return NEG_INF
        l += self.size
        r += self.size
        res = NEG_INF
        while l <= r:
            if l & 1:
                res = max(res, self.tree[l]); l += 1
            if not (r & 1):
                res = max(res, self.tree[r]); r -= 1
            l >>= 1; r >>= 1
        return res

    def update(self, idx: int, value: int) -> None:
        i = idx + self.size
        self.tree[i] = value
        i >>= 1
        while i:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i >>= 1

# Ejemplo:
# st = SegmentTreeMax(lista)
# print(st.query(2, 6))  # -> 7
# st.update(3, 100)
# print(st.query(2, 6))  # -> 100