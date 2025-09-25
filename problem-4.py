
# problem 4 : total count of number listed in the dictonary which is multiple [1,2,3,4,5,6,7,8,9]

class MultipleCounter:
    def __init__(self, numbers):
        self.numbers = numbers

    def count_multiples(self):
        result = {}
        for d in range(1, 10): 
            count = 0
            for num in self.numbers:
                if num % d == 0:
                    count += 1
            result[d] = count
        return result
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
counter = MultipleCounter(nums)
print(counter.count_multiples())