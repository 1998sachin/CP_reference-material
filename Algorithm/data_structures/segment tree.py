# segment tree implementation 
# minimum query 


infinite = 10**25   # a value representing infinite


# builds the segment tree.... time complexity O(n)
def build_segment_tree(tree, a, index, start, end):
    if start > end:
        return

    # for node element
    if start == end:
        tree[index] = a[start]

    # for internal node
    else:
        mid = (start + end) // 2
        build_segment_tree(tree, a, 2 * index, start, mid)
        build_segment_tree(tree, a, 2 * index + 1, mid + 1, end)
        tree[index] = min(tree[2 * index], tree[2 * index + 1])


# query function. Outputs the minimum element in the given range. Time complexity is O(log(n))
def query(tree, a, index, start, end, qs, qe):
    global infinte
    # No overlap
    if qs > end or qe < start:
        return infinite

    # total overlap
    if qs <= start and end <= qe:
        return tree[index]

    # partial overlap
    else:
        mid = (start + end) // 2
        left = query(tree, a, 2 * index, start, mid, qs, qe)
        right = query(tree, a, 2 * index + 1, mid + 1, end, qs, qe)
        return min(left, right)


# update the given node. Time complexity is O(log(n))
def update_node(tree, a, index, start, end, n_index, inc):
    # No overlap
    if n_index < start or n_index > end:
        return

    # reach the node
    if start == end:
        tree[index] += inc
        return

    # partial or complete overlap
    else:
        mid = (start + end) // 2
        update_node(tree, a, 2 * index, start, mid, n_index, inc)
        update_node(tree, a, 2 * index + 1, mid + 1, end, n_index, inc)
        tree[index] = min(tree[ 2 * index], tree[ 2 * index + 1])
        return


# update element in the given range. Time complexity is O(n).
def update_range(tree, a, index, start, end, rs, re, inc):
    # No overlap
    if re < start or rs > end:
        return

    # reach the node
    if start == end:
        tree[index] += inc
        return

    # partial or complete overlap
    else:
        mid = (start + end) // 2
        update_range(tree, a, 2 * index, start, mid, rs, re, inc)
        update_range(tree, a, 2 * index + 1, mid + 1, end, rs, re, inc)
        tree[index] = min(tree[ 2 * index], tree[ 2 * index + 1])
        return


# main starts
a = [1, 4, -2, 5]
tree = [0] * (4 * len(a))
index = 1
start = 0
end = len(a) - 1
build_segment_tree(tree, a, index, start, end)
print(tree)
for i in range(3):
    n_index, inc = list(map(int, input().split()))
    update_node(tree, a, index, start, end, n_index, inc)
    print(tree)
