class ViewExtents(object):
    """
    :summary: Object representing view extents
    
    A :class:`ViewExtents` object has the following read-only fields:
       * north
       * south
       * east
       * west
       
    Units for these are specified in degrees as a floating point number.
    
    .. note::
    The properties defined in view extents are read-only.  Since
    :class:`GoogleEarth` does not take a :class:`ViewExtents` as
    a parameter, this is a non-issue.
    """
    
    def __init__(self, comobject):
        """Initialize view extents from the provided com object"""
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
