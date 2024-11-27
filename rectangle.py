# rectangle.py

def area(length, width):
    """
    Вычисляет площадь прямоугольника.
    """
    if length < 0 or width < 0:
        raise ValueError("Длины сторон должны быть неотрицательными.")
    return length * width


def perimeter(length, width):
    """
    Вычисляет периметр прямоугольника.
    """
    if length < 0 or width < 0:
        raise ValueError("Длины сторон должны быть неотрицательными.")
    return 2 * (length + width)
