# -*- coding: utf-8 -*-
"""
Contains all custom errors called within the pydb package.
"""

class OptionalLibraryError(Exception):
    pass

class DatabaseError(Exception):
    pass

class MultipleDoiError(Exception):
    pass
