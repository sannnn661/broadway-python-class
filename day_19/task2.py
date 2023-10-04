"""Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.
Add the radius of the circles and print the result.
Do the above task using a method and then a magic method.
Compare the size of the circle and print the result using magic method. """

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type. You can only add Circles.")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Unsupported operand type. You can only compare Circles.")

    def __str__(self):
        return f"Circle with radius {self.radius}"

# Create two Circle objects
c1 = Circle(5)
c2 = Circle(3)

# Add the radii using the __add__ magic method
result_circle = c1 + c2
print(f"Result of adding circles: {result_circle}")

# Compare the sizes using the __lt__ magic method
if c1 < c2:
    print("c1 is smaller than c2")
elif c1 > c2:
    print("c1 is larger than c2")
else:
    print("c1 and c2 have the same size")



"""2nd Part"""

"""
Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.
Add the radius of the circles and print the result.
Do the above task using a method and then a magic method.
Compare the size of the circle and print the result using magic method.

"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def total_radius(self, other):
        return self.radius + other.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __gt__(self, other):
        return self.radius > other.radius


c1 = Circle(5)
c2 = Circle(10)
result = c1.radius + c2.radius
print(result)   # 15

result = c1.total_radius(c2)
print(result)

result = c1 + c2
print(result)

print(c1 > c2)  # True / False
