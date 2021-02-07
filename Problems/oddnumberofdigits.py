class Solution:
    def solve(self, nums):
        count = 0
        arr = []
        new = []
        for i in nums:

            arr[:] = str(i)
            if (len(arr) % 2 != 0):
                new.append(i)
        return len(new)

obj=Solution()
a=obj.solve([1,100,52,3,4,9])
print(a)