
def gettriple(nums):
    print(nums)
    n = len(nums)

    l = 0
    i = 1
    m = 2
    count = 0
    res = []
    while(i<n and l >=0 and m <n ):
        print(f"{l} {i} {m}")
        if abs(nums[l] - nums[i]) == abs(nums[m] - nums[i]):
            res.append([nums[l], nums[i], nums[m]])
            count+=1
            l-=1
            m+=1
        elif abs(nums[l] - nums[i]) < abs(nums[m] - nums[i]):
            l-=1
        else:
            m+=1
        if l <0 or m > n-1 :
            i+=1
            l = i-1
            m= i+1

    print("Results:")
    print(res)



if __name__ == "__main__":

    gettriple([2,3,4,5,6,9,12])