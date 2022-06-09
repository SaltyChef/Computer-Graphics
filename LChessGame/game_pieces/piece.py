from xml.etree.ElementPath import xpath_tokenizer
from core.base import Base
from core_ext.object3d import Object3D

   # ID's 
        # 1 = pawn
        # 2 = bishop
        # 3 = Kinght
        # 4 = Rook
        # 5 = Queen
        # 6 = King
class Piece():
    def __init__(self, coordenates, obj=Object3D(), name="empty", isEmpty=False, 
                        isFirstMove=True, player=1, ID=-1):
        self.coordenates = coordenates
        self.obj = obj
        self.name = name
        self.isEmpty = isEmpty
        self.isFirstMove = isFirstMove
        self.obj.set_position(self.coordenates)
        self.player = player
        self.ID = ID



    def getObject(self):
        return self.obj

    def move(self, from_, to, time, id):
        x_from = from_[0]
        z_from = from_[2]
        y = from_[1]

        countX = 0
        countZ = 0
        x_atual = x_from
        z_atual = z_from

        x_to = to[0]
        z_to = to[2]


        x_dist = x_atual - x_to
        z_dist = z_atual - z_to
        while(countX < 10000 and countZ < 10000):
            
            # x_to > x_atual
            if x_dist < 0:
                x_atual += 0.0001
                countX +=1
            elif x_dist > 0:
                x_atual -= 0.0001
                countX +=1

            if z_dist < 0:
                z_atual += 0.0001
                countZ +=1

            elif z_dist > 0:
                z_atual -= 0.0001
                countZ +=1


            x_dist = x_atual - x_to
            z_dist = z_atual - z_to

            self.obj.set_position([x_atual, y, z_atual])


        self.coordenates = to
        self.obj.set_position(to)
