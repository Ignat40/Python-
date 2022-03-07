#Write a Python class MyMath and implement pow, factorial, floor, difference.


class MyMath:

    
    def pow(self, x, y):
        return x ** y

    def factorial(self, x):
        
        fact = 1
        for i in range(1, x + 1):
            fact *= i

        return fact

    def floor(self, x: float):
        return int(x)

    def difference(self, x, y):
        return x - y


if __name__ == '__main__':

    m = MyMath()
    print(m.factorial(5))  # 120
    print(m.floor(5.3))  # 5
    print(m.pow(2, 10))  # 1024
    print(m.difference(10, 6))  # 4
