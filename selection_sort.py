"""import libraries"""
import random


class selection_sort:
    """This is a selection sort algorithm"""
    def __init__(self, w, x, y, z):
        """to generate random list"""
        self.__w = w
        self.__x = x
        self.__y = y
        self.__z = z
        random_list = []
        for i in range(w,x):
            n = random.randint(y,z)
            random_list.append(n)
        print(random_list)

    @property
    def w(self):
        """assign w to w"""
        return self.__w

    @w.setter
    def w(self, value):
        """set conditions for w"""
        if type(value) != int:
            raise TypeError("Range can only be specified by an integer.")
        self.__w = value
    
    @property
    def x(self):
        """assign x to x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set conditions for x"""
        if type(value) != int:
            raise TypeError("Range can only be specified by an integer.")
        self.__x = value
    
    @property
    def y(self):
        """assign y to y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set conditions for y"""
        if type(value) != int:
            raise TypeError("Range can only be specified by an integer.")
        self.__y = value
    
    @property
    def z(self):
        """assign z to z"""
        return self.__z

    @y.setter
    def z(self, value):
        """set conditions for y"""
        if type(value) != int:
            raise TypeError("Range can only be specified by an integer.")
        self.__z = value
    