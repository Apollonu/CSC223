from circle import Circle
from rectangle import Rectangle
from square import Square

def demo():
    shapes = [
        Circle(0, 0, 5),
        Circle(4, -2, 6, name = "Large Circle"),
        Rectangle(3, 6),
        Rectangle(7, 4, name = "Wide Rectangle"),
        Square(5)
    ]

    print("Blank state")
    for i in shapes:
        print(f"{i.name}: area = {i.area:.2f}")

    shapes[0].radius = 5
    shapes[2].length = 9
    shapes[2].width = 3
    shapes[4].side = 7

    print("\nModified state")
    for i in shapes:
        print(f"{i.name}: area = {i.area:.2f}")

if __name__ == "__main__":
    demo()
