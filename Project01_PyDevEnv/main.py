from rectangle import Rectangle

def main():
    box = Rectangle(5.0, 3.0)
    print("Valid Rectangle")
    print(f"Length: {box.get_length()}")
    print(f"Width: {box.get_width()}")
    print(f"Area: {box.get_area()}")

    invalid_box = Rectangle(-4.0, 6.0)

    print()
    print("Invalid Length Rectangle")
    print(f"Length: {invalid_box.get_length()}")
    print(f"Width: {invalid_box.get_width()}")
    print(f"Area: {invalid_box.get_area()}")

if __name__ == "__main__":
    main()
