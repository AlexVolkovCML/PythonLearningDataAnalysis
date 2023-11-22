class Rectangle:                                     #
    def __init__(self, height, width):               # класс принимает 2 параметра
        self.height = height
        self.width = width


    def perimeter(self):                             #метод, возвращает значение периметра
        return 2 * (self.height + self.width)

    def square(self):                                #метод, возвращает значение площади
        return self.height * self.width
