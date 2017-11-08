
import os
from .version import __version__


from .chemkin import *
from .flux import *
from .ignition import *
from .sensitivity import *
# from .html import *

def get_include():
    """
    Return the PyChemkin include directory.
    """
    return os.path.dirname(os.path.abspath(__file__))
