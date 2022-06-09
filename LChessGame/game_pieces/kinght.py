from game_pieces.piece import Piece
from core_ext.object3d import Object3D

class Kinght(Piece):
    def __init__(self, coordenates=[0,0,0], obj=Object3D(), name="", player=1):
        super().__init__(coordenates=coordenates, obj=obj, name=name, 
                        isEmpty=False, player=player)
        
