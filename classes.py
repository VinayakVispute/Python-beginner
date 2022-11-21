# Class declaration
class Point:
    def __init__(self, x=0, y=0):
        print("eh")  # Constructor
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()   # Objects Creation
# point1.move()
# point1.draw()
# print(point1.x)
# print(point1.y)

# point2 = Point(2, 3)
# print(point2.x)
# print(point2.y)
# point2.x = 33
# print(point2.x)
