{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

from math import pi

# Base class shape
class shape(object): # Inherit from base class 
    """Abstract base class for all ideal shape classes.

    Keyword arguments:
    dimension -- the principle dimension of the shape (default None)
    """
    def __init__(self, dimension:float=None):
        self.shape_type = self.__class__.__name__.capitalize()
        self.dim = dimension
        return
    
    def diameter(self):
        raise Exception("Unimplmented method error.")
    
    def volume(self):
        raise Exception("Unimplmented method error.")
    
    def surface(self):
        raise Exception("Unimplmented method error.")
        
    def type(self):
    """
     Returns the formatted name of the shape type. 
        
        This is set automatically, but can be overwritten by setting the attribute shape_type.
        
        :returns: the name of the class, so shapes.cube is a `Cube` shape type
        :rtype: str
      """
        return(self.shape_type)
    
class cube(shape): # Inherit from shape 
    def __init__(self, dim:float):
        super().__init__(dim)
        return
    
    def diameter(self):
        return (3 * self.dim**2)**(1/2)
    
    def volume(self):
        return self.dim**3
    
    def surface(self):
        return 6*(self.dim**2)
    
class sphere(shape): # Inherit from shape 
    def __init__(self, dim:float):
        super().__init__(dim)
        return
    
    def diameter(self):
        return self.dim*2
    
    def volume(self):
        return self.dim**3*pi*4/3
    
    def surface(self):
        return self.dim*pi*3
    
class pyramid(shape): # Inherit from shape
    
    has_mummies = True # This is for *all* regular pyramids
    
    def __init__(self, dim:float):
        super().__init__(dim)
        self.shape_type = 'Regular Pyramid'
        return
    

    def diameter(self):
        return (self.dim**2 + self.dim**2)**(1/2)
    
    def height(self):
        return (self.diameter()/2 + self.dim**2)**(1/2)
    
    def volume(self):
        return self.dim**2 * self.height() / 3
    
    def surface(self):
        return self.dim**2 + self.dim**2 * 3**(1/2)

class t_pyramid(shape): # Inherit from shape
    
    has_mummies = True # This is for *all* regular pyramids
    
    def __init__(self, dim:float):
        super().__init__(dim)
        self.shape_type = 'Triangular Pyramid'
        return
    
    def diameter(self):
        return self.dim
    
    def height(self):
        return self.diameter()*6**(1/2)/3
    
    def base_area(self):
        return self.diameter()**2/4*3**(1/2)
    
    def volume(self):
        return self.base_area() * self.height()/3
    
    def surface(self):
        return self.base_area()*4 
    
