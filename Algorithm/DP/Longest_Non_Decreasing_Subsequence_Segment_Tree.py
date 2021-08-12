def update_tree(start, end, index, tree, qs, qe, value):
    # no overlap
    if qs > end or qe < start:
        return tree[index]

    # complete overlap
    if qe >= end and qs <= start:
        tree[index] = value
        return tree[index]
       
    # partial overlap
    mid = (start + end) // 2
    l = update_tree(start, mid, 2 * index, tree, qs, qe, value)
    r = update_tree(mid + 1, end, 2 * index + 1, tree, qs, qe, value)
    tree[index] = max(l, r)
    return tree[index]


def query_tree(start, end, index, tree, qs, qe):
    # no overlap
    if qs > end or qe < start:
        return 0

    # complete overlap
    if qe >= end and qs <= start:
        return tree[index]

    # partial overlap
    mid = (start + end) // 2
    l = query_tree(start, mid, 2 * index, tree, qs, qe)
    r = query_tree(mid + 1, end, 2 * index + 1, tree, qs, qe)
    return max(l, r)




def lis(arr):
    tree = [ 0 for x in range(4 * len(arr))]
    idxArr = []
    for i in range(len(arr)):
        idxArr.append([arr[i], i])
    idxArr.sort(key = lambda x: x[0])
    
    for i in range(len(arr)):
        maxLis  = query_tree(0, len(arr) - 1, 1, tree, 0, idxArr[i][1] - 1)
        update_tree(0, len(arr) - 1, 1, tree, idxArr[i][1], idxArr[i][1], maxLis + 1)
    return tree[1]



print(lis([1, 2, 3, 3, 5, 6, 7]))
