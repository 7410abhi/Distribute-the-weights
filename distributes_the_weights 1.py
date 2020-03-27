def possible(arr,m,k):
    subset = 1
    curr_sub = arr[0]
    flag = True
    for i in range(1, len(arr)):
        if curr_sub + arr[i]>k:
            curr_sub = arr[i]
            subset = subset +1
        else:
            curr_sub = curr_sub + arr[i]

        if subset > m:
            flag = False
            break
    return(flag)    

T = int(input())
for _ in range(T):
    inp = list(map(int, input().split()))
    m = inp[1]
    arr = list(map(int, input().split()))
    

    L = max(arr)
    U = sum(arr)
    mid = L+U//2
    ans = []
    
    while (L<=U):
        if (possible(arr,m,mid):
            ans.append(mid)
            U = mid - 1
        else:
            L = mid + 1
            
        mid = L+U//2    
            
    print(min(ans))        
            
