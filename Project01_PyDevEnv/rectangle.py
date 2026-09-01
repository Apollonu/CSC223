class Rectangle:
    def __init__(self, length=0.0, width=0.0):
        self.length = 0.0
        self.width = 0.0
        self.set_length(length)
        self.set_width(width)
    def set_length(self, length):
        if length >= 0:
            self.length = length
        else:
            self.length = 0.0
    def set_width(self, width):
        if width >= 0:
            self.width = width
        else:
            self.width = 0.0
    def get_length(self):
        return self.length
    def get_width(self):
        return self.width
    def get_area(self):
        return self.length * self.width
