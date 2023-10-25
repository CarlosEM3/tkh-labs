# 1) Write a definition for a class named Circle with attributes center and
# radius,where center is a Point tuple and radius is a number
class Circle:
    def __init__(self, center = (0,0), radius =1): 
        self.center = center
        self.radius = radius

# 2) Instantiate a Circle object that represents a circle with
# its center at (150, 100) and radius 75
circ = Circle(center = (150,100), radius = 75)

print()

# 3) Write a function named point_in_circle that takes a
# Circle and a Point and returns True if the
# Point lies in or on the boundary of the circle.
# DOCS: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
def point_in_circle(circle, point):
    circle = (x,y)
    point_x = x
    point_y = y
    circ.center = (x - x.circle)**2 + (y-ycenter)**2 < circl.radius 
    ...
    
