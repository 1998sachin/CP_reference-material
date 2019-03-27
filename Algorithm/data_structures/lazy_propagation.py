# lazy propagation solution of adding 1 in l to r indices of an array, return max element in l to r
# hackerrank problem
from sys import stdin


def update(seg_tree, lazy_tree, index, start, end, qs, qe):
    # updating from lazy tree
    seg_tree[index] += lazy_tree[index]
    if start != end:
        lazy_tree[2 * index] += lazy_tree[index]
        lazy_tree[2 * index + 1] += lazy_tree[index]
    lazy_tree[index] = 0

    # no overlap
    if qe < start or qs > end:
        return

    # total overlap
    if qs <= start and qe >= end:
        seg_tree[index] += 1
        if start != end:
            lazy_tree[2 * index] += 1
            lazy_tree[2 * index + 1] += 1
        return

    # partial overlap
    mid = (start + end) // 2
    update(seg_tree, lazy_tree, 2 * index, start, mid, qs, qe)
    update(seg_tree, lazy_tree, 2 * index + 1, mid + 1, end, qs, qe)
    seg_tree[index] = max(seg_tree[2 * index], seg_tree[2 * index + 1])
    return


def query(seg_tree, lazy_tree, index, start, end, qs, qe):
    # updating from lazy tree
    seg_tree[index] += lazy_tree[index]
    if start != end:
        lazy_tree[2 * index] += lazy_tree[index]
        lazy_tree[2 * index + 1] += lazy_tree[index]
    lazy_tree[index] = 0

    # no overlap
    if qe < start or qs > end:
        return -float('inf')

    # total overlap
    if qs <= start and qe >= end:
        return seg_tree[index]

    # partial overlap
    mid = (start + end) // 2
    left = query(seg_tree, lazy_tree, 2 * index, start, mid, qs, qe)
    right = query(seg_tree, lazy_tree, 2 * index + 1, mid + 1, end, qs, qe)
    return max(left, right)
    

# main starts
n, q = list(map(int, stdin.readline().split()))
seg_tree = [0] * (4 * n)
lazy_tree = [0] * (4 * n)
start = 0; end = n - 1; index = 1
while q > 0:
    t, l, r = list(map(int, stdin.readline().split()))
    if t == 0:
        update(seg_tree, lazy_tree, index, start, end, l, r)
        #print(seg_tree, lazy_tree)
    else:
        print(query(seg_tree, lazy_tree, index, start, end, l, r))
        #print(seg_tree, lazy_tree)
    q -= 1
