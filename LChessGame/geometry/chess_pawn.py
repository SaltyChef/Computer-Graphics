"""An example of a basic scene: spinning cube"""

import imp
from core_ext.object3d import Object3D
from core.base import Base
from core_ext.mesh import Mesh
from core_ext.texture import Texture


from geometry.cone import ConeGeometry
from geometry.cylinder import CylinderGeometry
from geometry.cylindrical import CylindricalGeometry
from geometry.sphere import SphereGeometry
from geometry.polygon import PolygonGeometry
from material.lambert import LambertMaterial
from material.texture import TextureMaterial
from material.surface import SurfaceMaterial




class ChessPawn(Base):
    def getObject3D(side=0):
        radial_segment = 32
        geometry = SphereGeometry(radius=0.3, radius_segments=radial_segment, height_segments=16)      #nice
        geometry2 = ConeGeometry(radius=0.5, height=0.3, radial_segments=radial_segment, height_segments=16, closed=True)       
        geometry3 = CylinderGeometry(radius=0.2, height=0.40, radial_segments=radial_segment, height_segments=16, closed=False)     
        geometry4 = CylindricalGeometry(radius_top=0.2, radius_bottom=0.24, height=0.1, radial_segments=radial_segment, height_segments=16, closed_top=False, closed_bottom=False)   
        geometry5 = CylindricalGeometry(radius_top=0.24, radius_bottom=0.3, height=0.055, radial_segments=radial_segment, height_segments=16, closed_top=False, closed_bottom=False) 
        geometry6 = CylindricalGeometry(radius_top=0.3, radius_bottom=0.36, height=0.055, radial_segments=radial_segment, height_segments=16, closed_top=False, closed_bottom=False) 
        geometry7 = CylindricalGeometry(radius_top=0.36, radius_bottom=0.39, height=0.02, radial_segments=radial_segment, height_segments=16, closed_top=False, closed_bottom=False) 
        geometry8 = CylindricalGeometry(radius_top=0.39, radius_bottom=0.43, height=0.04, radial_segments=radial_segment, height_segments=16, closed_top=False, closed_bottom=False) 
        geometry9 = CylindricalGeometry(radius_top=0.43, radius_bottom=0.45, height=0.05, radial_segments=radial_segment, height_segments=16, closed_top=False, closed_bottom=False) 
        geometry10 = CylindricalGeometry(radius_top=0.45, radius_bottom=0.46, height=0.06, radial_segments=radial_segment, height_segments=16, closed_top=False, closed_bottom=False)
        geometry11 = CylinderGeometry(radius=0.46, height=0.15, radial_segments=radial_segment, height_segments=16, closed=True)     
      

  
   
        grid_texture = Texture(file_name='images/whiteMarble.jpg')
        if side == 1:
            grid_texture = Texture(file_name='images/blackMarble.jpg')
        
        material = LambertMaterial(texture=grid_texture)




        mesh = Mesh(geometry, material)
        mesh.translate(0.0,0.65,0.0)
        
        
        mesh2 = Mesh(geometry2, material)
        mesh2.translate(0.0,0.41,0.0)
        mesh2.scale(0.7)

        mesh3 = Mesh(geometry3, material)
        mesh3.translate(0.0,0.117,0.0)
        

        mesh4 = Mesh(geometry4, material)
        mesh4.translate(0.0,-0.135,0.0)
       

        mesh5 = Mesh(geometry5, material)
        mesh5.translate(0.0,-0.212,0.0)
        

        mesh6 = Mesh(geometry6, material)
        mesh6.translate(0.0,-0.265,0.0)
        

        mesh7 = Mesh(geometry7, material)
        mesh7.translate(0.0,-0.302,0.0)
        

        mesh8 = Mesh(geometry8, material)
        mesh8.translate(0.0,-0.333,0.0)
       

        mesh9 = Mesh(geometry9, material)
        mesh9.translate(0.0,-0.375,0.0)
       

        mesh10 = Mesh(geometry10, material)
        mesh10.translate(0.0,-0.431,0.0)


        mesh11 = Mesh(geometry11, material)
        mesh11.translate(0.0,-0.532,0.0)

        chess_pawn = Object3D()
        chess_pawn.add(mesh)
        chess_pawn.add(mesh2)
        chess_pawn.add(mesh3)
        chess_pawn.add(mesh4)
        chess_pawn.add(mesh5)
        chess_pawn.add(mesh6)
        chess_pawn.add(mesh7)
        chess_pawn.add(mesh8)
        chess_pawn.add(mesh9)
        chess_pawn.add(mesh10)
        chess_pawn.add(mesh11)
        
        
        return chess_pawn
        
        
