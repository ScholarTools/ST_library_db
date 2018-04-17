#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:22:08 2018

@author: jim
"""

from .errors import OptionalLibraryError

#from pypub.paper_info import PaperInfo
#from pypub.scrapers.base_objects import *

class MissingModule(object):
    """
    This class throws an error upon trying to get an attribute.
    
    The idea is that if you import a missing module, and then try and get a
    class or function from this missing module (i.e. actually use the import
    calls) then an error is thrown.
    """
    def __init__(self,msg):
        self.msg = msg
        
    def __getattr__(self, name):
        #do we really want getattribute instead?
        #=> I think getattribute is more comprehensive
        raise OptionalLibraryError(self.msg)
        
try:
    import pypub.publishers.pub_objects as pub_objects
except ImportError:
    pub_objects = MissingModule('The method called requires the library "pypub" from the Scholar Tools Github repo')

try:
    from pypub.paper_info import PaperInfo
except ImportError:
    PaperInfo = MissingModule('The method called requires the library "pypub" from the Scholar Tools Github repo')

try:
    from pypub.scrapers import base_objects
except ImportError:
    base_objects = MissingModule('The method called requires the library "pypub" from the Scholar Tools Github repo')
        
