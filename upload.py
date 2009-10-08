import sys
import subprocess

if sys.platform == 'win32':
    print 'Running on Windows'
    PYTHON24 = r'C:\Python24\python.exe'
    PYTHON25 = r'C:\Python25\python.exe'
    PYTHON26 = r'C:\Python26\python.exe'
else: # cygwin?
    print 'Running under cygwin'
    PYTHON24 = r'/cygdrive/c/Python24/python.exe'
    PYTHON25 = r'/cygdrive/c/Python25/python.exe'
    PYTHON26 = r'/cygdrive/c/Python26/python.exe'

if __name__ == '__main__':
    print 'Creating Source Distribution'
    subprocess.call([PYTHON26, 'setup.py', 'sdist', 'upload']) # source distribution
    subprocess.call([PYTHON26, 'setup.py', 'bdist', '--formats=wininst,egg,zip'])
