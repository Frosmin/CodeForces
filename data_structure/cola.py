from collections import deque
import sys

input = sys.stdin.buffer.readline


cola = deque()

cola.append(1)
cola.appendleft(2)
print(cola)

