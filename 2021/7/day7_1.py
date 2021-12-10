def get_diff(nums, pos):
    count = 0
    for n in nums:
        count += abs(n - pos)
    return count

with open('day7_1.txt') as file:
    lines = file.readlines()
    nums = [int(x) for x in lines[0].strip().split(',')]
    print(get_diff(nums, 1))
    print(get_diff(nums, 2))
    print(get_diff(nums, 3))
    print(get_diff(nums, 10))
    #exit(0)
    left = 0
    right = max(nums)
    while abs(left - right) > 1:
        middle = left + ((right - left) // 2)
        print(left, middle, right)
        right_half = middle + ((right - middle) // 2)
        left_half = left + ((middle - left) // 2)
        right_diff = get_diff(nums, right_half)
        left_diff = get_diff(nums, left_half)
        print(left_half, right_half)
        print(left_diff, right_diff)
        if (left_diff < right_diff):
            right = middle
        else:
            left = middle
        #input()

    print(left, right)
    print(min(get_diff(nums,left), get_diff(nums,right)))
