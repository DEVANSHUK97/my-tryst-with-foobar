def solution(n):
    # Your code here
    ans_arr = [-1,0,1]

    if n < len(ans_arr):
        return ans_arr[n]

    for loc in range(3,n+1):
        if loc%2 == 0:
            candidate_by_subtracting_1 = ans_arr[loc-1]+1
            candidate_by_halving = ans_arr[loc//2]+1
            ans = min(candidate_by_subtracting_1, candidate_by_halving)
            ans_arr.append(ans)
        else:
            candidate_by_subtracting_1 = ans_arr[loc-1]+1
            candidate_by_halving_next = ans_arr[(loc+1)//2]+2
            ans = min(candidate_by_subtracting_1, candidate_by_halving_next)
            ans_arr.append(ans)
    return ans_arr[n]
