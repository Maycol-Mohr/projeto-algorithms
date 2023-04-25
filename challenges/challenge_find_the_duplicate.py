def find_duplicate(nums):
    array_vazio = {}

    for num in nums:
        if type(num) != int:
            return False

        if num < 1:
            return False

        if num not in array_vazio:
            array_vazio[num] = num
        else:
            return num

        # if nums.count(num) > 1:
        #     return num

    return False


print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
