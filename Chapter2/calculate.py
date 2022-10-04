class Calculate():
    def add(self, x: int, y: int) -> int:
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {0} and {1}".format(type(x), type(y)))


if __name__ == '__main__':
    calc = Calculate()
    result = calc.add("Hello", "World")
    print(result)
