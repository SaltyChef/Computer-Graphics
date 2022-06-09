import OpenGL.GL as GL
from core.matrix import Matrix
from extras.text_texture import TextTexture
from material.texture import TextureMaterial
from geometry.bigsphere import BigSphere
from geometry.rectangle import RectangleGeometry
from math import sin, cos, pi
from time import sleep
from geometry.chess_knight import ChessKnight
from geometry.chess_queen import ChessQueen
from core.base import Base
from core_ext.camera import Camera
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from game_pieces.piece import Piece

from geometry.chess_king import ChessKing
from geometry.board import Board
from geometry.selectBox import SelectBox
from geometry.chess_pawn import ChessPawn
from geometry.chess_rook import ChessRook
from geometry.chess_bishop import ChessBishop
from extras.movement_rig import MovementRig
from core_ext.mesh import Mesh
from light.directional import DirectionalLight
from light.ambient import AmbientLight
from light.point import PointLight



class ChessGame(Base):


    def DefaulStart(self):
        self.boardSize = 8
        self.RA1_start = [-7, 1.25, -7]
        self.KA1_start = [-5, 0.1, -7]
        self.BA1_start = [-3, 1.2, -7]
        self.QA1_start = [-1 ,-0.1 , -7]
        self.KINGA_start = [1 ,1.6 , -7]
        self.BA2_start = [ 3, 1.2, -7]
        self.KA2_start = [5, 0.1, -7]
        self.RA2_start = [7, 1.25, -7]
        self.PA1_start = [-7 , 0.6 , -5]
        self.PA2_start = [-5 , 0.6 , -5]
        self.PA3_start = [-3 , 0.6 , -5]
        self.PA4_start = [-1 , 0.6 , -5]
        self.PA5_start = [1 , 0.6 , -5]
        self.PA6_start = [3 , 0.6 , -5]
        self.PA7_start = [5 , 0.6 , -5]
        self.PA8_start = [7 , 0.6 , -5]


        # setting pieces for player 1
        self.RA1 = Piece(self.RA1_start, ChessRook.getObject3D(0), "RA1", player=1,     ID=4)
        self.KA1 = Piece(self.KA1_start, ChessKnight.getObject3D(0), "KA1", player=1,   ID=3)
        self.BA1 = Piece(self.BA1_start, ChessBishop.getObject3D(0), "BA1", player=1,   ID=2)
        self.QA1 = Piece(self.QA1_start, ChessQueen.getObject3D(0), "QA1", player=1,    ID=5)
        self.KINGA = Piece(self.KINGA_start, ChessKing.getObject3D(0),"KingA", player=1,ID=6)
        self.BA2 = Piece(self.BA2_start, ChessBishop.getObject3D(0),"BA2", player=1,    ID=2)
        self.KA2 = Piece(self.KA2_start, ChessKnight.getObject3D(0), "KA2", player=1,   ID=3)
        self.RA2 = Piece(self.RA2_start, ChessRook.getObject3D(0), "RA2", player=1,     ID=4) 
        self.PA1 = Piece(self.PA1_start, ChessPawn.getObject3D(0), "PA1", player=1,     ID=1)
        self.PA2 = Piece(self.PA2_start, ChessPawn.getObject3D(0), "PA2", player=1,     ID=1)
        self.PA3 = Piece(self.PA3_start, ChessPawn.getObject3D(0), "PA3", player=1,     ID=1)
        self.PA4 = Piece(self.PA4_start, ChessPawn.getObject3D(0), "PA4", player=1,     ID=1)
        self.PA5 = Piece(self.PA5_start, ChessPawn.getObject3D(0), "PA5", player=1,     ID=1)
        self.PA6 = Piece(self.PA6_start, ChessPawn.getObject3D(0), "PA6", player=1,     ID=1)
        self.PA7 = Piece(self.PA7_start, ChessPawn.getObject3D(0), "PA7", player=1,     ID=1)
        self.PA8 = Piece(self.PA8_start, ChessPawn.getObject3D(0), "PA8", player=1,     ID=1) 

        # setting pieces for player 2
    
        self.sbox = SelectBox.getObject3D(0)
        self.sbox.position = [-7 , 0.6 , -5]
        self.sbox.translate(-7 , 0.6 , -5)

        self.bigSphere = BigSphere.getObject3D()
        self.scene.add(self.bigSphere)

        self.pawnA1 = self.PA1.getObject()
        self.pawnA2 = self.PA2.getObject()
        self.pawnA3 = self.PA3.getObject()
        self.pawnA4 = self.PA4.getObject()
        self.pawnA5 = self.PA5.getObject()
        self.pawnA6 = self.PA6.getObject()
        self.pawnA7 = self.PA7.getObject()
        self.pawnA8 = self.PA8.getObject()
        self.kingA = self.KINGA.getObject()
        self.QueenA = self.QA1.getObject()
        self.rookA1 = self.RA1.getObject()
        self.rookA2 = self.RA2.getObject()
        self.bishopA1 = self.BA1.getObject()
        self.bishopA2 = self.BA2.getObject()
        self.knightA1 = self.KA1.getObject()
        self.knightA2 = self.KA2.getObject()  

        self.knightA1.rotate_y(-pi/2)
        self.knightA2.rotate_y(-pi/2)

        self.knightA1.scale(5)
        self.knightA2.scale(5)
        self.bishopA2.scale(0.27)
        self.bishopA1.scale(0.27)
        self.rookA1.scale(2)
        self.rookA2.scale(2)
        self.QueenA.scale(4)    

        #self.scene.add(self.goldenSphere)
        self.scene.add(self.pawnA1)
        self.scene.add(self.pawnA2)
        self.scene.add(self.pawnA3)
        self.scene.add(self.pawnA4)
        self.scene.add(self.pawnA5)
        self.scene.add(self.pawnA6)
        self.scene.add(self.pawnA7)
        self.scene.add(self.pawnA8)
        self.scene.add(self.rookA1)
        self.scene.add(self.knightA1)
        self.scene.add(self.bishopA1)
        self.scene.add(self.QueenA)
        self.scene.add(self.kingA)
        self.scene.add(self.bishopA2)
        self.scene.add(self.knightA2)
        self.scene.add(self.rookA2)
        
        # Other side 

        self.KINGB_start = [1 ,1.6 , 7]
        self.QB1_start = [-1 ,-0.1 , 7]
        self.RB1_start = [-7, 1.25, 7]
        self.RB2_start = [7, 1.25, 7]
        self.BB1_start = [-3, 1.2, 7]
        self.BB2_start = [3, 1.2, 7]
        self.KB1_start = [-5, 0.1, 7]
        self.KB2_start = [5, 0.1, 7]
        self.PB1_start = [-7 , 0.6 , 5]
        self.PB2_start = [-5 , 0.6 , 5]
        self.PB3_start = [-3 , 0.6 , 5]
        self.PB4_start = [-1 , 0.6 , 5]
        self.PB5_start = [1 , 0.6 , 5]
        self.PB6_start = [3 , 0.6 , 5]
        self.PB7_start = [5 , 0.6 , 5]
        self.PB8_start = [7 , 0.6 , 5]


        # ID's 
        # 1 = pawn
        # 2 = bishop
        # 3 = Kinght
        # 4 = Rook
        # 5 = Queen
        # 6 = King
        self.PB1 = Piece(self.PB1_start, ChessPawn.getObject3D(1), "PB1", player=2, ID=1)
        self.PB2 = Piece(self.PB2_start, ChessPawn.getObject3D(1), "PB2", player=2, ID=1)
        self.PB3 = Piece(self.PB3_start, ChessPawn.getObject3D(1), "PB3", player=2, ID=1)
        self.PB4 = Piece(self.PB4_start, ChessPawn.getObject3D(1), "PB4", player=2, ID=1)
        self.PB5 = Piece(self.PB5_start, ChessPawn.getObject3D(1), "PB5", player=2, ID=1)
        self.PB6 = Piece(self.PB6_start, ChessPawn.getObject3D(1), "PB6", player=2, ID=1)
        self.PB7 = Piece(self.PB7_start, ChessPawn.getObject3D(1), "PB7", player=2, ID=1)
        self.PB8 = Piece(self.PB8_start, ChessPawn.getObject3D(1), "PB8", player=2, ID=1)

        self.RB1 = Piece(self.RB1_start, ChessRook.getObject3D(1), "RB1", player=2,           ID=4)
        self.KB1 = Piece(self.KB1_start, ChessKnight.getObject3D(1), "KB1", player=2,       ID=3)
        self.BB1 = Piece(self.BB1_start, ChessBishop.getObject3D(1), "BB1", player=2,       ID=2)
        self.QB1 = Piece(self.QB1_start, ChessQueen.getObject3D(1), "QB1", player=2,         ID=5)
        self.KINGB = Piece(self.KINGB_start, ChessKing.getObject3D(1),"KINGB", player=2,      ID=6)
        self.BB2 = Piece(self.BB2_start, ChessBishop.getObject3D(1),"BB2", player=2,        ID=2)
        self.KB2 = Piece(self.KB2_start, ChessKnight.getObject3D(1), "KB2", player=2,       ID=3)
        self.RB2 = Piece(self.RB2_start, ChessRook.getObject3D(1), "RB2", player=2,           ID=4) 


        
        self.pawnB1 = self.PB1.getObject()
        self.pawnB2 = self.PB2.getObject()
        self.pawnB3 = self.PB3.getObject()
        self.pawnB4 = self.PB4.getObject()
        self.pawnB5 = self.PB5.getObject()
        self.pawnB6 = self.PB6.getObject()
        self.pawnB7 = self.PB7.getObject()
        self.pawnB8 = self.PB8.getObject()
    
    
        self.kingB = self.KINGB.getObject()
        self.QueenB = self.QB1.getObject()
        self.rookB1 = self.RB1.getObject()
        self.rookB2 = self.RB2.getObject()
        self.bishopB1 = self.BB1.getObject()
        self.bishopB2 = self.BB2.getObject()
        self.knightB1 = self.KB1.getObject()
        self.knightB2 = self.KB2.getObject()  
        self.knightB1.rotate_y(pi/2)
        self.knightB2.rotate_y(pi/2)
       
        self.bishopB1.scale(0.27)
        self.bishopB2.scale(0.27)
        self.QueenB.scale(4)
        self.rookB1.scale(2)
        self.rookB2.scale(2)
        self.knightB1.scale(5)
        self.knightB2.scale(5)

 

        self.scene.add(self.knightB1)
        self.scene.add(self.knightB2)
        self.scene.add(self.pawnB1)
        self.scene.add(self.pawnB2)
        self.scene.add(self.pawnB3)
        self.scene.add(self.pawnB4)
        self.scene.add(self.pawnB5)
        self.scene.add(self.pawnB6)
        self.scene.add(self.pawnB7)
        self.scene.add(self.pawnB8)
        self.scene.add(self.rookB1)
        self.scene.add(self.rookB2)
        self.scene.add(self.bishopB1)
        self.scene.add(self.bishopB2)
        self.scene.add(self.kingB)
        self.scene.add(self.QueenB)




        e = Piece(coordenates=[-7, 0, 3], isEmpty=True)
        e1 = Piece(coordenates=[-5, 0, 3], isEmpty=True)
        e2 = Piece(coordenates=[-3, 0, 3], isEmpty=True)
        e3 = Piece(coordenates=[-1, 0, 3], isEmpty=True)
        e4 = Piece(coordenates=[1, 0, 3], isEmpty=True)
        e5 = Piece(coordenates=[3, 0, 3], isEmpty=True)
        e6 = Piece(coordenates=[5, 0, 3], isEmpty=True)
        e7 = Piece(coordenates=[7, 0, 3], isEmpty=True)    
        
        e8 = Piece(coordenates=[-7, 0, 1], isEmpty=True)
        e9 = Piece(coordenates=[-5, 0, 1], isEmpty=True)
        e10 = Piece(coordenates=[-3, 0, 1], isEmpty=True)
        e11 = Piece(coordenates=[-1, 0, 1], isEmpty=True)
        e12 = Piece(coordenates=[1, 0, 1], isEmpty=True)
        e13 = Piece(coordenates=[3, 0, 1], isEmpty=True)
        e14 = Piece(coordenates=[5, 0, 1], isEmpty=True)
        e15 = Piece(coordenates=[7, 0, 1], isEmpty=True)    

        e16 = Piece(coordenates=[-7, 0, -1], isEmpty=True)
        e17 = Piece(coordenates=[-5, 0, -1], isEmpty=True)
        e18 = Piece(coordenates=[-3, 0, -1], isEmpty=True)
        e19 = Piece(coordenates=[-1, 0, -1], isEmpty=True)
        e20 = Piece(coordenates=[1, 0, -1], isEmpty=True)
        e21 = Piece(coordenates=[3, 0, -1], isEmpty=True)
        e22 = Piece(coordenates=[5, 0, -1], isEmpty=True)
        e23 = Piece(coordenates=[7, 0, -1], isEmpty=True)    
        
        e24 = Piece(coordenates=[-7, 0, -3], isEmpty=True)
        e25 = Piece(coordenates=[-5, 0, -3], isEmpty=True)
        e26 = Piece(coordenates=[-3, 0, -3], isEmpty=True)
        e27 = Piece(coordenates=[-1, 0, -3], isEmpty=True)
        e28 = Piece(coordenates=[1, 0, -3], isEmpty=True)
        e29 = Piece(coordenates=[3, 0, -3], isEmpty=True)
        e30 = Piece(coordenates=[5, 0, -3], isEmpty=True)
        e31 = Piece(coordenates=[7, 0, -3], isEmpty=True)    


        self.boardMatrix = [ [self.RA1, self.KA1, self.BA1, self.QA1, self.KINGA, self.BA2, self.KA2, self.RA2 ],
                             [self.PA1, self.PA2, self.PA3, self.PA4, self.PA5,   self.PA6, self.PA7, self.PA8 ],
                             [e, e1, e2, e3, e4, e5, e6, e7],
                             [e8, e9, e10, e11, e12, e13, e14, e15],
                             [e16, e17, e18, e19, e20, e21, e22, e23],
                             [e24, e25, e26, e27, e28, e29, e30, e31],
                             [self.PB1, self.PB2, self.PB3, self.PB4, self.PB5, self.PB6, self.PB7, self.PB8],
                             [self.RB1, self.KB1, self.BB1, self.QB1, self.KINGB, self.BB2, self.KB2, self.RB2 ]]

        return
        


    def moveSelectBox(self):
        
        x = self.sbox.global_position[0]
        z = self.sbox.global_position[2]

        #for camera 1
        if self.currentCameraPos == '1' :
            if self.input.is_key_down('right') and x < self.boardLimit:
                self.sbox.translate(2, 0, 0)
            if self.input.is_key_down('up') and z > -self.boardLimit:
                self.sbox.translate(0, 0, -2)
            if self.input.is_key_down('left') and x > -self.boardLimit:
                self.sbox.translate(-2, 0, 0)
            if self.input.is_key_down('down') and z < self.boardLimit:
                self.sbox.translate(0, 0 , 2)
        
        if self.currentCameraPos == '2':
            if self.input.is_key_down('right') and x > -self.boardLimit:
                self.sbox.translate(-2, 0, 0)
            if self.input.is_key_down('up') and z < self.boardLimit:
                self.sbox.translate(0, 0, 2)
            if self.input.is_key_down('left') and x < self.boardLimit:
                self.sbox.translate(2, 0, 0)
            if self.input.is_key_down('down') and z > -self.boardLimit:
                self.sbox.translate(0, 0 , -2)
        
        if self.currentCameraPos == '3':
            if self.input.is_key_down('right') and z > -self.boardLimit:
                self.sbox.translate(0, 0, -2)
            if self.input.is_key_down('up') and x > -self.boardLimit:
                self.sbox.translate(-2, 0, 0)
            if self.input.is_key_down('left') and z < self.boardLimit:
                self.sbox.translate(0, 0, 2)
            if self.input.is_key_down('down') and x < self.boardLimit:
                self.sbox.translate(2, 0, 0)
        
        if self.currentCameraPos == '4' or self.currentCameraPos == '5':
            if self.input.is_key_down('right') and z < self.boardLimit:
                self.sbox.translate(0, 0, 2) 
            if self.input.is_key_down('up')  and x < self.boardLimit:
                self.sbox.translate(2, 0, 0)
            if self.input.is_key_down('left') and z > -self.boardLimit:
                self.sbox.translate(0, 0, -2)
            if self.input.is_key_down('down') and x > -self.boardLimit:
                self.sbox.translate(-2, 0, 0)

        self.currentKey = "arrow"
        self.lastKey = "arrow"
        return 
        

    

    def changeCameraPos(self):
        if self.input.is_key_pressed('1'):
            self.camera.set_position(self.cameraPosStart1)
            self.camera.look_at(self.centerOfBoard)
            self.currentCameraPos = '1'
            self.rig.set_position(self.centerOfBoard)
    
        if self.input.is_key_pressed('2'):
            self.camera.set_position(self.cameraPosStart2)
            self.camera.look_at(self.centerOfBoard)
            self.currentCameraPos = '2'
            self.rig.set_position(self.centerOfBoard)
    
        if self.input.is_key_pressed('3'):
            self.camera.set_position(self.cameraPosStart3)
            self.camera.look_at(self.centerOfBoard)
            self.currentCameraPos = '3'
            self.rig.set_position(self.centerOfBoard)
    
        if self.input.is_key_pressed('4'):
            self.camera.set_position(self.cameraPosStart4)
            self.camera.look_at(self.centerOfBoard)
            self.currentCameraPos = '4'
            self.rig.set_position(self.centerOfBoard)
    
        if self.input.is_key_pressed('5'):
            self.camera.set_position(self.cameraPosStart5)
            self.camera.look_at(self.centerOfBoard)
            self.currentCameraPos = '5'
            self.rig.set_position(self.centerOfBoard)

    

    def changeBoxForPlayer(self):
        if self.input.is_key_pressed('1'):
            self.currentPlayer = '1'
            self.sbox.position = self.startPosBoxPlayer1
        if self.input.is_key_pressed('2'):
            self.sbox.position = self.startPosBoxPlayer2
            self.currentPlayer = '2'



    

    def cleanPathList(self):
        for i in range(len(self.listPathBox)):
             self.scene._children_list.pop()
        self.listPathBox.clear()


    def isInsideBoard(self, coord):
        if coord[2] >= -self.boardLimit and coord[0] >= -self.boardLimit and coord[2] <= self.boardLimit and coord[0] <= self.boardLimit:
            return True
        return False



    def checkEnemy(self, CheckCoord):
        y = self.sbox.global_position[1]

        piece = self.getPiece(CheckCoord)

        if not self.isInsideBoard(CheckCoord):
            return False
        if piece.player != self.currentPlayer and piece.isEmpty == False:
            pathBox1 = SelectBox.getObject3D(2)
            pathBox1.set_position([CheckCoord[0], y , CheckCoord[2]])
            self.listPathBox.append(pathBox1)
            self.scene.add(pathBox1)
            return False

        return False    

    def checkCreatePath(self, CheckCoord):
        y = self.sbox.global_position[1]
        
        if not self.isInsideBoard(CheckCoord):
            return False
        
        if self.getPiece(CheckCoord).name == "empty":
                pathBox1 = SelectBox.getObject3D(1)
                pathBox1.set_position([CheckCoord[0], y , CheckCoord[2]])
                self.listPathBox.append(pathBox1)
                self.scene.add(pathBox1)
                return True
        
        return self.checkEnemy(CheckCoord)



    def printPath(self, currentPiece):
        coordenates = currentPiece.coordenates
        y = self.sbox.global_position[1]
        # Pawn
        if currentPiece.ID == 1:
            if self.currentPlayer == 2:
                if self.getPiece([coordenates[0], y , coordenates[2]-2]).name == "empty":
                    pathBox1 = SelectBox.getObject3D(1)
                    pathBox1.set_position([coordenates[0], y , coordenates[2]-2])
                    self.listPathBox.append(pathBox1)
                    self.scene.add(pathBox1)
                    
                    if (currentPiece.isFirstMove):
                        if self.getPiece([coordenates[0], y , coordenates[2]-4]).name == "empty":
                            pathBox1 = SelectBox.getObject3D(1)
                            pathBox1.set_position([coordenates[0], y , coordenates[2]-4])
                            self.listPathBox.append(pathBox1)
                            self.scene.add(pathBox1)

                self.checkEnemy([coordenates[0]-2, y , coordenates[2]-2])
                self.checkEnemy([coordenates[0]+2, y , coordenates[2]-2])
            

            elif self.currentPlayer == 1:
                
                if self.getPiece([coordenates[0], y , coordenates[2]+2]).name == "empty":
                        pathBox1 = SelectBox.getObject3D(1)
                        pathBox1.set_position([coordenates[0], y , coordenates[2]+2])
                        self.listPathBox.append(pathBox1)
                        self.scene.add(pathBox1)

                        if (currentPiece.isFirstMove):
                            if self.getPiece([coordenates[0], y , coordenates[2]+4]).name == "empty":
                                pathBox1 = SelectBox.getObject3D(1)
                                pathBox1.set_position([coordenates[0], y , coordenates[2]+4])
                                self.listPathBox.append(pathBox1)
                                self.scene.add(pathBox1)

                self.checkEnemy([coordenates[0]+2, y , coordenates[2]+2])
                self.checkEnemy([coordenates[0]-2, y , coordenates[2]+2])  
        # Bishop
        if currentPiece.ID == 2:
            c = [coordenates[0]+2, y, coordenates[2]+2]
            while self.checkCreatePath(c):
               c = [c[0]+2, y, c[2]+2]

            c = [coordenates[0]-2, y, coordenates[2]+2]
            while self.checkCreatePath(c):
               c = [c[0]-2, y, c[2]+2]

            c = [coordenates[0]+2, y, coordenates[2]-2]
            while self.checkCreatePath(c):
               c = [c[0]+2, y, c[2]-2]

            c = [coordenates[0]-2, y, coordenates[2]-2]
            while self.checkCreatePath(c):
               c = [c[0]-2, y, c[2]-2]

        # Knight 
        if currentPiece.ID == 3:
            self.checkCreatePath([coordenates[0]-4, y, coordenates[2]-2])
            self.checkCreatePath([coordenates[0]-2, y, coordenates[2]-4])
            self.checkCreatePath([coordenates[0]+2, y, coordenates[2]-4])
            self.checkCreatePath([coordenates[0]+4, y, coordenates[2]-2])
            self.checkCreatePath([coordenates[0]+4, y, coordenates[2]+2])
            self.checkCreatePath([coordenates[0]+2, y, coordenates[2]+4])
            self.checkCreatePath([coordenates[0]-2, y, coordenates[2]+4])
            self.checkCreatePath([coordenates[0]-4, y, coordenates[2]+2])

        # Rook 
        if currentPiece.ID == 4:
            i = 2
            while self.checkCreatePath([coordenates[0], y, coordenates[2]-i]):
                i += 2
            i = 2
            while self.checkCreatePath([coordenates[0], y, coordenates[2]+i]):
                i += 2
            i = 2
            while self.checkCreatePath([coordenates[0]-i, y, coordenates[2]]):
                i += 2
            i = 2
            while self.checkCreatePath([coordenates[0]+i, y, coordenates[2]]):
                i += 2

        # Queen 
        if currentPiece.ID == 5:
            c = [coordenates[0]+2, y, coordenates[2]+2]
            while self.checkCreatePath(c):
               c = [c[0]+2, y, c[2]+2]

            c = [coordenates[0]-2, y, coordenates[2]+2]
            while self.checkCreatePath(c):
               c = [c[0]-2, y, c[2]+2]

            c = [coordenates[0]+2, y, coordenates[2]-2]
            while self.checkCreatePath(c):
               c = [c[0]+2, y, c[2]-2]

            c = [coordenates[0]-2, y, coordenates[2]-2]
            while self.checkCreatePath(c):
               c = [c[0]-2, y, c[2]-2]

            i = 2
            while self.checkCreatePath([coordenates[0], y, coordenates[2]-i]):
                i += 2
            i = 2
            while self.checkCreatePath([coordenates[0], y, coordenates[2]+i]):
                i += 2
            i = 2
            while self.checkCreatePath([coordenates[0]-i, y, coordenates[2]]):
                i += 2
            i = 2
            while self.checkCreatePath([coordenates[0]+i, y, coordenates[2]]):
                i += 2

        # KIng
        if currentPiece.ID == 6:
            self.checkCreatePath([coordenates[0], y , coordenates[2]-2])
            self.checkCreatePath([coordenates[0], y , coordenates[2]+2])
            self.checkCreatePath([coordenates[0]-2, y , coordenates[2]])
            self.checkCreatePath([coordenates[0]+2, y , coordenates[2]])   
            self.checkCreatePath([coordenates[0]+2, y , coordenates[2]+2])   
            self.checkCreatePath([coordenates[0]+2, y , coordenates[2]-2])
            self.checkCreatePath([coordenates[0]-2, y , coordenates[2]+2])   
            self.checkCreatePath([coordenates[0]-2, y , coordenates[2]-2])      
             
            return
                
                
    def selectPiece(self, selectedCoord, currentPlayer):
      
        piece = self.getPiece(selectedCoord)
        coordenates = piece.coordenates
                
        #Checking if exist a piece where the user selected and its not empty
        # currentPiece.name != "empty") and 
        if (selectedCoord[0] == coordenates[0]) and (selectedCoord[2] == coordenates[2]) : 
            print(piece.name, piece.ID, piece.coordenates, piece.isFirstMove)
            if currentPlayer == piece.player:
                self.currentPiece = piece
                
                self.LastPieceAnimatedCoord =  piece.coordenates
                self.LastPiece = piece

                

                self.printPath(piece)
            else:
                print("Cannot select this piece")

        return 


    def checkIfIsInPath(self, to):
        for i in range(len(self.listPathBox)):
            box = self.listPathBox[i]   # is a object3D()
            coord = box.global_position
            x = coord[0]
            z = coord[2]
            if x == to[0] and z == to[2]:
                self.currentPiece.isFirstMove = False
                self.currentPiece = self.getPiece(to)
                return True
        return False



    def getPiece(self, coord):
        for i in range(len(self.boardMatrix)):
            for j in range(len(self.boardMatrix[0])):
                piece = self.boardMatrix[i][j]
                c = piece.coordenates
                
                #Checking if exist a piece where the user selected and its not empty
                if (coord[0] == c[0]) and (coord[2] == c[2]) : 
                    return piece
        
    def getMatrixIndex(self, coord):
        for i in range(len(self.boardMatrix)):
            for j in range(len(self.boardMatrix[0])):
                currentPiece = self.boardMatrix[i][j]
                coordenates = currentPiece.coordenates
                
                #Checking if exist a piece where the user selected and its not empty
                if (coord[0] == coordenates[0]) and (coord[2] == coordenates[2]) : 
                    return i, j


    def changePieces(self, p1_coord, p2_coord):
        print("to: " , p2_coord)
        p1 = self.getPiece(p1_coord)
        p2 = self.getPiece(p2_coord)
        
        if(p2.isEmpty):     # MUDAR O EMPTY QUANDO FOR PARA COMER AS PEçAS
            if self.checkIfIsInPath(p2_coord):
                p1.move(p1_coord, p2_coord, self.time, p1.ID)
                p2.move(p2_coord, p1_coord, self.time, p2.ID)
                self.cleanPathList()
            else:
                return
        elif not self.checkIfIsInPath(p2_coord):
            return
        elif p1.player == p2.player:
            return


        p1_index = self.getMatrixIndex(p1_coord)
        p2_index = self.getMatrixIndex(p2_coord)
        
        # kill
        if p1.isEmpty == False and p2.isEmpty == False and p1.player != p2.player: 
            self.boardMatrix[p2_index[0]][p2_index[1]] = self.boardMatrix[p1_index[0]][p1_index[1]]
            p1.move(p1_coord, p2_coord, self.time, p1.ID) 
            self.boardMatrix[p2_index[0]][p2_index[1]] = Piece(p1_coord, name="empty", isEmpty=True)
            self.addDead(p2.player, p2)
        
        else :
            swap = self.boardMatrix[p1_index[0]][p1_index[1]]
            self.boardMatrix[p1_index[0]][p1_index[1]] = self.boardMatrix[p2_index[0]][p2_index[1]]
            self.boardMatrix[p2_index[0]][p2_index[1]] = swap
        

        if self.currentPlayer == 2:
            sleep(1)
            self.currentPlayer = 1
            if not (self.currentCameraPos == '3' or self.currentCameraPos == '4' or self.currentCameraPos == '5'):
                self.camera.set_position(self.cameraPosStart2)
                self.camera.look_at(self.centerOfBoard)
                self.currentCameraPos = '2'
        
        elif self.currentPlayer == 1:
            sleep(1)
            self.currentPlayer = 2
            if not (self.currentCameraPos == '3' or self.currentCameraPos == '4' or self.currentCameraPos == '5'):
                self.camera.set_position(self.cameraPosStart1)
                self.camera.look_at(self.centerOfBoard)
                self.currentCameraPos = '1'



    def addDead(self, deadPlayer, piece):
            y = piece.obj.global_position[1]
            if deadPlayer == 2:
                x = self.listDead2_lastPosition[0]
                z = self.listDead2_lastPosition[2] - 1.5
                self.listDead2.append(piece)
                self.listDead2_lastPosition = [x, y, z]
                piece.obj.set_position(self.listDead2_lastPosition)

            if deadPlayer == 1:
                x = self.listDead1_lastPosition[0]
                z = self.listDead1_lastPosition[2] + 1.5
                self.listDead1.append(piece)
                self.listDead1_lastPosition = [x, y, z]
                piece.obj.set_position(self.listDead1_lastPosition)

    #  ============================  INITIALIZE ================================ 
    def initialize(self):
        self.centerOfBoard = [0, 0, 0]
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.listPathBox = []


        self.listDead1 = []
        self.listDead2 = []
        
        self.listDead1_lastPosition = [-9, 0, -7]
        self.listDead2_lastPosition = [9, 0, 7]

        self.cameraPosStart1 = [0, 10, 15]
        self.cameraPosStart2 = [0, 10, -15]
        self.cameraPosStart3 = [15, 10, 0]
        self.cameraPosStart4 = [-15, 10, 0]
        self.cameraPosStart5 = [0, 18, 0]
        self.selectPosition = [0,0,0]

        self.boardLimit = 7.0

        self.currentCameraPos = '2'
        self.currentPlayer = 1
        self.startPosBoxPlayer1 = [7 , 0.2 , -5]
        self.startPosBoxPlayer2 = [7 , 0.2 , -5]
        self.camera.set_position(self.cameraPosStart2)
        self.camera.look_at(self.centerOfBoard)

        
        self.rig = MovementRig()
        self.rig.set_position(self.centerOfBoard)
        self.scene.add(self.rig)

    
        
        ambient = AmbientLight(color=[0.8, 0.8, 0.8])
        self.scene.add(ambient)

        directional = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-2, 0, -2])
        self.scene.add(directional)
        
        point = PointLight(color=[0.5, 0.5, 0.5], position=[9, 10, 9])
        self.scene.add(point)





        self.board = Board.getObject3D()
        self.scene.add(self.board)

        self.DefaulStart()
        self.scene.add(self.sbox)
        self.lastKey = ""
        self.currentPiece = Piece(coordenates=[0, 0, 0], isEmpty=True)
        self.currentPieceCoord = self.currentPiece.coordenates



        self.LastPiece = Piece(coordenates=[0, 0, 0], isEmpty=True)
        self.LastPieceAnimatedCoord =  [0, 0, 0]

    #  ============================  UPDATE ================================ 
    
    def createBoard(self, txt, pos, font_size):
        label_texture = TextTexture(text=txt,
                                    system_font_name="Arial Bold",
                                    font_size=font_size, font_color=[0, 0, 200],
                                    image_width=256, image_height=128,
                                    align_horizontal=0.5, align_vertical=0.5,
                                    image_border_width=4,
                                    image_border_color=[255, 0, 0])

        self.label_material = TextureMaterial(label_texture)
        self.label_geometry = RectangleGeometry(width=10, height=5)
        self.label_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.label = Mesh(self.label_geometry, self.label_material)
        self.label.set_position(pos)
   
        self.scene.add(self.label)

    

    def checkMate(self):
        pos = [0, 5,0]

        for i in range(len(self.listDead1)):
            piece = self.listDead1[i]
            if piece.ID == 6 and self.currentPlayer == 1:
                self.camera.set_position(self.cameraPosStart4)
                self.camera.look_at(pos)
                self.createBoard("Player 2 Wins!", pos, 40)
                return True

        for i in range(len(self.listDead2)):
            piece = self.listDead2[i]
            if piece.ID == 6 and self.currentPlayer == 2:
                self.camera.set_position(self.cameraPosStart4)
                self.camera.look_at(pos)
                self.createBoard("Player 1 Wins!", pos, 40)
                return True
        

        return False


    def update(self):
        GL.glClearColor(0.5, 0.5, 0.5, 1)
                
        self.changeCameraPos()
        self.moveSelectBox()
        self.bigSphere.rotate_y(0.001)

       


        #select the piece
        if self.input.is_key_pressed('return') and self.lastKey != "return":
            
            self.cleanPathList()
            self.currentKey == "arrow"
            self.selectPiece(self.sbox.global_position , self.currentPlayer)
            
            if self.LastPiece.coordenates != self.currentPiece.coordenates:
                if self.currentPiece.ID == 5:
                    self.currentPiece.obj.translate(0, 0.05, 0)
                if self.currentPiece.ID == 3:
                    self.currentPiece.obj.translate(0, 0.09, 0)

            self.lastKey = "return"
        
        if self.currentKey == 'arrow' and self.lastKey != "return":
            x = self.LastPieceAnimatedCoord[0]
            y = self.LastPieceAnimatedCoord[1]
            z = self.LastPieceAnimatedCoord[2]
            self.LastPiece.obj.set_position([x, y, z])    

        #unselect the piece
        if self.input.is_key_pressed('escape') and self.lastKey != "escape":
            self.lastKey = "escape"
            self.lastPiece = self.currentPiece 
            self.currentPiece = Piece(coordenates=[0, 0, 0], isEmpty=True)
            if self.lastKey != "space":
                x = self.LastPieceAnimatedCoord[0]
                y = self.LastPieceAnimatedCoord[1]
                z = self.LastPieceAnimatedCoord[2]
                self.LastPiece.obj.set_position([x, y, z])    

            self.cleanPathList()

        #make move
        if self.input.is_key_pressed('space') and self.lastKey != "space":
            self.lastKey = "space"
        
            to = self.sbox.global_position
            to[1] = self.currentPiece.coordenates[1]
            if to != self.currentPiece.coordenates:
                self.changePieces(self.currentPiece.coordenates, to)
                self.cleanPathList()
                self.LastPiece = Piece(coordenates=[0, 0, 0], isEmpty=True)
                
            
        
        if self.checkMate():
            self.label.look_at(self.camera.global_position)
            if self.input.is_key_pressed('r') and self.lastKey != 'r':
                self.lastKey == "r"
                self.DefaulStart()
                self.initialize()


 
        if self.currentPiece.isEmpty == False:

            if self.currentPiece.ID == 5:
                self.currentPiece.obj.translate(0.0, -cos(self.time* pi)/120, 0.0)
            elif self.currentPiece.ID == 3:
                self.currentPiece.obj.translate(0.0, -cos(self.time* pi)/120, 0.0)
            elif self.currentPiece.ID == 2:
                self.currentPiece.obj.translate(0.0, -cos(self.time* pi)/5, 0.0)
            else:
                self.currentPiece.obj.translate(0.0, -cos(self.time* pi)/60, 0.0)
            


        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)
            

# Instantiate this class and run the program
ChessGame(screen_size=[1024, 1024]).run()