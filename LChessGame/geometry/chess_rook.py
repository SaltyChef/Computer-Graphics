"""An example of a basic scene: spinning cube"""
from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
import imp
from core_ext.object3d import Object3D
from core.base import Base
from core_ext.mesh import Mesh
from core_ext.texture import Texture
from math import pi
from geometry.cylinder import CylinderGeometry
from geometry.cylindrical import CylindricalGeometry
from geometry.my_cilinder import myCylinderGeometry
from geometry.box import BoxGeometry
from geometry.polygon import PolygonGeometry
from material.surface import SurfaceMaterial
from material.texture import TextureMaterial
from material.lambert import LambertMaterial
class ChessRook(Base):
    def getObject3D(side=0):
        geometry1 = CylinderGeometry(radius=0.2, height=0.2, radial_segments=32, height_segments=20, closed=False)      
        geometry2 = CylinderGeometry(radius=0.1, height=0.4, radial_segments=32, height_segments=20, closed=False)     
        geometry3 = CylindricalGeometry(radius_top=0.1, radius_bottom=0.12, height=0.1, radial_segments=32, height_segments=20, closed_top=False, closed_bottom=False)   
        geometry4 = CylindricalGeometry(radius_top=0.12, radius_bottom=0.15, height=0.055, radial_segments=32, height_segments=20, closed_top=False, closed_bottom=False) 
        geometry5 = CylindricalGeometry(radius_top=0.15, radius_bottom=0.18, height=0.055, radial_segments=32, height_segments=20, closed_top=False, closed_bottom=False) 
        geometry6 = CylindricalGeometry(radius_top=0.18, radius_bottom=0.195, height=0.02, radial_segments=32, height_segments=20, closed_top=False, closed_bottom=False) 
        geometry7 = CylindricalGeometry(radius_top=0.195, radius_bottom=0.215, height=0.04, radial_segments=32, height_segments=20, closed_top=False, closed_bottom=False) 
        geometry8 = CylindricalGeometry(radius_top=0.215, radius_bottom=0.225, height=0.05, radial_segments=32, height_segments=20, closed_top=False, closed_bottom=False)
        geometry9 = CylindricalGeometry(radius_top=0.225, radius_bottom=0.23, height=0.06, radial_segments=32, height_segments=20, closed_top=False, closed_bottom=False) 
        geometry10 = CylinderGeometry(radius=0.23, height=0.15, radial_segments=32, height_segments=20, closed=False)     
        geometry11 = PolygonGeometry(sides=32, radius=0.23)     
        geometry12 = PolygonGeometry(sides=32, radius=0.2)
        geometry13 = PolygonGeometry(sides=32, radius=0.2)
        geometry14 = myCylinderGeometry()
        geometry15 = BoxGeometry(width= 0.01,height = 0.25,depth=0.1 )
        geometry16 = myCylinderGeometry()
        geometry17 = BoxGeometry(width= 0.01,height = 0.25,depth=0.1 )
        geometry18 = myCylinderGeometry()
        geometry19 = BoxGeometry(width= 0.01,height = 0.25,depth=0.1 )
        geometry20 = myCylinderGeometry()
        geometry21 = BoxGeometry(width= 0.01,height = 0.25,depth=0.1 )

        grid_texture = Texture(file_name='images/whiteMarble.jpg')
        if side == 1:
            grid_texture = Texture(file_name='images/blackMarble.jpg')
        
        material = LambertMaterial(texture=grid_texture)
        

        mesh1 = Mesh(geometry1, material)
        mesh1.translate(0.0,0.4,0.0)

        mesh2 = Mesh(geometry2, material)
        mesh2.translate(0.0,0.1,0.0)
        
        mesh3 = Mesh(geometry3, material)
        mesh3.translate(0.0,-0.135,0.0)
       
        mesh4 = Mesh(geometry4, material)
        mesh4.translate(0.0,-0.212,0.0)
        
        mesh5 = Mesh(geometry5, material)
        mesh5.translate(0.0,-0.265,0.0)
        
        mesh6 = Mesh(geometry6, material)
        mesh6.translate(0.0,-0.3,0.0)
        
        mesh7 = Mesh(geometry7, material)
        mesh7.translate(0.0,-0.33,0.0)
       
        mesh8 = Mesh(geometry8, material)
        mesh8.translate(0.0,-0.375,0.0)
       
        mesh9 = Mesh(geometry9, material)
        mesh9.translate(0.0,-0.43,0.0)

        mesh10 = Mesh(geometry10, material)
        mesh10.translate(0.0,-0.532,0.0)

        mesh11 = Mesh(geometry11, material)
        mesh11.translate(0.0,-0.6,0.0)
        mesh11.rotate_x( pi/2 )

        mesh12 = Mesh(geometry12, material)
        mesh12.translate(0.0,0.3,0.0)
        mesh12.rotate_x( pi/2 )

        mesh13 = Mesh(geometry13, material)
        mesh13.translate(0.0,0.5,0.0)
        mesh13.rotate_x( -pi/2 ) 

        mesh14 = Mesh(geometry14, material)
        mesh14.translate(0.15,0.5,0)
        mesh15 = Mesh(geometry15, material)
        mesh15.translate(0.15,0.5,0)

        mesh16 = Mesh(geometry16, material)
        mesh16.translate(-0.15,0.5,0)
        mesh16.rotate_y( pi )
        mesh17 = Mesh(geometry17, material)
        mesh17.translate(-0.15,0.5,0)

        mesh18 = Mesh(geometry18, material)
        mesh18.translate(0,0.5,0.15)
        mesh18.rotate_y( 3*pi/2 )
        mesh19 = Mesh(geometry19, material)
        mesh19.translate(0,0.5,0.15)
        mesh19.rotate_y( pi/2 )

        mesh20 = Mesh(geometry20, material)
        mesh20.translate(0,0.5,-0.15)
        mesh20.rotate_y( pi/2 )
        mesh21 = Mesh(geometry21, material)
        mesh21.translate(0,0.5,-0.15)
        mesh21.rotate_y( pi/2 )


        Chess_Rook = Object3D()
        Chess_Rook.add(mesh1)
        Chess_Rook.add(mesh2)
        Chess_Rook.add(mesh3)
        Chess_Rook.add(mesh4)
        Chess_Rook.add(mesh5)
        Chess_Rook.add(mesh6)
        Chess_Rook.add(mesh7)
        Chess_Rook.add(mesh8)
        Chess_Rook.add(mesh9)
        Chess_Rook.add(mesh10)
        Chess_Rook.add(mesh11)
        Chess_Rook.add(mesh12)
        Chess_Rook.add(mesh13)
        Chess_Rook.add(mesh14)
        Chess_Rook.add(mesh15)
        Chess_Rook.add(mesh16)
        Chess_Rook.add(mesh17)
        Chess_Rook.add(mesh18)
        Chess_Rook.add(mesh19)
        Chess_Rook.add(mesh20)
        Chess_Rook.add(mesh21)
        return Chess_Rook
