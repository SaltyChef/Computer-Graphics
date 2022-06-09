"""An example of a basic scene: spinning cube"""
from operator import ge
from re import T
from geometry.sphere import SphereGeometry
from core_ext.object3d import Object3D
from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from material.lambert import LambertMaterial

from geometry.cylinder import CylinderGeometry
from geometry.cone import ConeGeometry
from geometry.pyramid import PyramidGeometry
from geometry.cylindrical import CylindricalGeometry
from geometry.geometry import Geometry
from geometry.parametric import ParametricGeometry
from geometry.box import BoxGeometry
from geometry.ellipsoid import EllipsoidGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from material.texture import TextureMaterial



class ChessKing(Base):
    
    
    def getObject3D(side=0):
        base_radius = 0.6
        geometry_cylinder = CylinderGeometry(radius=0.2, height=2, radial_segments=64, height_segments=4, closed=False)
        geometry_base = CylinderGeometry(radius=base_radius, height=0.3, radial_segments=32, height_segments=3, closed=False)
        geometry_base_tamp_up = EllipsoidGeometry(width=base_radius*2, height=0, depth=base_radius*2, radius_segments=32, height_segments=16)
        geometry_base_tamp_down = EllipsoidGeometry(width=base_radius*2, height=0, depth=base_radius*2, radius_segments=32, height_segments=16)
        geometry_base_tamp_cone = ConeGeometry(radius=base_radius, height=1.0, radial_segments=32, height_segments=4, closed=False)

        geometry_head = ConeGeometry(radius=base_radius, height=0.8, radial_segments=32, height_segments=4, closed=False)
        geometry_head_base = EllipsoidGeometry(width=base_radius*(3/2), height=0.1, depth=base_radius*(3/2), radius_segments=32, height_segments=16)
        geometry_head_tamp = EllipsoidGeometry(width=base_radius*2, height=0, depth=base_radius*2, radius_segments=32, height_segments=16)

        geometry_head_tamp_2 = EllipsoidGeometry(width=base_radius, height=0.3, depth=base_radius, radius_segments=32, height_segments=16)
        # g = CylinderGeometry( radius=1, height=2, radial_segments=64, height_segments=4, closed=False)

        x = 0.15
        y = 0.4
        geometry_head_x_vertical = BoxGeometry(width=x, height=y, depth=0.1)
        geometry_head_x_horizontal = BoxGeometry(width=y, height=x, depth=0.1)

        grid_texture = Texture(file_name='images/whiteMarble.jpg')
        if side == 1:
            grid_texture = Texture(file_name='images/blackMarble.jpg')
        
        material = LambertMaterial(texture=grid_texture)
    

        mesh = Mesh(geometry_base, material)
        mesh.translate(0.0, -2, 0.0)

        mesh1 = Mesh(geometry_cylinder, material)
        mesh1.translate(0.0, 1.5, 0.0)

        mesh2 = Mesh(geometry_base_tamp_up, material)
        mesh2.translate(0.0, 0.14, 0.0)

        mesh3 = Mesh(geometry_base_tamp_cone, material)
        mesh3.translate(0.0, 0.4, 0.0)

        mesh4 = Mesh(geometry_head, material)
        mesh4.translate(0.0, 2.2, 0.0)
        mesh4.rotate_x(3.14)

        mesh5 = Mesh(geometry_head_base, material)
        mesh5.translate(0.0, 2.1, 0.0)

        mesh6 = Mesh(geometry_head_tamp, material)
        mesh6.translate(0.0, 2.6, 0.0)

        mesh7 = Mesh(geometry_head_tamp_2, material)
        mesh7.translate(0.0, 2.6, 0.0)

        mesh8 = Mesh(geometry_head_x_vertical, material)
        mesh8.translate(0.0, 2.9, 0.0)

        mesh9 = Mesh(geometry_base_tamp_down, material)
        mesh9.translate(0.0, -0.15, 0.0)

        mesh10 = Mesh(geometry_head_x_horizontal, material)
        mesh10.translate(0.0, 2.9, 0.0)

        # m = Mesh(g, material)
        mesh.add(mesh1)
        mesh.add(mesh2)
        mesh.add(mesh3)
        mesh.add(mesh4)
        mesh.add(mesh5)
        mesh.add(mesh6)
        mesh.add(mesh7)
        mesh.add(mesh8)
        mesh.add(mesh9)
        mesh.add(mesh10)
        # self.mesh.add(m)
        mesh.translate(0.0, 0.5, 0.0)

        chess_king_obj = Object3D()
        chess_king_obj.add(mesh)
        return chess_king_obj
        
        
        
