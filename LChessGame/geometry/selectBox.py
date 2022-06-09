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



class SelectBox(Base):
    
    
    def getObject3D(side=0):
        

        width = 2
        depth = 2
        height = 0.09

        if(side == 0):
            grid_texture = Texture(file_name='images/wormhole.jpg')
            material = TextureMaterial(texture=grid_texture)
        
        elif(side == 1):
            grid_texture = Texture(file_name='images/green.jpg')
            material = TextureMaterial(texture=grid_texture)
            width = 1
            depth = 1
            height = 0.15

        elif side == 2:
            grid_texture = Texture(file_name='images/red.jpg')
            material = TextureMaterial(texture=grid_texture)

        geometry = BoxGeometry(width=width, height=height, depth=depth)
        mesh = Mesh(geometry, material)


        chess_king_obj = Object3D()
        chess_king_obj.add(mesh)
        chess_king_obj.translate(0,-0.65, 0)
        return chess_king_obj
        
        
