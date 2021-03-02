def helper(x, y, m, f, steps):
    print("-----------")
    print(x,y,m,f,steps)
    if x == 1 and y == 1:
        return [0, True]
    if x == m+f and y == f:
        return [steps, True]
    if y == m+f and x == m:
        return [steps, True]
    if x < m or y < f:
        return ["Impossible", False]

    choice1 = helper(x, y, m+f, f, steps+1)
    choice2 = helper(x, y, m, m+f, steps+1)

    if choice1[1] == False and choice2[1] == False:
        return ["Impossible", False]
    elif choice1[1] == True:
        return [choice1[0], True]
    else:
        return [choice2[0], True]

def solution(x, y):
    # Your code here
    ans = helper(x, y, 1, 1, 1)
    return str(ans[0])

print(solution(1,2))
print(solution(2,4))
print(solution(3,1))
print(solution(4,7))
