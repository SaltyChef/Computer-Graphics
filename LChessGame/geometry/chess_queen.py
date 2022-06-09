
import OpenGL.GL as GL
from core.base import Base
from geometry.geometry import Geometry
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.object3d import Object3D
from core.base import Base
from core_ext.mesh import Mesh
from core_ext.texture import Texture
from material.texture import TextureMaterial
from core.obj_reader import my_obj_reader
from material.lambert import LambertMaterial
class Geometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('core/chess_queen.obj')
        color_data = [0.58823, 0.294117, 0.0] * len(position_data)
        uv_data = [GL.glGenTextures(1000)] * len(position_data)
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()

        
class ChessQueen(Base):
    def getObject3D(side=0):
        geometry = Geometry()
        grid_texture = Texture(file_name='images/whiteMarble.jpg')
        if side == 1:
            grid_texture = Texture(file_name='images/blackMarble.jpg')
        material = LambertMaterial(texture=grid_texture)
        mesh1 = Mesh(geometry, material)
        mesh1.translate(0.0,0.0,0.0)
        Chess_Queen = Object3D()
        Chess_Queen.add(mesh1)

        return Chess_Queen
