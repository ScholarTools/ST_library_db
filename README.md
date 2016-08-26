# pydb
Database for ScholarTools implemented in python using SQLAlchemy and SQLite.

## Purpose
Pydb is a local database created and used in tandem with other ScholarTools repositories to mirror the user's main paper library. It speeds up the retrieval of data (preventing redundant or repetitive API calls to Mendeley or another library, which can be expensive) by keeping information stored locally. Data within this database persists even after moving documents in the user library to the trash to expedite accessing that information again in the future and to build a more complete set of reference relationships between papers.

