from geometry.my_cylindrical import CylindricalGeometry
from math import pi


class myCylinderGeometry(CylindricalGeometry):
    def __init__(self, radius=0.05, height=0.25, radial_segments=32, height_segments=4, closed=False):
        super().__init__(radius, radius, height, radial_segments, height_segments, closed, closed)