class FeatureCollection(object):
    """
    This is a collection of features.

    Represents a shallow snapshot of a collection of features. Stores references 
    to the features at the time of creation. If those features change after 
    the collection has been created, the collection still contains the modified 
    features. If a feature within the collection is deleted, the collection 
    still returns a corresponding feature of which its methods always fail 
    with E_INVALID_OR_DELETED_FEATURE.

    The underlying collection is 1-based but the python interface is
    0-based.
    """
    def __init__(self, comobject):
        """
        Initialize a FeatureCollection from the underlying comobject.
        """
        self.ge_fc = comobject
    
    def item(self, index):
        """
        Retrieves an item from the collection.

        Retrieves item with the given one-based index: the first element's 
        index is 1, and the last element's index is equal to the collection's 
        Count.
        """
        self.ge_fc.Item(index + 1)
    
    def count(self):
        """
        Number of features in the collection. 
        """
        return self.ge_fc.Count()
