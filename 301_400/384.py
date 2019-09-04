# 384 shuffle an array 打乱一个数组

__author__ = 'YangXuan (jumpthepig@gmail.com)'


import random


class Solution:

    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            index = random.randrange(i, len(self.array))
            self.array[index], self.array[i] = self.array[i], self.array[index]
        return self.array


case1 = [1, 2, 3]
obj = Solution(case1)
p1 = obj.reset()
print(p1)
p2 = obj.shuffle()
print(p2)
