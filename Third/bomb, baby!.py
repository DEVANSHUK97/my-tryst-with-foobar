def helper(x, y, m, f, steps):
    if x == 1 and y == 1:
        return [0, True]
    if x == m+f and y == f:
        return [steps, True]
    if y == m+f and x == m:
        return [steps, True]
    if x > m or y > f:
        return ["Impossible", False]
    choice1 = helper(x, y, m+f, f, steps+1)
    choice2 = helper(x, y, m, m+f, steps+1)

    if choice1[1] == False and choice2[1] == False:
        return ["Impossible", False]
    elif choice1[1] == True and choice2[1] == True:
        return [choice1[0], True]
    elif choice2[1] == True and choice1[1] == True:
        return [choice2[0], True]
    else:
        return [min(choice1[0], choice2[0]), True]

def solution(x, y):
    # Your code here
    ans = helper(x, y, 1, 1, 1)
    return string(ans[0])
