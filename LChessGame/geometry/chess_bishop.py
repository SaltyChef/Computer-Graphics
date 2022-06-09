from math import pi
from material.lambert import LambertMaterial
from core_ext.object3d import Object3D
from core.base import Base
from core_ext.mesh import Mesh
from core_ext.texture import Texture

from geometry.cylindrical import CylindricalGeometry
from geometry.ellipsoid import EllipsoidGeometry
from geometry.polygon import PolygonGeometry
from geometry.sphere import SphereGeometry

from material.surface import SurfaceMaterial
from material.texture import TextureMaterial


class ChessBishop(Base):
    def getObject3D(side=0):
        translate_to_center = -0.15
        radial_segment = 32

        geometry = EllipsoidGeometry(width=0.46, height=0.36, depth=0.46, radius_segments=32, height_segments=16)

        geometry2_1 = CylindricalGeometry(radius_top=0.15, radius_bottom=0.33, height=0.08, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry2_2 = CylindricalGeometry(radius_top=0.33, radius_bottom=0.45, height=0.11, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry2_3 = CylindricalGeometry(radius_top=0.45, radius_bottom=0.58, height=0.19, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry2_4 = CylindricalGeometry(radius_top=0.58, radius_bottom=0.71, height=0.24, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry2_5 = CylindricalGeometry(radius_top=0.71, radius_bottom=0.83, height=0.28, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry2_6 = CylindricalGeometry(radius_top=0.83, radius_bottom=0.94, height=0.3, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry2_7 = CylindricalGeometry(radius_top=0.94, radius_bottom=1.02, height=0.32, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False) 
        geometry2_8 = CylindricalGeometry(radius_top=1.02, radius_bottom=1.04, height=0.16, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        
        geometry3 = SphereGeometry(radius=1.05, radius_segments=radial_segment, height_segments=16)
        
        geometry4_1 = CylindricalGeometry(radius_top=0.74, radius_bottom=0.74, height=0.07, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_2 = CylindricalGeometry(radius_top=0.74, radius_bottom=0.84, height=0.05, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_3 = CylindricalGeometry(radius_top=0.84, radius_bottom=0.84, height=0.08, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_4 = CylindricalGeometry(radius_top=0.84, radius_bottom=0.74, height=0.05, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_5 = CylindricalGeometry(radius_top=0.74, radius_bottom=0.7, height=0.05, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_6 = CylindricalGeometry(radius_top=0.7, radius_bottom=0.7, height=0.08, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_7 = CylindricalGeometry(radius_top=0.7, radius_bottom=0.76, height=0.06, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_8 = CylindricalGeometry(radius_top=0.76, radius_bottom=0.86, height=0.04, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_9 = CylindricalGeometry(radius_top=0.86, radius_bottom=0.86, height=0.08, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_10 = CylindricalGeometry(radius_top=0.86, radius_bottom=0.81, height=0.02, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_11 = CylindricalGeometry(radius_top=0.81, radius_bottom=1.0, height=0.01, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_12 = CylindricalGeometry(radius_top=1.0, radius_bottom=1.18, height=0.03, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_13 = CylindricalGeometry(radius_top=1.18, radius_bottom=1.18, height=0.27, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry4_14 = CylindricalGeometry(radius_top=1.18, radius_bottom=1.0, height=0.03, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_15 = CylindricalGeometry(radius_top=1.0, radius_bottom=0.43, height=0.02, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry4_16 = CylindricalGeometry(radius_top=0.43, radius_bottom=0.38, height=0.05, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        
        geometry5_1 = CylindricalGeometry(radius_top=0.38, radius_bottom=0.37, height=0.15, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry5_2 = CylindricalGeometry(radius_top=0.37, radius_bottom=0.47, height=2.2, radial_segments=radial_segment, height_segments=14, closed_top=False, closed_bottom=False)
        geometry5_3 = CylindricalGeometry(radius_top=0.47, radius_bottom=0.54, height=0.53, radial_segments=radial_segment, height_segments=3, closed_top=False, closed_bottom=False)
        geometry5_4 = CylindricalGeometry(radius_top=0.54, radius_bottom=0.63, height=0.44, radial_segments=radial_segment, height_segments=3, closed_top=False, closed_bottom=False)
        geometry5_5 = CylindricalGeometry(radius_top=0.63, radius_bottom=0.77, height=0.28, radial_segments=radial_segment, height_segments=3, closed_top=False, closed_bottom=False)
        geometry5_6 = CylindricalGeometry(radius_top=0.77, radius_bottom=0.93, height=0.15, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry5_7 = CylindricalGeometry(radius_top=0.93, radius_bottom=1.1, height=0.06, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry5_8 = CylindricalGeometry(radius_top=1.1, radius_bottom=1.3, height=0.03, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        
        geometry6_1 = CylindricalGeometry(radius_top=1.3, radius_bottom=1.35, height=0.03, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry6_2 = CylindricalGeometry(radius_top=1.35, radius_bottom=1.33, height=0.17, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_3 = CylindricalGeometry(radius_top=1.33, radius_bottom=1.3, height=0.22, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_4 = CylindricalGeometry(radius_top=1.3, radius_bottom=1.32, height=0.3, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_5 = CylindricalGeometry(radius_top=1.32, radius_bottom=1.42, height=0.33, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_6 = CylindricalGeometry(radius_top=1.42, radius_bottom=1.58, height=0.23, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_7 = CylindricalGeometry(radius_top=1.58, radius_bottom=1.86, height=0.26, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_8 = CylindricalGeometry(radius_top=1.86, radius_bottom=1.88, height=0.26, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_9 = CylindricalGeometry(radius_top=1.88, radius_bottom=1.78, height=0.07, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry6_10 = CylindricalGeometry(radius_top=1.78, radius_bottom=1.78, height=0.04, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry6_11 = CylindricalGeometry(radius_top=1.78, radius_bottom=1.84, height=0.04, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry6_12 = CylindricalGeometry(radius_top=1.84, radius_bottom=1.88, height=0.03, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry6_13 = CylindricalGeometry(radius_top=1.88, radius_bottom=1.88, height=0.15, radial_segments=radial_segment, height_segments=2, closed_top=False, closed_bottom=False)
        geometry6_14 = CylindricalGeometry(radius_top=1.88, radius_bottom=1.82, height=0.04, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        geometry6_15 = CylindricalGeometry(radius_top=1.82, radius_bottom=1.7, height=0.03, radial_segments=radial_segment, height_segments=1, closed_top=False, closed_bottom=False)
        
        geometry7 = PolygonGeometry(sides=radial_segment, radius=1.7)
 
        # material = SurfaceMaterial(property_dict={"useVertexColors": True})


        # grid_texture = Texture(file_name='images/marbleBlack.jpg')
        # grid_texture = Texture(file_name='images/basalt1.jpg')
        
        grid_texture = Texture(file_name='images/whiteMarble.jpg')
        if side == 1:
            grid_texture = Texture(file_name='images/blackMarble.jpg')
        
        material = LambertMaterial(texture=grid_texture)

        mesh = Mesh(geometry, material)
        mesh.translate(0.0, 5.17, 0.0)

        mesh2_1 = Mesh(geometry2_1, material)
        mesh2_1.translate(0.0, translate_to_center, 0.0)

        mesh2_2 = Mesh(geometry2_2, material)
        mesh2_2.translate(0.0, -0.095 + translate_to_center, 0.0)

        mesh2_3 = Mesh(geometry2_3, material)
        mesh2_3.translate(0.0, -0.245 + translate_to_center, 0.0)

        mesh2_4 = Mesh(geometry2_4, material)
        mesh2_4.translate(0.0, -0.46 + translate_to_center, 0.0)

        mesh2_5 = Mesh(geometry2_5, material)
        mesh2_5.translate(0.0, -0.72 + translate_to_center, 0.0)

        mesh2_6 = Mesh(geometry2_6, material)
        mesh2_6.translate(0.0, -1.01 + translate_to_center, 0.0)

        mesh2_7 = Mesh(geometry2_7, material)
        mesh2_7.translate(0.0, -1.32 + translate_to_center, 0.0)

        mesh2_8 = Mesh(geometry2_8, material)
        mesh2_8.translate(0.0, -1.56 + translate_to_center, 0.0)

        mesh3 = Mesh(geometry3, material)
        mesh3.translate(0.0, -1.775 + translate_to_center, 0.0)

        mesh4_1 = Mesh(geometry4_1, material)
        mesh4_1.translate(0.0, -2.54 + translate_to_center, 0.0)

        mesh4_2 = Mesh(geometry4_2, material)
        mesh4_2.translate(0.0, -2.6 + translate_to_center, 0.0)

        mesh4_3 = Mesh(geometry4_3, material)
        mesh4_3.translate(0.0, -2.66 + translate_to_center, 0.0)

        mesh4_4 = Mesh(geometry4_4, material)
        mesh4_4.translate(0.0, -2.72 + translate_to_center, 0.0)

        mesh4_5 = Mesh(geometry4_5, material)
        mesh4_5.translate(0.0, -2.77 + translate_to_center, 0.0)

        mesh4_6 = Mesh(geometry4_6, material)
        mesh4_6.translate(0.0, -2.835 + translate_to_center, 0.0)

        mesh4_7 = Mesh(geometry4_7, material)
        mesh4_7.translate(0.0, -2.905 + translate_to_center, 0.0)

        mesh4_8 = Mesh(geometry4_8, material)
        mesh4_8.translate(0.0, -2.95 + translate_to_center, 0.0)

        mesh4_9 = Mesh(geometry4_9, material)
        mesh4_9.translate(0.0, -3.01 + translate_to_center, 0.0)

        mesh4_10 = Mesh(geometry4_10, material)
        mesh4_10.translate(0.0, -3.06 + translate_to_center, 0.0)

        mesh4_11 = Mesh(geometry4_11, material)
        mesh4_11.translate(0.0, -3.075 + translate_to_center, 0.0)

        mesh4_12 = Mesh(geometry4_12, material)
        mesh4_12.translate(0.0, -3.095 + translate_to_center, 0.0)

        mesh4_13 = Mesh(geometry4_13, material)
        mesh4_13.translate(0.0, -3.24 + translate_to_center, 0.0)

        mesh4_14 = Mesh(geometry4_14, material)
        mesh4_14.translate(0.0, -3.39 + translate_to_center, 0.0)

        mesh4_15 = Mesh(geometry4_15, material)
        mesh4_15.translate(0.0, -3.414 + translate_to_center, 0.0)

        mesh4_16 = Mesh(geometry4_16, material)
        mesh4_16.translate(0.0, -3.449 + translate_to_center, 0.0)

        mesh5_1 = Mesh(geometry5_1, material)
        mesh5_1.translate(0.0, -3.549 + translate_to_center, 0.0)

        mesh5_2 = Mesh(geometry5_2, material)
        mesh5_2.translate(0.0, -4.724 + translate_to_center, 0.0)

        mesh5_3 = Mesh(geometry5_3, material)
        mesh5_3.translate(0.0, -6.089 + translate_to_center, 0.0)

        mesh5_4 = Mesh(geometry5_4, material)
        mesh5_4.translate(0.0, -6.574 + translate_to_center, 0.0)

        mesh5_5 = Mesh(geometry5_5, material)
        mesh5_5.translate(0.0, -6.934 + translate_to_center, 0.0)

        mesh5_6 = Mesh(geometry5_6, material)
        mesh5_6.translate(0.0, -7.149 + translate_to_center, 0.0)

        mesh5_7 = Mesh(geometry5_7, material)
        mesh5_7.translate(0.0, -7.254 + translate_to_center, 0.0)

        mesh5_8 = Mesh(geometry5_8, material)
        mesh5_8.translate(0.0, -7.299 + translate_to_center, 0.0)

        mesh6_1 = Mesh(geometry6_1, material)
        mesh6_1.translate(0.0, -7.329 + translate_to_center, 0.0)

        mesh6_2 = Mesh(geometry6_2, material)
        mesh6_2.translate(0.0, -7.43 + translate_to_center, 0.0)

        mesh6_3 = Mesh(geometry6_3, material)
        mesh6_3.translate(0.0, -7.625 + translate_to_center, 0.0)

        mesh6_4 = Mesh(geometry6_4, material)
        mesh6_4.translate(0.0, -7.885 + translate_to_center, 0.0)

        mesh6_5 = Mesh(geometry6_5, material)
        mesh6_5.translate(0.0, -8.2 + translate_to_center, 0.0)

        mesh6_6 = Mesh(geometry6_6, material)
        mesh6_6.translate(0.0, -8.48 + translate_to_center, 0.0)

        mesh6_7 = Mesh(geometry6_7, material)
        mesh6_7.translate(0.0, -8.725 + translate_to_center, 0.0)

        mesh6_8 = Mesh(geometry6_8, material)
        mesh6_8.translate(0.0, -8.985 + translate_to_center, 0.0)

        mesh6_9 = Mesh(geometry6_9, material)
        mesh6_9.translate(0.0, -9.15 + translate_to_center, 0.0)

        mesh6_10 = Mesh(geometry6_10, material)
        mesh6_10.translate(0.0, -9.205 + translate_to_center, 0.0)

        mesh6_11 = Mesh(geometry6_11, material)
        mesh6_11.translate(0.0, -9.245 + translate_to_center, 0.0)

        mesh6_12 = Mesh(geometry6_12, material)
        mesh6_12.translate(0.0, -9.28 + translate_to_center, 0.0)

        mesh6_13 = Mesh(geometry6_13, material)
        mesh6_13.translate(0.0, -9.37 + translate_to_center, 0.0)

        mesh6_14 = Mesh(geometry6_14, material)
        mesh6_14.translate(0.0, -9.465 + translate_to_center, 0.0)

        mesh6_15 = Mesh(geometry6_15, material)
        mesh6_15.translate(0.0, -9.5 + translate_to_center, 0.0)

        mesh7 = Mesh(geometry7, material)
        mesh7.translate(0.0, -9.515 + translate_to_center, 0.0)
        mesh7.rotate_x(pi/2)

        mesh.add(mesh2_1)
        mesh.add(mesh2_2)
        mesh.add(mesh2_3)
        mesh.add(mesh2_4)
        mesh.add(mesh2_5)
        mesh.add(mesh2_6)
        mesh.add(mesh2_7)
        mesh.add(mesh2_8)
        mesh.add(mesh3)
        mesh.add(mesh4_1)
        mesh.add(mesh4_2)
        mesh.add(mesh4_3)
        mesh.add(mesh4_4)
        mesh.add(mesh4_5)
        mesh.add(mesh4_6)
        mesh.add(mesh4_7)
        mesh.add(mesh4_8)
        mesh.add(mesh4_9)
        mesh.add(mesh4_10)
        mesh.add(mesh4_11)
        mesh.add(mesh4_12)
        mesh.add(mesh4_13)
        mesh.add(mesh4_14)
        mesh.add(mesh4_15)
        mesh.add(mesh4_16)
        mesh.add(mesh5_1)
        mesh.add(mesh5_2)
        mesh.add(mesh5_3)
        mesh.add(mesh5_4)
        mesh.add(mesh5_5)
        mesh.add(mesh5_6)
        mesh.add(mesh5_7)
        mesh.add(mesh5_8)
        mesh.add(mesh6_1)
        mesh.add(mesh6_2)
        mesh.add(mesh6_3)
        mesh.add(mesh6_4)
        mesh.add(mesh6_5)
        mesh.add(mesh6_6)
        mesh.add(mesh6_7)
        mesh.add(mesh6_8)
        mesh.add(mesh6_9)
        mesh.add(mesh6_10)
        mesh.add(mesh6_11)
        mesh.add(mesh6_12)
        mesh.add(mesh6_13)
        mesh.add(mesh6_14)
        mesh.add(mesh6_15)
        mesh.add(mesh7)

        chess_bishop = Object3D()
        chess_bishop.add(mesh)
        return chess_bishop
