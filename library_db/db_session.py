#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

# Standard imports
import os

# Third party imports
import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

# Local imports
from . import db_tables as tables
from . import db_logging
from . import utils

from .utils import get_truncated_display_string as td
from .utils import get_list_class_display as cld


# These database functions can be called from a number of
# different repos. Without specifying an absolute path, a
# new database file would be created in the root directories
# of each repo that uses a Session() object.
# This method strips the filepath down to ScholarTools and
# then points it to create a papers.db file within pydb.

package_path = os.path.dirname(os.path.realpath(__file__))


class DB_Session(object):
    """
    Attributes
    ----------
    s
    save_path
    logging
    """
    def __init__(self,user_name,save_path=None):
        """
        
        Example
        -------------
        s = db.DB_Session("Jim")
        
        s = db.DB_Session("jimh@noone.nowhere.com","C:/test/")
        
        """
        
        #root_path = utils.get_save_root(['client_library'], True)
        #save_name = utils.user_name_to_file_name(self.user_name) + '.pickle'
        #self.file_path = os.path.join(root_path, save_name)
        
        
        #ST_library_db/library_db'
        if save_path is None:
            temp_path = os.path.split(package_path)[0]
            save_path = os.path.join(temp_path,"data")
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            
        temp_name = utils.user_name_to_file_name(user_name)
        db_file_name = temp_name + "_papers.db"
        
        # SQLite is used to maintain a local database
        db_path = os.path.join(save_path,db_file_name)
        dialect = 'sqlite:///'
        
        # Combine the dialect and path names to use as params for the engine
        engine_params = dialect + db_path
        
        self.save_path = db_path
        
        engine = sql.create_engine(engine_params, echo=False)
        tables.Base.metadata.create_all(engine)
        self.s = sessionmaker(bind=engine)
        
        self.logging = db_logging.DB_Logging(self.s)
    
    def __repr__(self):
        pv = ['s',        cld(self.s),
              'save_path', self.save_path,
              'logging', cld(self.logging)]
        
        return utils.property_values_to_string(pv)
    
    
    