'''input
5 1 3 9
'''
# LIS using segment tree O(nlog(n)) time complexity.
from sys import stdin


# query function O(log(n)) 
def query(tree, index, start, end, qs, qe):
    # No overlap
    if qs > end or qe < start:
        return 0

    # total overlap
    if qs <= start and end <= qe:
        return tree[index]

    # partial overlap
    else:
        mid = (start + end) // 2
        left = query(tree, 2 * index, start, mid, qs, qe)
        right = query(tree, 2 * index + 1, mid + 1, end, qs, qe)
        return max(left, right)


# update the given node. Time complexity is O(log(n))
def update_node(tree, index, start, end, n_index, inc):
    # No overlap
    if n_index < start or n_index > end:
        return

    # reach the node
    if start == end:
        tree[index] = inc
        return

    # partial or complete overlap
    else:
        mid = (start + end) // 2
        update_node(tree, 2 * index, start, mid, n_index, inc)
        update_node(tree, 2 * index + 1, mid + 1, end, n_index, inc)
        tree[index] = max(tree[2 * index], tree[2 * index + 1])


# main starts
arr = list(map(int, stdin.readline().split()))
sorted_index = [i[0] for i in sorted(enumerate(arr), key=lambda x:x[1])]

tree = [0] * (4 * len(arr))
index = 1
start = 0
end = len(arr) - 1
for i in range(0, len(arr)):
    mymax = query(tree, index, start, end, 0, sorted_index[i] - 1)
    update_node(tree, index, start, end, sorted_index[i], mymax + 1)
print(tree[1])
