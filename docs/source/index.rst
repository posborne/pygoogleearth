Examples
==================
Here are some quick examples to get you started!

**To Minneapolis and Back**
   >>> import pygoogleearth
   >>> ge = pygoogleearth.GoogleEarth()
   >>> orpos = ge.get_camera() # grab our original position
   >>> ge.set_camera_params(44.9773194, -093.2639111) # move to minneapolis
   >>> time.sleep(5.0) # wait five seconds
   >>> orpos['alt'] = orpos['alt'] + 150000 # zoom out some
   >>> ge.set_camera_params(**orpos) # move back with modified alt (note that params match)


:mod:`pygoogleearth`
=====================================================================
.. moduleauthor:: Paul Osborne <paul.osborne@bethel.edu>

:class:`GoogleEarth` - Google Earth Interface
**********************************************
.. currentmodule:: pygoogleearth
.. autoclass:: GoogleEarth
   :members:

:class:`AnimationController`
******************************
.. currentmodule:: pygoogleearth.animationcontroller
.. autoclass:: AnimationController
   :members:
   
:class:`CameraInfo`
******************************
.. currentmodule:: pygoogleearth.camerainfo
.. autoclass:: CameraInfo
   :members:
   
:class:`FeatureCollection`
******************************
.. currentmodule:: pygoogleearth.featurecollection
.. autoclass:: FeatureCollection
   :members:
   
:class:`SearchController`
******************************
.. currentmodule:: pygoogleearth.searchcontroller
.. autoclass:: SearchController
   :members:
   
:class:`TourController`
******************************
.. currentmodule:: pygoogleearth.viewextents
.. autoclass:: TourController
   :members:
   
:class:`ViewExtents`
******************************
.. currentmodule:: pygoogleearth.viewextents
.. autoclass:: ViewExtents
   :members: