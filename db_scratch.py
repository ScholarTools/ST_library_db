#JAH: This is now out of date

from database import db_logging as db
from database import db_tables as tables
from database import Session

session = Session()

entries = session.query(tables.MainPaperInfo).all()

dois = [x.doi for x in entries]

# Checking if there are multiple DOIs present within MainPaperInfo table
the_set = set([x for x in dois if dois.count(x) > 1])

import pdb
pdb.set_trace()

db._end(session)
