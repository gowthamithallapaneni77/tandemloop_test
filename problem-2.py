#problem 2 : single integer = odd numbers




class OddSeries:
    def __init__(self, n):
        self.n = n  # no.of elements in the series

    def generate(self):
        series = []
        for i in range(self.n):
            series.append(2 * i + 1)  #ith odd number
        return series

# Example usage
a = int(input("Enter a single integer: "))
series_obj = OddSeries(a)
result = series_obj.generate()
print("Output:",result)

