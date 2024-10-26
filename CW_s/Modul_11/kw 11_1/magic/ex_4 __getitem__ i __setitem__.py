# __getitem__ i __setitem__ => [ ]

from collections import UserList

class PositiveNumber(UserList):
    def __init__(self, data=[]):
        super(PositiveNumber, self).__init__()
        self.data = [el for el in list(filter(lambda x: x > 0, data))]

    def __getitem__(self, index):  # Буде спрацьовувати завжди коли ми звертаємось по індексу
        if index is None:
            return self.data
        return self.data[index]

    def __setitem__(self, key, value):
        if value > 0 and key < len(self.data):
            self.data[key] = value

    def append(self, item) -> None:
        if item > 0:
            self.data.append(item)

nums = PositiveNumber([2, -4, 5])
print(nums)
print(nums[None])
print(nums[1])
nums[1] = -2
nums[1] = 3
print(nums[None])
nums.append(-4)
print(nums[None])