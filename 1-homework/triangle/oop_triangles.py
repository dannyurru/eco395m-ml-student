from base_triangle import BaseTriangle
    
class IsoscelesTriangle(BaseTriangle):
    
    def __init__(self, leg, base):

       self.side_a = leg
       self.side_b = leg
       self.side_c = base
       self.base = base
       self.height = (leg**2 - (base / 2)**2) ** (1/2)
       BaseTriangle.__init__(self, self.side_a, self.side_b, self.side_c, self.base, self.height)

    def _get_sides(self):
          return (self.side_a, self.side_b, self.side_c)
    
    # leave as an exercise
    def _get_base_height(self):
        return (self.base, self.height)
    
class RightTriangle(BaseTriangle):
    def __init__(self, leg_a, leg_b):
        self.side_a = leg_a
        self.side_b = leg_b
        self.side_c = (leg_a**2 + leg_b**2) ** 0.5
        self.base = leg_a
        self.height = leg_b
        BaseTriangle.__init__(self, self.side_a, self.side_b, self.side_c, self.base, self.height)

    pass
    
if __name__ == "__main__":
    
    right_triangle = RightTriangle(leg_a=3, leg_b=4)
    assert right_triangle.calc_area() == (1 / 2) * 3 * 4
    assert right_triangle.calc_perimeter() == 3 + 4 + 5

    isosceles_triangle  = IsoscelesTriangle(leg=5, base=6)
    assert isosceles_triangle.calc_area() == (1 / 2) * 6 * 4
    assert isosceles_triangle.calc_perimeter() == 6 + 5 + 5
