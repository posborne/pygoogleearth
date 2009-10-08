from setuptools import setup, find_packages

long_description = """\
NOTE: This library is not an official google library!  It is a pythonic
wrapper around the COM32 API provided by Google.

PyGoogleEarth is a pythonic wrapper around the Google Earth
COM Interface documented here: http://earth.google.com/comapi/.  It
maps the functionality provided by the API to python objects and reduces
the barrier-to-entry put up by using win32com.  In addition to wrapping
the COM API it also provides some nice additions which make it easier
to manipulate Google Earth from python.
"""

setup(
      name = "pygoogleearth",
      version = "0.0.2",
      packages = ['pygoogleearth'],
      install_requires = ['pywin32'],
      
      # metadata
      author = "Paul Osborne",
      author_email = "paul-osborne@bethel.edu",
      description = "Python wrapper for Google Earth COM API",
      long_description = long_description,
      license = "MIT",
      keywords = "google earth com api googleearth",
      url = "http://pygoogleearth.googlecode.com/",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Win32 (MS Windows)',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Multimedia :: Graphics :: Presentation',
          'Topic :: Scientific/Engineering :: GIS',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Software Development :: Libraries',],
)

#===============================================================================
# NOTE TO SELF: To Deploy...
# python setup.py sdist bdist_egg bdist_wininst register upload
#===============================================================================