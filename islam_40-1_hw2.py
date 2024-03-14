class Figure:
    def __init__(self):
        self._perimeter = 0

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):
        self._perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self._side_length = side_length
        self.calculate_perimeter()

    def calculate_area(self):
        return self._side_length ** 2

    def calculate_perimeter(self):
        self.perimeter = 4 * self._side_length

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self._side_length}cm, perimeter: {self.perimeter}cm, area: {area}cm")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self._length = length
        self._width = width
        self.calculate_perimeter()

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        self.perimeter = 2 * (self._length + self._width)

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self._length}cm, width: {self._width}cm, perimeter: {self.perimeter}cm, area: {area}cm")


figures = [Square(5), Square(7), Rectangle(4, 6), Rectangle(3, 8), Rectangle(5, 9)]

print("Информация о фигурах:")
for figure in figures:
    figure.info()



