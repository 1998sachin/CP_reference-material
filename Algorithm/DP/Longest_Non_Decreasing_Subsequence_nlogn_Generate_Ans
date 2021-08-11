# Idea by Tushar Roy Youtube

from bisect import bisect_right


def lis(arr):
    c = [] # stores index
    cArr = [] # stores value at index, required for binary search
    ans = [-1 for x in range(len(arr))] # to generate ans
    for i in range(len(arr)):
        if i == 0:
            c.append(i)
            cArr.append(arr[i])
            ans[i] = -1
        else:
            index = bisect_right(cArr, arr[i])
            if(index >= len(c)):
                ans[i] = c[-1]
                c.append(i)
                cArr.append(arr[i])
            else:
                if index - 1 < 0:
                    ans[i] = -1
                else:
                    ans[i] = c[index - 1]
                c[index] = i
                cArr[index] = arr[i]
    return len(c)


print(lis([2, 10, 5, 1, 8, 6, 6, 6, 5]))
