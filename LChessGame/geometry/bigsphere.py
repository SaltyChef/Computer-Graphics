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




class BigSphere(Base):
    def getObject3D():
        geometry = SphereGeometry( radius=30, radius_segments=64, height_segments=64)      #nice

  
   
        grid_texture = Texture(file_name='images/fundo2.png')
        
        material = LambertMaterial(texture=grid_texture)


        mesh = Mesh(geometry, material)
        mesh.set_position([0,0,0])
        
        sphere = Object3D()
        sphere.add(mesh)
        
        
        return sphere
        
        
