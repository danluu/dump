import unittest

class Node:
    def __init__(self, val):
        self.val = val

def heap_init():
    return [None]

def swap(h, i, j):
    h[i], h[j] = h[j], h[i]

def bubble_up(h, i):
    if i <= 1:
        return

    p = i // 2
    if h[p].val > h[i].val:
        swap(h, p, i)
        bubble_up(h, p)

def sift_down(h, i):
    left = i * 2
    right = i * 2 + 1

    if left >= len(h) and right >= len(h):
        return
    candidate = -1
    if left >= len(h):
        candidate = right
    elif right >= len(h):
        candidate = left
    elif h[left].val < h[right].val:
        candidate = left
    else:
        candidate = right

    if h[candidate].val < h[i].val:
        swap(h, candidate, i)
        sift_down(h, candidate)

def heap_push(h, x):
    h.append(x)
    bubble_up(h, len(h) - 1)

def heap_pop(h):
    swap(h, 1, len(h) - 1)
    res = h.pop()
    sift_down(h, 1)
    return res
    
class TestHeap(unittest.TestCase):
    def test_init(self):
        h = heap_init()
        assert(len(h) == 1)

    def test_trivial(self):
        h = heap_init()
        heap_push(h,Node(1))

        self.assertEqual(heap_pop(h).val, 1)

    def test_trivial2(self):
        h = heap_init()
        heap_push(h,Node(2))
        heap_push(h,Node(3))
        heap_push(h,Node(1))
        heap_push(h,Node(4))

        self.assertEqual(heap_pop(h).val, 1)
        self.assertEqual(heap_pop(h).val, 2)
        self.assertEqual(heap_pop(h).val, 3)
        self.assertEqual(heap_pop(h).val, 4)


if __name__ == '__main__':
    unittest.main()
