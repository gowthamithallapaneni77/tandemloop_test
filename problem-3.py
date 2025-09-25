


# problem3 
# increases at odd number 
# for even numbers prints previous odd numbers series 



class OddSeries:
    def __init__(self, n):
        self.n = n   # input number

    def generate(self):
        # largest odd number <= n
        if self.n % 2 == 0:
            length = self.n - 1
        else:
            length = self.n

        # odd number series
        series = []
        for i in range(length):
            series.append(2 * i + 1)
        return series
    
a = int(input("Enter a single integer: "))
series_obj = OddSeries(a)
result = series_obj.generate()
print(", ".join(map(str,result)))
