class ViewExtents(object):
    
    def __init__(self, comobject):
        self.ge_ve = comobject
    
    def __getattr__(self, name):
        if name == 'north':
            return self.ge_ve.North
        elif name == 'south':
            return self.ge_ve.South
        elif name == 'east':
            return self.ge_ve.East
        elif name == 'west':
            return self.ge_ve.West
        else:
            raise AttributeError
