from pygoogleearth.kml.kmlabstract import KMLObject

class KMLTimePrimitive(KMLObject):
    """This is an abstract element and cannot be used directly in a KML file. 
    
    This element is extended by the <TimeSpan> and <TimeStamp> elements.
    """
    
class KMLTimeSpan(KMLTimePrimitive):
    """Represents an extent in time bounded by begin and end dateTimes.
        
    If <begin> or <end> is missing, then that end of the period is 
    unbounded (see Example below).
    The dateTime is defined according to XML Schema time (see XML    
    Schema Part 2: Datatypes Second Edition). The value can be 
    expressed as yyyy-mm-ddThh:mm:sszzzzzz, where T is the separator 
    between the date and the time, and the time zone is either Z 
    (for UTC) or zzzzzz, which represents +/-hh:mm in relation to UTC. 
    Additionally, the value can be expressed as a date only. 
    See <TimeStamp> for examples.
    """
    
class KMLTimeStamp(KMLTimePrimitive):
    """Represents a single moment in time. This is a simple element 
    and contains no children. Its value is a dateTime, specified in 
    XML time (see XML Schema Part 2: Datatypes Second Edition). The 
    precision of the TimeStamp is dictated by the dateTime value in 
    the <when> element."""