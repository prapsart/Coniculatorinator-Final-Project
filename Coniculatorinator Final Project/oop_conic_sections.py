# This file contains the classes which will generate the graph
# Imported by main_menu.py

import numpy as np
import matplotlib.pyplot as plt     # Importations of packages

class ConicSection(): # PARENT CLASS - Inherited by all the classes
    def __init__(self): # Generates the cartesian plane
        self.x = np.linspace(-20,20)
        self.y = np.linspace(-20,20)
        self.x,self.y = np.meshgrid(self.x,self.y)
        self.fig,self.ax=plt.subplots()
        self.axes()
    
    def axes(self): # Generates the X and Y Axes lines
        plt.axhline(0, alpha = .1)
        plt.axvline(0, alpha = .1)


class RightLeftParabola(ConicSection): # RIGHT/LEFT PARABOLAS
    def __init__(self,h,k,p):
        super().__init__()
        self.h = h
        self.k = k
        self.p = p
    
    def graph_parts(self):
        V = (self.h,self.k)
        #axes()
        plt.contour(self.x+V[0], self.y+V[1], (self.y**(2) - 4*self.p*self.x), [0], colors='k')
        # Focus.
        plt.plot(V[0]+self.p,V[1], '.-r')
        # Vertex
        plt.plot(V[0],V[1], '.-b')
        # Directrix.
        plt.axvline(-self.p+V[0], linestyle='--', color='g')
        # Latus rectum
        lr1 = V[1]+(2*self.p)
        lr2 = V[1]-(2*self.p)
        self.ax.vlines(V[0]+self.p,lr1,lr2, linestyle='-.', color='m')
        
        plt.show()


class UpDownParabola(ConicSection): # UPWARD/DOWNWARD PARABOLA
    def __init__(self,h,k,p):
        super().__init__()
        self.h = h
        self.k = k
        self.p = p
    
    def graph_parts(self):
        V = (self.h,self.k)
        plt.contour(self.x+V[0], self.y+V[1], (self.x**(2) - 4*self.p*self.y), [0], colors='k')
        # Focus.
        plt.plot(V[0],V[1]+self.p, '.-r')
        # Vertex
        plt.plot(V[0],V[1], '.-b')
        # Directrix.
        plt.axhline(-self.p+V[1], linestyle='--', color='g')
        # Latus rectum
        lr1 = V[0]+2*self.p
        lr2 = V[0]-2*self.p
        self.ax.hlines(V[1]+self.p,lr1,lr2, linestyle='-.', color='m')

        plt.show()

class Circle(ConicSection): # CIRCLE
    def __init__(self,h,k,r2):
        super().__init__()
        self.h = h
        self.k = k
        self.r2 = r2
    
    def graph_parts(self):
        C = (self.h,self.k)
        plt.contour(self.x+C[0], self.y+C[1], (self.x**2 + self.y**2), [self.r2], colors='k')
        plt.plot(C[0],C[1],'.-r')

        plt.show()


class EllipseXmaj(ConicSection): # ELLIPSE X-MAJOR
    def __init__(self,a,b,h,k):
        super().__init__()
        self.a = a
        self.b = b
        self.h = h
        self.k = k
    
    def graph_parts(self):
        C  = (self.h,self.k)
        plt.contour(self.x+C[0], self.y+C[1], (self.x**2/self.a**2 + self.y**2/self.b**2), [1], colors='k')
        #Foci
        c = np.sqrt(self.a**2 - self.b**2)
        plt.plot(C[0]+c, C[1], '.-r')
        plt.plot(C[0]-c, C[1], '.-r')
        #Center
        plt.plot(C[0],C[1],'.-r')
        #Vertices
        plt.plot(C[0]+self.a,C[1],'.-b')
        plt.plot(C[0]-self.a,C[1],'.-b')
        #Latera Recti
        lr1 = self.b**2/self.a
        lr2 = -self.b**2/self.a
        self.ax.vlines(C[0]+c, C[1]+lr1,C[1]+lr2, linestyle='--', color='g')
        self.ax.vlines(C[0]-c, C[1]+lr1,C[1]+lr2, linestyle='--', color='g')

        plt.show()


class EllipseYmaj(ConicSection): # ELLIPSE Y-MAJOR 
    def __init__(self,a,b,h,k):
        super().__init__()
        self.a = a
        self.b = b
        self.h = h
        self.k = k
    
    def graph_parts(self): 
        C  = (self.h,self.k)
        plt.contour(self.x+C[0], self.y+C[1], (self.x**2/self.a**2 + self.y**2/self.b**2), [1], colors='k')
        # Foci 
        c = np.sqrt(self.b**2 - self.a**2)
        #plt.plot(C[0], C[1]-c, '.-r', C[0], C[1]+c, '.-r')
        plt.plot(C[0], C[1]+c, '.-r')
        plt.plot(C[0], C[1]-c, '.-r')
        # Center 
        plt.plot(C[0],C[1],'.-r')
        # Vertices
        plt.plot(C[0],C[1]+self.b,'.-b')
        plt.plot(C[0],C[1]-self.b,'.-b')
        #Latera Recti
        lr1 = self.a**2/self.b
        lr2 = -self.a**2/self.b
        self.ax.hlines(C[1]+c, C[0]+lr1,C[0]+lr2,'b', linestyle='--', color='g')
        self.ax.hlines(C[1]-c, C[0]+lr1,C[0]+lr2,'b', linestyle='--', color='g')

        plt.show()


class HyperbolaXmaj(ConicSection): # HYPERBOLA X-AXIS
    def __init__(self,a,b,h,k):
        super().__init__()
        self.a = a
        self.b = b
        self.h = h
        self.k = k
    
    def graph_parts(self):
        C = (self.h,self.k)
        plt.contour(self.x+C[0], self.y+C[1], (self.x**2/self.a**2 - self.y**2/self.b**2), [1], colors='k')
        # Foci
        c = np.sqrt(self.a**2 + self.b**2)
        plt.plot(C[0]+c, C[1], '.-r', C[0]-c, C[1], '.-r')
        # Center
        plt.plot(C[0],C[1],'.-r')
        # Vertices
        plt.plot(C[0]+self.a,C[1],'.-b')
        plt.plot(C[0]-self.a,C[1],'.-b')
        #Asymptotes
        plt.plot(C[0]+self.x[0,:], C[1]+self.b/self.a*self.x[0,:], '--', alpha=.3)
        plt.plot(C[0]+self.x[0,:], C[1]-self.b/self.a*self.x[0,:], '--', alpha=.3)

        plt.show()


class HyperbolaYmaj(ConicSection): # HYPERBOLA Y-AXIS
    def __init__(self,a,b,h,k):
        super().__init__()
        self.a = a
        self.b = b
        self.h = h
        self.k = k
    
    def graph_parts(self):
        C = (self.h,self.k)
        plt.contour(self.x+C[0], self.y+C[1], (self.y**2/self.a**2 - self.x**2/self.b**2), [1], colors='k')
        # Foci
        c = np.sqrt(self.a**2 + self.b**2)
        plt.plot(C[0], C[1]+c, '.-r', C[0], C[1]-c, '.-r')
        # Center
        plt.plot(C[0],C[1],'.-r')
        # Vertices
        plt.plot(C[0],C[1]+self.a,'.-b')
        plt.plot(C[0],C[1]-self.a,'.-b')
        #Asymptotes
        plt.plot(C[0]+self.b/self.a*self.x[0,:], C[1]+self.x[0,:], '--', alpha=.3)
        plt.plot(C[0]-self.b/self.a*self.x[0,:], C[1]+self.x[0,:], '--', alpha=.3)

        plt.show()