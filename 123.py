def maxAscendingSum(nums):
    sum_arr = 0
    sum_tmp = 0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            sum_tmp += nums[i]
        else:
            sum_tmp += nums[i]
            sum_arr = sum_tmp
            sum_tmp = 0

    print(sum_arr)
maxAscendingSum([10,20,30,5,10,50])