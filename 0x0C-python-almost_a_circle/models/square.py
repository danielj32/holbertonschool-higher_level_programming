#!/usr/bin/python3
"""define a class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ construct """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size """
        return self.width

    @size.setter
    def size(self, val):
        """ setter """
        self.width = val
        self.height = val

    def __str__(self):
        """ Print the method """
        st = "[Square] ({}) {}/{} - {}"
        st = st.format(self.id, self.x, self.y, self.width)
        return st

    def update(self, *args, **kwargs):
        """ Updating  the Attributes """
        atr = ['id', 'size', 'x', 'y']
        if args and 0 < len(args) <= 4:
            for i, arg in enumerate(args):
                if i == 0:
                    super().update(arg)
                else:
                    self.__setattr__(atr[i], arg)
        elif kwargs and 0 < len(kwargs) <= 4:
            for k, v in kwargs.items():
                if k == 'id':
                    super().update(id=v)
                elif k in atr:
                    self.__setattr__(k, v)

    def to_dictionary(self):
        """ Return Repr """
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y}
