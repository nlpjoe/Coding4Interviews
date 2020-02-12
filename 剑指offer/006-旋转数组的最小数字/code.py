class Solution(object):
    def minArray(self, numbers):
        low, high = 0, len(numbers) - 1
        while low < high:
            mid = (high+low) / 2
            if numbers[mid] > numbers[high]:
                low = mid + 1
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                high -= 1
        return numbers[low]
