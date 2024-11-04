from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer, Signal, QObject, Qt
import numpy as np
from numpy.linalg import norm
from math import cos, sin, atan2, sqrt, pi, radians
import pandas as pd
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtGui
from pyqtgraph.opengl import GLViewWidget
from functions.unidad_1 import crearCuaternio,conjCuaternio,proCuaternios, D_H

class Rejilla():
    def __init__(self,xMin:float,xMax:float,yMin:float,yMax:float,zMin:float,zMax:float,espaciado:float) -> None:
        fontSize = 11
        fuente = 'Helvetica'
        colorRejillas = [50,50,50]
        colorTexto = [150,150,150]
        
        spacing = QtGui.QVector3D(espaciado,espaciado,espaciado)
        
        tamanioX = xMax-xMin
        tamanioY = yMax-yMin
        tamanioZ = zMax-zMin
        
        sizeX = QtGui.QVector3D(tamanioZ,tamanioY,1)
        sizeY = QtGui.QVector3D(tamanioX,tamanioZ,1)
        sizeZ = QtGui.QVector3D(tamanioX,tamanioY,1)
        
        trasladoX = xMin + (tamanioX/2)
        trasladoY = yMin + (tamanioY/2)
        trasladoZ = zMin + (tamanioZ/2)
        
        # Se crean las rejillas
        gx = gl.GLGridItem()
        gx.setSize(size=sizeX)
        gx.setSpacing(spacing=spacing)
        gx.rotate(-90, 0, 1, 0)
        gx.translate(xMin, trasladoY, trasladoZ)
        gx.setColor(colorRejillas)
        
        gy = gl.GLGridItem()
        gy.setSize(size=sizeY)
        gy.setSpacing(spacing=spacing)
        gy.rotate(90, 1, 0, 0)
        gy.translate(trasladoX, yMin, trasladoZ)
        gy.setColor(colorRejillas)
        
        gz = gl.GLGridItem()
        gz.setSize(size=sizeZ)
        gz.setSpacing(spacing=spacing)
        gz.translate(trasladoX, trasladoY, zMin)
        gz.setColor(colorRejillas)
        
        self.rejillas = [gx,gy,gz]
        
        rangoX = np.arange(xMin, xMax+espaciado, espaciado)
        if rangoX[-1] > xMax:
            rangoX = np.delete(rangoX, -1)
            
        rangoY = np.arange(yMin, yMax+espaciado, espaciado)
        if rangoY[-1] > yMax:
            rangoY = np.delete(rangoY, -1)
            
        rangoZ = np.arange(zMin, zMax+espaciado, espaciado)
        if rangoZ[-1] > zMax:
            rangoZ = np.delete(rangoZ, -1)
            
            
        # Se crean las numeraciones de los ejes
        espacioExtraY = tamanioY/25
        espacioExtraX = tamanioX/25
        self.textos = []
        for ix in rangoX:
            pos = (ix,yMax+espacioExtraY,zMin)
            lx = gl.GLTextItem(pos=pos, color=colorTexto, text=str(ix), font=QFont(fuente, fontSize))
            self.textos.append(lx)
            
        for iy in rangoY:
            pos = (xMax+espacioExtraX,iy,zMin)
            ly = gl.GLTextItem(pos=pos, color=colorTexto, text=str(iy), font=QFont(fuente, fontSize))
            self.textos.append(ly)
            
        for iz in rangoZ:
            pos = (xMin,yMin,iz)
            lz = gl.GLTextItem(pos=pos, color=colorTexto, text=str(iz), font=QFont(fuente, fontSize))
            self.textos.append(lz)
        
    def loadOnGlView(self,GlView:GLViewWidget):
        self.GLView = GlView
        for rejilla in self.rejillas:
            GlView.addItem(rejilla)
        for texto in self.textos:
            GlView.addItem(texto)
    
    def setGridColor(self,color):
        for rejilla in self.rejillas:
            rejilla.setColor(color)
    
    def setTextColor(self,color):
        for texto in self.textos:
            texto.setData(**{'color':color})
    
class Cono():
    def __init__(self,n:int,pos:np.array,vec:np.array,t:float,d:float,color:list,drawEdges:bool,color_borde:list):
        self.n = n
        self.pos = pos
        self.vec = vec
        self.t = t
        self.d = d 
        self.carasVisibles = 2*n
        self.scatter = None
        self.linea = None
        self.generateVertexFaces()
        self.caras = self.carasCompletas[:,:]
        self.mesh = gl.GLMeshItem(vertexes=self.vertices, faces=self.caras, color=color, smooth=True, shader='shaded', 
                   drawEdges=drawEdges, edgeColor=color_borde)
        
    def generateVertexFaces(self):
        n = self.n
        pos = self.pos[:]
        vec = self.vec[:]
        t = self.t
        d = self.d
        vec = (vec/norm(vec))*t
        ax = vec[0]
        ay = vec[1]
        az = vec[2]
        if ax!=0:
            bx = -((ay+az)/ax)
            B = np.array([bx,1,1])
            B = (B/sqrt(bx**2+1+1))*(d/2)
        elif ay!=0:
            by = -((ax+az)/ay)
            B = np.array([1,by,1])
            B = (B/sqrt(by**2+1+1))*(d/2)
        else:
            bz = -((ay+ax)/az)
            B = np.array([1,1,bz])
            B = (B/sqrt(bz**2+1+1))*(d/2)
        
        vertices = np.zeros((n+2,3))
        vertices[0,:] = pos
        vertices[1,:] = vec+pos
        
        caras = np.zeros((2*n,3))
        
        k=0
        for i in range(2):
            for j in range(n):
                if j!=n-1:
                    caras[k,:] = np.array([i,j+2,j+3])
                else:
                    caras[k,:] = np.array([i,j+2,2])
                k+=1
        caras = caras.astype(int)
        
        r1 = np.insert(B,0,0)
        for i in range(n):
            Q = crearCuaternio((i+1)*2*pi/n,vec)
            conjQ = conjCuaternio(Q)
            r2 = proCuaternios(proCuaternios(Q,r1),conjQ)
            vertices[i+2,:] = r2[1:4] + pos
        self.vertices = vertices
        self.carasCompletas = caras
        self.caras = self.carasCompletas[0:self.carasVisibles,:]
        if self.scatter != None:
            self.scatter.setData(pos=self.vertices)
        if self.linea != None:
            self.linea.setData(pos=self.vertices[0:2,:])
        
    def generateVertex(self):
        n = self.n
        pos = self.pos[:]
        vec = self.vec[:]
        t = self.t
        d = self.d
        vec = (vec/norm(vec))*t
        ax = vec[0]
        ay = vec[1]
        az = vec[2]
        if ax!=0:
            bx = -((ay+az)/ax)
            B = np.array([bx,1,1])
            B = (B/sqrt(bx**2+1+1))*(d/2)
        elif ay!=0:
            by = -((ax+az)/ay)
            B = np.array([1,by,1])
            B = (B/sqrt(by**2+1+1))*(d/2)
        else:
            bz = -((ay+ax)/az)
            B = np.array([1,1,bz])
            B = (B/sqrt(bz**2+1+1))*(d/2)
            
        vertices = np.zeros((n+2,3))
        vertices[0,:] = pos
        vertices[1,:] = vec+pos
        r1 = np.insert(B,0,0)
        for i in range(n):
            Q = crearCuaternio((i+1)*2*pi/n,vec)
            conjQ = conjCuaternio(Q)
            r2 = proCuaternios(proCuaternios(Q,r1),conjQ)
            vertices[i+2,:] = r2[1:4] + pos
        self.vertices = vertices
        if self.scatter != None:
            self.scatter.setData(pos=self.vertices)
        if self.linea != None:
            self.linea.setData(pos=self.vertices[0:2,:])
        
    def loadOnGlView(self,glView:GLViewWidget):
        self.GLView = glView
        glView.addItem(self.mesh)
        
    def setN(self,n:int):
        self.n = n
        self.generateVertexFaces()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
        
    def setT(self,t:float):
        self.t = t
        self.generateVertex()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
    
    def setD(self,d:float):
        self.d = d
        self.generateVertex()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
    
    def setGeometry(self,n:int,pos:np.array,vec:np.array,t:float,d:float):
        self.n = n
        self.pos = pos[:]
        self.vec = vec[:]
        self.t = t
        self.d = d
        self.generateVertex()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
    
    def setCarasVisibles(self,carasVisibles):
        self.carasVisibles = carasVisibles
        self.caras = self.carasCompletas[0:carasVisibles,:]
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
        
    def dibujarVertices(self,glView:GLViewWidget):
        self.scatter = gl.GLScatterPlotItem(pos=self.vertices, color=(1, 1, 1, 1), size=0.2, pxMode=False)
        glView.addItem(self.scatter)
        
    def dibujarLinea(self,glView:GLViewWidget):
        self.linea = gl.GLLinePlotItem(pos=self.vertices[0:2,:], color="b", width=2, antialias=True)
        glView.addItem(self.linea)

    def setShader(self,shader):
        self.mesh.setShader(shader)

    def removeItem(self):
        self.GLView.removeItem(self.mesh)
    
    def show(self):
        self.mesh.show()
        
    def hide(self):
        self.mesh.hide()
    
class Cilindro():
    def __init__(self,n:int,pos:np.array,vec:np.array,t:float,d:float,color:list,drawEdges:bool,color_borde:list):
        self.n = n
        self.pos = pos
        self.vec = vec
        self.t = t
        self.d = d 
        self.carasVisibles = 2*n
        self.scatter = None
        self.generateVertexFaces()
        self.caras = self.carasCompletas[:,:]
        self.mesh = gl.GLMeshItem(vertexes=self.vertices, faces=self.caras, color=color, smooth=True, shader='shaded', 
                   drawEdges=drawEdges, edgeColor=color_borde)
         
    def generateVertexFaces(self):
        n = self.n
        pos = self.pos[:]
        vec = self.vec[:]
        t = self.t
        d = self.d
        vec = (vec/norm(vec))*t
        ax = vec[0]
        ay = vec[1]
        az = vec[2]
        if ax!=0:
            bx = -((ay+az)/ax)
            B = np.array([bx,1,1])
            B = (B/sqrt(bx**2+1+1))*(d/2)
        elif ay!=0:
            by = -((ax+az)/ay)
            B = np.array([1,by,1])
            B = (B/sqrt(by**2+1+1))*(d/2)
        else:
            bz = -((ay+ax)/az)
            B = np.array([1,1,bz])
            B = (B/sqrt(bz**2+1+1))*(d/2)
        
        vertices = np.zeros((2*n,3))
        
        caras = np.zeros((2*n,3))
        
        caras[n-1,:] = np.array([0,n-1,2*n-1])
        caras[2*n-1,:] = np.array([0,2*n-1,n])
        
        for i in range(n-1):
            caras[i,:] = np.array([i,i+1,n+i])
        for i in range(n-1):
            caras[i+n,:] = np.array([i+1,n+i,n+i+1])
        
        caras = caras.astype(int)
        
        r1 = np.insert(B,0,0)
        for i in range(n):
            Q = crearCuaternio((i+1)*2*pi/n,vec)
            conjQ = conjCuaternio(Q)
            r2 = proCuaternios(proCuaternios(Q,r1),conjQ)
            vertices[i,:] = r2[1:4] + pos
            vertices[i+n,:] = r2[1:4] + pos + vec
        self.vertices = vertices
        self.carasCompletas = caras
        self.caras = self.carasCompletas[0:self.carasVisibles,:]
        if self.scatter != None:
            self.scatter.setData(pos=self.vertices)
        
    def generateVertex(self):
        n = self.n
        pos = self.pos[:]
        vec = self.vec[:]
        t = self.t
        d = self.d
        vec = (vec[:]/norm(vec[:]))*t
        ax = vec[0]
        ay = vec[1]
        az = vec[2]
        if ax!=0:
            bx = -((ay+az)/ax)
            B = np.array([bx,1,1])
            B = (B/sqrt(bx**2+1+1))*(d/2)
        elif ay!=0:
            by = -((ax+az)/ay)
            B = np.array([1,by,1])
            B = (B/sqrt(by**2+1+1))*(d/2)
        else:
            bz = -((ay+ax)/az)
            B = np.array([1,1,bz])
            B = (B/sqrt(bz**2+1+1))*(d/2)
        
        vertices = np.zeros((2*n,3))
        
        r1 = np.insert(B,0,0)
        for i in range(n):
            Q = crearCuaternio((i+1)*2*pi/n,vec)
            conjQ = conjCuaternio(Q)
            r2 = proCuaternios(proCuaternios(Q,r1),conjQ)
            vertices[i,:] = r2[1:4] + pos
            vertices[i+n,:] = r2[1:4] + pos + vec
        self.vertices = vertices
        if self.scatter != None:
            self.scatter.setData(pos=self.vertices)
        
    def loadOnGlView(self,glView:GLViewWidget):
        self.GLView = glView
        glView.addItem(self.mesh)
        
    def setN(self,n):
        self.n = n
        self.generateVertexFaces()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
        
    def setT(self,t):
        self.t = t
        self.generateVertex()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
    
    def setD(self,d):
        self.d = d
        self.generateVertex()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
    
    def setGeometry(self,n:int,pos:np.array,vec:np.array,t:float,d:float):
        self.n = n
        self.pos = pos[:]
        self.vec = vec[:]
        self.t = t
        self.d = d
        self.generateVertex()
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
    
    def setCarasVisibles(self,carasVisibles):
        self.carasVisibles = carasVisibles
        self.caras = self.carasCompletas[0:carasVisibles,:]
        self.mesh.setMeshData(**{'vertexes':self.vertices,'faces': self.caras})
        self.mesh.meshDataChanged()
        
    def dibujarVertices(self,glView:GLViewWidget):
        self.scatter = gl.GLScatterPlotItem(pos=self.vertices, color=(1, 1, 1, 1), size=0.2, pxMode=False)
        glView.addItem(self.scatter)

    def setShader(self,shader):
        self.mesh.setShader(shader)

    def removeItem(self):
        self.GLView.removeItem(self.mesh)
    
    def show(self):
        self.mesh.show()
        
    def hide(self):
        self.mesh.hide()
    
class Flecha():
    def __init__(self,pos:np.array, vec:np.array,tflecha:float, tpunta:float,dcil:float,dcono:float, color:list) -> None:
        self.pos = pos
        self.vec = vec
        self.tflecha = tflecha
        self.tpunta = tpunta
        self.dcil = dcil
        self.dcono = dcono
        self.color = color
        drawEdges = False
        self.drawEdges = drawEdges
        color_borde = color[:]
        self.color_borde = color_borde
        shader = 'edgeHilight'  # 'balloon', 'normalColor', 'viewNormalColor', 'shaded', 'edgeHilight', 'heightColor'
        n = 20
        self.n = n
        
        tCilindro = tflecha-tpunta
        vecCilindro = (vec/norm(vec))*tCilindro
        posFlecha = vecCilindro + pos
        self.cilindro = Cilindro(n,pos, vec,tCilindro,dcil, color, drawEdges, color_borde)
        self.cono = Cono(n,posFlecha, vec,tpunta,dcono, color, drawEdges, color_borde)
        
    def actualizarFlecha(self):
        tCilindro = self.tflecha-self.tpunta
        vecCilindro = (self.vec/norm(self.vec))*tCilindro
        posFlecha = vecCilindro + self.pos
        
        self.cilindro.setGeometry(self.n,self.pos[:],self.vec[:],tCilindro,self.dcil)
        self.cono.setGeometry(self.n,posFlecha,self.vec,self.tpunta,self.dcono)
        
    def loadOnGlView(self,glView:GLViewWidget):
        self.GLView = glView
        self.cilindro.loadOnGlView(glView)
        self.cono.loadOnGlView(glView)
        
    def setTFlecha(self,tFlecha):
        self.tflecha = tFlecha
        if self.tflecha == self.tpunta:
            self.tpunta = self.tflecha-1
        self.actualizarFlecha()
        
    def setTPunta(self,tpunta):
        self.tpunta = tpunta
        self.actualizarFlecha()
    
    def setDCil(self,dcil):
        self.dcil = dcil
        self.actualizarFlecha()
        
    def setDcono(self,dcono):
        self.dcono = dcono
        self.actualizarFlecha()
    
    def setGeometry(self,pos:np.array, vec:np.array,tflecha:float, tpunta:float,dcil:float,dcono:float):
        self.pos = pos[:]
        self.vec = vec[:]
        self.tflecha = tflecha
        self.tpunta = tpunta
        self.dcil = dcil
        self.dcono = dcono
        self.actualizarFlecha()

    def setShader(self,shader):
        self.cilindro.setShader(shader)
        self.cono.setShader(shader)

    def removeItem(self):
        self.cono.removeItem()
        self.cilindro.removeItem()

    def show(self):
        self.cono.show()
        self.cilindro.show()
        
    def hide(self):
        self.cono.hide()
        self.cilindro.hide()

class SistemaCoordenadas3D(QObject):
    animacionTerminada = Signal()
    def __init__(self,A:np.array, L:float, G:float, texto:str):
        super().__init__()
        self.fontSize = 12
        self.fuente = 'Helvetica'
        colorTexto = [200,200,200]
        shader = 'edgeHilight'  # 'balloon', 'normalColor', 'viewNormalColor', 'shaded', 'edgeHilight', 'heightColor'
        self.colorX = [0,0,1,1]
        self.colorY = [1,1,0,1]
        self.colorZ = [0,1,0,1]
        self.A = A[:,:]
        
        self.setL(L,False)
        self.setA(A,False)
        self.setG(G,False)
        self.setText(texto,False)
        
        self.flechaX = Flecha(self.pos[:],self.vecX[:],self.L,self.tpunta,self.G,self.dcono,self.colorX)
        self.flechaY = Flecha(self.pos[:],self.vecY[:],self.L,self.tpunta,self.G,self.dcono,self.colorY)
        self.flechaZ = Flecha(self.pos[:],self.vecZ[:],self.L,self.tpunta,self.G,self.dcono,self.colorZ)
        
        self.tX = gl.GLTextItem(pos=(self.ptx[:,0:1],self.ptx[:,1:2],self.ptx[:,2:3]), color=colorTexto, text="X"+self.sub(self.text), font=QFont(self.fuente, self.fontSize))
        self.tY = gl.GLTextItem(pos=(self.pty[:,0:1],self.pty[:,1:2],self.pty[:,2:3]), color=colorTexto, text="Y"+self.sub(self.text), font=QFont(self.fuente, self.fontSize))
        self.tZ = gl.GLTextItem(pos=(self.ptz[:,0:1],self.ptz[:,1:2],self.ptz[:,2:3]), color=colorTexto, text="Z"+self.sub(self.text), font=QFont(self.fuente, self.fontSize))
        
        self.setShader(shader)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.avanzarCuadro)
        
        
    def loadOnGlView(self,glView:GLViewWidget):
        self.GLView = glView
        self.flechaX.loadOnGlView(glView)
        self.flechaY.loadOnGlView(glView)
        self.flechaZ.loadOnGlView(glView)
        glView.addItem(self.tX)
        glView.addItem(self.tY)
        glView.addItem(self.tZ)
        
    def actualizar(self):
        self.flechaX.setGeometry(self.pos[:],self.vecX[:],self.L,self.tpunta,self.G,self.dcono)
        self.flechaY.setGeometry(self.pos[:],self.vecY[:],self.L,self.tpunta,self.G,self.dcono)
        self.flechaZ.setGeometry(self.pos[:],self.vecZ[:],self.L,self.tpunta,self.G,self.dcono)
        self.tX.setData(pos=(self.ptx[:,0:1],self.ptx[:,1:2],self.ptx[:,2:3]), color='w', text="X"+self.sub(self.text), font=QFont(self.fuente, self.fontSize))
        self.tY.setData(pos=(self.pty[:,0:1],self.pty[:,1:2],self.pty[:,2:3]), color='w', text="Y"+self.sub(self.text), font=QFont(self.fuente, self.fontSize))
        self.tZ.setData(pos=(self.ptz[:,0:1],self.ptz[:,1:2],self.ptz[:,2:3]), color='w', text="Z"+self.sub(self.text), font=QFont(self.fuente, self.fontSize))
        
    def sub(self,numero):
        text = str(numero)
        subindice = ''
        n = len(text)
        for i in range(n):
            subindice = subindice + chr(ord(text[i]) + 8272)
        return subindice
        
    def setA(self,A:np.array,load=True):
        self.A = A[:,:]
        self.pos = A[0:3,3].T
        self.vecX = A[0:3,0].T
        self.vecY = A[0:3,1].T
        self.vecZ = A[0:3,2].T
        ptx = A @ np.array([[self.L],
                            [0],
                            [0],
                            [1]])
        
        pty = A @ np.array([[0],
                            [self.L],
                            [0],
                            [1]])
        
        ptz = A @ np.array([[0],
                            [0],
                            [self.L],
                            [1]])
        self.ptx = ptx.T[: , 0:3]
        self.pty = pty.T[: , 0:3]
        self.ptz = ptz.T[: , 0:3]
        if load:
            self.actualizar()
        
    def setL(self,L,load=True):
        self.L = L
        if load:
            ptx = self.A @ np.array([[self.L],
                                     [0],
                                     [0],
                                     [1]])
            
            pty = self.A @ np.array([[0],
                                     [self.L],
                                     [0],
                                     [1]])
            
            ptz = self.A @ np.array([[0],
                                     [0],
                                     [self.L],
                                     [1]])
            self.ptx = ptx.T[: , 0:3]
            self.pty = pty.T[: , 0:3]
            self.ptz = ptz.T[: , 0:3]
            self.actualizar()
        
    def setG(self,G,load=True):
        self.G = G
        self.tpunta = G*1.5
        self.dcono = G*2.2
        if load:
            self.actualizar()
        
    def setText(self,text,load=True):
        self.text = text
        if load:
            self.actualizar()
            
    def setShader(self,shader):
        self.flechaX.setShader(shader)
        self.flechaY.setShader(shader)
        self.flechaZ.setShader(shader)
    
    def removeItem(self):
        self.flechaX.removeItem()
        self.flechaY.removeItem()
        self.flechaZ.removeItem()
        self.GLView.removeItem(self.tX)
        self.GLView.removeItem(self.tY)
        self.GLView.removeItem(self.tZ)
        
    def show(self):
        self.flechaX.show()
        self.flechaY.show()
        self.flechaZ.show()
        self.tX.show()
        self.tY.show()
        self.tZ.show()
        
    def hide(self):
        self.flechaX.hide()
        self.flechaY.hide()
        self.flechaZ.hide()
        self.tX.hide()
        self.tY.hide()
        self.tZ.hide()
        
    def iniciarAnimacion(self,MTHs:list,t:list):
        self.MTHs = MTHs
        self.t = t
        self.n = len(MTHs)
        self.i = 1
        self.setA(MTHs[0])
        self.dt = t[1]-t[0]
        self.timer.start(self.dt)
    
    def avanzarCuadro(self):
        self.setA(self.MTHs[self.i])
        if self.i != self.n-1:
            self.i+=1
            if round(self.dt) != round(self.t[self.i]-self.t[self.i-1]):
                self.dt = self.t[self.i]-self.t[self.i-1]
                self.timer.setInterval(self.dt)
        else:
            self.timer.stop()
            self.animacionTerminada.emit()
    
class Solido():
    def __init__(self,A:np.array):
        self.bordes = False
        self.bordesColor = [0,0,0,1]
        self.tamanioEjes = 90
        self.diametroEjes = 5
        self.color_0 = [1,0,0,1]
        ######################################## Se carga el eslabón 0  ##################################
        archivo_excel = 'resources/CADS/RobotCilindrico/Eslabon_0.xlsx'
        # Lee la hoja de cálculo deseada en un DataFrame de pandas
        self.vertices_0_a = pd.read_excel(archivo_excel, sheet_name='Vertices').values
        self.caras_0 = pd.read_excel(archivo_excel, sheet_name='Caras').values
        ##################################################################################################
        self.vertices_0 = np.zeros((self.vertices_0_a.shape[0],3))
        self.setA(A,False)
        ########################################  Se crea el eslabón 0  ##################################
        shader = 'edgeHilight'  # 'balloon', 'normalColor', 'viewNormalColor', 'shaded', 'edgeHilight', 'heightColor'
        self.eslabon_0 = gl.GLMeshItem(vertexes=self.vertices_0, faces=self.caras_0, color=self.color_0, smooth=True, shader=shader, 
                    drawEdges=self.bordes, edgeColor=self.bordesColor)
        self.eslabon_0.setGLOptions('translucent')
        ##################################################################################################
        self.sistema_0 = SistemaCoordenadas3D(A,self.tamanioEjes,self.diametroEjes,'0')
    def setA(self,A:np.array,load=True):
        self.A = A
        for i in range(self.vertices_0.shape[0]):
            P = self.vertices_0_a[i,:]
            P = np.append(P,1).T
            P = self.A @ P
            self.vertices_0[i,:] = P[0:3]
        if load:
            self.eslabon_0.setMeshData(**{'vertexes':self.vertices_0,'faces': self.caras_0})
            self.sistema_0.setA(A)
    def loadOnGlView(self,glView:GLViewWidget):
        glView.addItem(self.eslabon_0)
        self.sistema_0.loadOnGlView(glView)
    
class RobotCilindrico(QObject):
    # Definir una señal personalizada
    animacionTerminada = Signal()
    def __init__(self,q1:float,q2:float,q3:float,q4:float):
        super().__init__()
        self.bordes = False
        self.bordesColor = [0,0,0,1]
        self.tamanioEjes = 90
        self.diametroEjes = 5
        self.en3D = 2
        self.L1 = 170
        self.L2 = 75
        self.L4 = 70
        self.color_0 = [173/255,51/255,51/255,1]
        self.color_1 = [0/255,51/255,102/255,1]
        self.color_2 = [218/255,218/255,218/255,1]
        self.color_3 = [239/255,184/255,16/255,1]
        self.color_4 = [173/255,51/255,51/255,1]
        shader = 'edgeHilight'  # 'balloon', 'normalColor', 'viewNormalColor', 'shaded', 'edgeHilight', 'heightColor'
        self.anchoLineas = 10
        ################################## Se crea el timer para la animación  ###########################
        self.timer = QTimer()
        self.timer.timeout.connect(self.avanzarCuadro)
        ######################################## Se carga el eslabón 0  ##################################
        archivo_excel = 'resources/CADS/RobotCilindrico/Eslabon_0.xlsx'
        # Lee la hoja de cálculo deseada en un DataFrame de pandas
        self.vertices_0 = pd.read_excel(archivo_excel, sheet_name='Vertices').values
        self.caras_0 = pd.read_excel(archivo_excel, sheet_name='Caras').values
        ##################################################################################################
        ######################################## Se carga el eslabón 1  ##################################
        archivo_excel = 'resources/CADS/RobotCilindrico/Eslabon_1.xlsx'
        # Lee la hoja de cálculo deseada en un DataFrame de pandas
        self.vertices_1_a = pd.read_excel(archivo_excel, sheet_name='Vertices').values
        self.caras_1 = pd.read_excel(archivo_excel, sheet_name='Caras').values
        ##################################################################################################
        ######################################## Se carga el eslabón 2  ##################################
        archivo_excel = 'resources/CADS/RobotCilindrico/Eslabon_2.xlsx'
        # Lee la hoja de cálculo deseada en un DataFrame de pandas
        self.vertices_2_a = pd.read_excel(archivo_excel, sheet_name='Vertices').values
        self.caras_2 = pd.read_excel(archivo_excel, sheet_name='Caras').values
        ##################################################################################################
        ######################################## Se carga el eslabón 3  ##################################
        archivo_excel = 'resources/CADS/RobotCilindrico/Eslabon_3.xlsx'
        # Lee la hoja de cálculo deseada en un DataFrame de pandas
        self.vertices_3_a = pd.read_excel(archivo_excel, sheet_name='Vertices').values
        self.caras_3 = pd.read_excel(archivo_excel, sheet_name='Caras').values
        ##################################################################################################
        ######################################## Se carga el eslabón 4  ##################################
        archivo_excel = 'resources/CADS/RobotCilindrico/Eslabon_4.xlsx'
        # Lee la hoja de cálculo deseada en un DataFrame de pandas
        self.vertices_4_a = pd.read_excel(archivo_excel, sheet_name='Vertices').values
        self.caras_4 = pd.read_excel(archivo_excel, sheet_name='Caras').values
        ##################################################################################################
        ############################### Se inicializan los vertices movibles #############################
        self.vertices_1 = np.zeros((self.vertices_1_a.shape[0],3))
        self.vertices_2 = np.zeros((self.vertices_2_a.shape[0],3))
        self.vertices_3 = np.zeros((self.vertices_3_a.shape[0],3))
        self.vertices_4 = np.zeros((self.vertices_4_a.shape[0],3))
        ##################################################################################################
        #####################  Se calculan los vertices segun cinemática dirécta  ########################
        self.setPosQ(q1,q2,q3,q4,False)
        ##################################################################################################
        ########################################  Se crea el eslabón 0  ##################################
        self.eslabon_0 = gl.GLMeshItem(vertexes=self.vertices_0, faces=self.caras_0, color=self.color_0, smooth=True, shader=shader, 
                    drawEdges=self.bordes, edgeColor=self.bordesColor)
        self.eslabon_0.setGLOptions('translucent')
        ##################################################################################################
        ########################################  Se crea el eslabón 1  ##################################
        self.eslabon_1 = gl.GLMeshItem(vertexes=self.vertices_1, faces=self.caras_1, color=self.color_1, smooth=True, shader=shader, 
                    drawEdges=self.bordes, edgeColor=self.bordesColor)
        self.eslabon_1.setGLOptions('translucent')
        ##################################################################################################
        ########################################  Se crea el eslabón 2  ##################################
        self.eslabon_2 = gl.GLMeshItem(vertexes=self.vertices_2, faces=self.caras_2, color=self.color_2, smooth=True, shader=shader, 
                    drawEdges=self.bordes, edgeColor=self.bordesColor)
        self.eslabon_2.setGLOptions('translucent')
        ##################################################################################################
        ########################################  Se crea el eslabón 3  ##################################
        self.eslabon_3 = gl.GLMeshItem(vertexes=self.vertices_3, faces=self.caras_3, color=self.color_3, smooth=True, shader=shader, 
                    drawEdges=self.bordes, edgeColor=self.bordesColor)
        self.eslabon_3.setGLOptions('translucent')
        ##################################################################################################
        ########################################  Se crea el eslabón 4  ##################################
        self.eslabon_4 = gl.GLMeshItem(vertexes=self.vertices_4, faces=self.caras_4, color=self.color_4, smooth=True, shader=shader, 
                    drawEdges=self.bordes, edgeColor=self.bordesColor)
        self.eslabon_4.setGLOptions('translucent')
        ##################################################################################################
        ##########################  Se crean los sistemas de ejes coordenados 3D  ########################
        self.sistema_0 = SistemaCoordenadas3D(np.eye(4,4),self.tamanioEjes,self.diametroEjes,'0')
        self.sistema_1 = SistemaCoordenadas3D(self.A01,self.tamanioEjes,self.diametroEjes,'1')
        self.sistema_2 = SistemaCoordenadas3D(self.A02,self.tamanioEjes,self.diametroEjes,'2')
        self.sistema_3 = SistemaCoordenadas3D(self.A03,self.tamanioEjes,self.diametroEjes,'3')
        self.sistema_4 = SistemaCoordenadas3D(self.A04,self.tamanioEjes,self.diametroEjes,'4')
        ##################################################################################################
        ####################  Se crean las lineas y puntos del robot (esquema)  ##########################
        self.linea_1 = gl.GLLinePlotItem(pos=self.puntos[0:2,:], color=self.color_0, width=self.anchoLineas, antialias=True)
        self.linea_2 = gl.GLLinePlotItem(pos=self.puntos[1:3,:], color=self.color_1, width=self.anchoLineas, antialias=True)
        self.linea_3 = gl.GLLinePlotItem(pos=self.puntos[2:4,:], color=self.color_2, width=self.anchoLineas, antialias=True)
        self.linea_4 = gl.GLLinePlotItem(pos=self.puntos[3:5,:], color=self.color_3, width=self.anchoLineas, antialias=True)
        self.linea_5 = gl.GLLinePlotItem(pos=self.puntos[4:6,:], color=self.color_4, width=self.anchoLineas, antialias=True)
        self.linea_1.hide()
        self.linea_2.hide()
        self.linea_3.hide()
        self.linea_4.hide()
        self.linea_5.hide()
        self.glPuntos = gl.GLScatterPlotItem(pos=np.delete(self.puntos, 0, axis=0), color=(1, 1, 1, 1), size=20, pxMode=False)
        self.glPuntos.hide()
        ##################################################################################################
        ############################  Se crea el texto que muestra el punto  #############################
        px = round(self.A04[0,3],1)
        py = round(self.A04[1,3],1)
        pz = round(self.A04[2,3],1)
        texto = "XYZ efector final:\n("+str(px)+", "+str(py)+", "+str(pz)+")"
        self.textP4 = DynamicTextItem(texto)
        ##################################################################################################
        
    def setPosQ(self,q1:float,q2:float,q3:float,q4:float,load=True):
        Par = np.array([
            [radians(q1), self.L1,        0,            0],
            [          0,      q2, -self.L2, radians(-90)],
            [          0,      q3,        0,            0],
            [radians(q4), self.L4,        0,            0]
        ])
        A01 = D_H(Par[0,:])
        A12 = D_H(Par[1,:])
        A23 = D_H(Par[2,:])
        A34 = D_H(Par[3,:])
        
        A02 = A01 @ A12
        A03 = A02 @ A23
        A04 = A03 @ A34
        
        self.A12 = A12
        self.A23 = A23
        self.A34 = A34
        self.A01 = A01
        self.A02 = A02
        self.A03 = A03
        self.A04 = A04
        p12 = np.eye(4)
        p12[0,3] = self.L2
        p12 = A02@p12
        self.puntos = np.array([[0,0,0],
                             A01[0:3,3].T,
                             p12[0:3,3].T,
                             A02[0:3,3].T,
                             A03[0:3,3].T,
                             A04[0:3,3].T])
        if self.en3D==2:
            self.calcVertices()
            if load:
                self.loadVertices()
        elif self.en3D==1:
            if load:
                self.loadLineas()
        if self.en3D!=0:
            if load:
                self.sistema_1.setA(self.A01)
                self.sistema_2.setA(self.A02)
                self.sistema_3.setA(self.A03)
                self.sistema_4.setA(self.A04)
                px = round(self.A04[0,3],1)
                py = round(self.A04[1,3],1)
                pz = round(self.A04[2,3],1)
                texto = "XYZ efector final:\n("+str(px)+", "+str(py)+", "+str(pz)+")"
                self.textP4.setText(texto)
                  
    def calcVertices(self):
        for i in range(self.vertices_1.shape[0]):
            P = self.vertices_1_a[i,:]
            P = np.append(P,1).T
            P = self.A01 @ P
            self.vertices_1[i,:] = P[0:3]
        for i in range(self.vertices_2.shape[0]):
            P = self.vertices_2_a[i,:]
            P = np.append(P,1).T
            P = self.A02 @ P
            self.vertices_2[i,:] = P[0:3]
        for i in range(self.vertices_3.shape[0]):
            P = self.vertices_3_a[i,:]
            P = np.append(P,1).T
            P = self.A03 @ P
            self.vertices_3[i,:] = P[0:3]
        for i in range(self.vertices_4.shape[0]):
            P = self.vertices_4_a[i,:]
            P = np.append(P,1).T
            P = self.A04 @ P
            self.vertices_4[i,:] = P[0:3]
        
    def loadVertices(self):
        self.eslabon_1.setMeshData(**{'vertexes':self.vertices_1,'faces': self.caras_1})
        self.eslabon_2.setMeshData(**{'vertexes':self.vertices_2,'faces': self.caras_2})
        self.eslabon_3.setMeshData(**{'vertexes':self.vertices_3,'faces': self.caras_3})
        self.eslabon_4.setMeshData(**{'vertexes':self.vertices_4,'faces': self.caras_4})
        
    def loadLineas(self):
        self.linea_1.setData(pos=self.puntos[0:2,:])
        self.linea_2.setData(pos=self.puntos[1:3,:])
        self.linea_3.setData(pos=self.puntos[2:4,:])
        self.linea_4.setData(pos=self.puntos[3:5,:])
        self.linea_5.setData(pos=self.puntos[4:6,:])
        self.glPuntos.setData(pos=np.delete(self.puntos, 0, axis=0))
        
    def loadOnGlView(self,glView:GLViewWidget):
        glView.addItem(self.eslabon_0)
        glView.addItem(self.eslabon_1)
        glView.addItem(self.eslabon_2)
        glView.addItem(self.eslabon_3)
        glView.addItem(self.eslabon_4)
        self.sistema_0.loadOnGlView(glView)
        self.sistema_1.loadOnGlView(glView)
        self.sistema_2.loadOnGlView(glView)
        self.sistema_3.loadOnGlView(glView)
        self.sistema_4.loadOnGlView(glView)
        glView.addItem(self.linea_1)
        glView.addItem(self.linea_2)
        glView.addItem(self.linea_3)
        glView.addItem(self.linea_4)
        glView.addItem(self.linea_5)
        glView.addItem(self.glPuntos)
        glView.addItem(self.textP4)
        
    def setEn3D(self,en3D):
        if en3D==2:
            self.calcVertices()
            self.loadVertices()
            self.eslabon_0.show()
            self.eslabon_1.show()
            self.eslabon_2.show()
            self.eslabon_3.show()
            self.eslabon_4.show()
            self.linea_1.hide()
            self.linea_2.hide()
            self.linea_3.hide()
            self.linea_4.hide()
            self.linea_5.hide()
            self.glPuntos.hide()
            self.sistema_0.show()
            self.sistema_1.show()
            self.sistema_2.show()
            self.sistema_3.show()
            self.sistema_4.show()
            self.en3D = en3D
        elif en3D==1:
            self.loadLineas()
            self.eslabon_0.hide()
            self.eslabon_1.hide()
            self.eslabon_2.hide()
            self.eslabon_3.hide()
            self.eslabon_4.hide()
            self.linea_1.show()
            self.linea_2.show()
            self.linea_3.show()
            self.linea_4.show()
            self.linea_5.show()
            self.glPuntos.show()
            self.sistema_0.show()
            self.sistema_1.show()
            self.sistema_2.show()
            self.sistema_3.show()
            self.sistema_4.show()
            self.en3D = en3D
        elif en3D==0:
            self.loadLineas()
            self.eslabon_0.hide()
            self.eslabon_1.hide()
            self.eslabon_2.hide()
            self.eslabon_3.hide()
            self.eslabon_4.hide()
            self.linea_1.hide()
            self.linea_2.hide()
            self.linea_3.hide()
            self.linea_4.hide()
            self.linea_5.hide()
            self.glPuntos.hide()
            self.sistema_0.hide()
            self.sistema_1.hide()
            self.sistema_2.hide()
            self.sistema_3.hide()
            self.sistema_4.hide()
            self.en3D = en3D
        
    def iniciarAinimacion(self,puntos:np.ndarray):
        if self.en3D!=0:
            self.puntosA = puntos
            self.n = puntos.shape[0]
            self.i = 1
            self.setPosQ(puntos[0,1],puntos[0,2],puntos[0,3],puntos[0,4])
            self.dt = puntos[1,0]-puntos[0,0]
            self.timer.start(self.dt)
        else:
            self.animacionTerminada.emit()
        
    def detenerAnimacion(self):
        self.timer.stop()
        self.animacionTerminada.emit()
        
    ## Método que se llama cada vez que se desborda el timer de la animación
    def avanzarCuadro(self):
        self.setPosQ(self.puntosA[self.i,1],self.puntosA[self.i,2],self.puntosA[self.i,3],self.puntosA[self.i,4])
        if self.i != self.n-1:
            self.i+=1
            if round(self.dt) != round(self.puntosA[self.i,0]-self.puntosA[self.i-1,0]):
                self.dt = self.puntosA[self.i,0]-self.puntosA[self.i-1,0]
                self.timer.setInterval(self.dt)
        else:
            self.timer.stop()
            self.animacionTerminada.emit()
    
    def setShader(self,shader):
        self.eslabon_0.setShader(shader)
        self.eslabon_1.setShader(shader)
        self.eslabon_2.setShader(shader)
        self.eslabon_3.setShader(shader)
        self.eslabon_4.setShader(shader)
        
class DynamicTextItem(gl.GLGraphicsItem.GLGraphicsItem):
    def __init__(self, text=""):
        super().__init__()
        self.text = text
        self.setGLOptions('translucent')

    def setText(self, text):
        self.text = text
        self.update()

    def paint(self):
        self.setupGLState()
        painter = QtGui.QPainter(self.view())
        painter.setPen(Qt.white)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        rect = self.view().rect()
        painter.drawText(rect, Qt.AlignTop | Qt.AlignLeft, self.text)
        painter.end()