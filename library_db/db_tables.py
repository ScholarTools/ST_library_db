"""
Tables
-----------------
ref_mapping
    main_paper_id
    ref_paper_id
    ordering
main_paper_info
authors
references
linked_notes



DocumentTags: Document ID and string

TODO: Include MESH


"""

# Third party imports
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RefMapping(Base):
    """
    This table keeps track of paper references.
    Both 'original_paper' and 'ref_paper' are unique identifying integers. See
    the References table for mapping to information.
    The 'ordering' column keeps track of reference order within a paper.
    
    So we might have:
        
    Jim et al. citing Chris et al. as #2
    
    Jim et al. - main_paper_id
    Chris et al. - ref_paper_id
    #2 - ordering
    
    """
    __tablename__ = 'ref_mapping'

    id = sql.Column(sql.INTEGER, primary_key=True)
    main_paper_id = sql.Column(sql.INTEGER, sql.ForeignKey('main_paper_info.id'))
    ref_paper_id = sql.Column(sql.INTEGER, sql.ForeignKey('references.id'))
    ordering = sql.Column(sql.INTEGER)

    def __repr__(self):
        return "<RefMapping(original_paper='%d', ref_paper='%d')>" % (self.main_paper_id, self.ref_paper_id)


class MainPaperInfo(Base):
    """
    """
    
    __tablename__ = 'main_paper_info'

    id = sql.Column(sql.INTEGER, primary_key=True)
    
    #This is the primary key in the References DB - if it exists
    ref_table_id = sql.Column(sql.INTEGER)

    #TODO: Document type
    #- journal article
    #- book chapter
    #- other

    #Info about the document
    #--------------------------------------------
    abstract = sql.Column(sql.VARCHAR)
    date = sql.Column(sql.VARCHAR)
    keywords = sql.Column(sql.VARCHAR)
    pages = sql.Column(sql.VARCHAR)
    publication = sql.Column(sql.VARCHAR)
    title = sql.Column(sql.VARCHAR)
    volume = sql.Column(sql.VARCHAR)
    year = sql.Column(sql.VARCHAR)
    
    
    #What is this url?
    url = sql.Column(sql.VARCHAR)
    
    
    #Link to pdf to download
    pdf_link = sql.Column(sql.VARCHAR)
    
    #???What about supplemental info?
    #???What about a html link
    
    #Internal Meta
    #--------------------------------
    #This can be used to allow the adding of documents that are not in the 
    #library but that we know about ...
    in_lib = sql.Column(sql.INTEGER)
    
    #lib_id = 
    
    #??????? - I think this should instead be the url of the document ...
    #Although we get this from the DOI so I'm inclined to remove it
    #scraper_obj = sql.Column(sql.VARCHAR)

    #????? - this looks like it is passed to the constructor ...
    #I think this indicates that the library thing has an element
    has_file = sql.Column(sql.INTEGER)
    
    valid_doi = sql.Column(sql.INTEGER)
    #Verification of what??? the DOI?????
    verification_timestamp = sql.Column(sql.TIMESTAMP)

    #Document IDs ----------------------------
    pii = sql.Column(sql.VARCHAR)
    eid = sql.Column(sql.VARCHAR)
    pmid = sql.Column(sql.VARCHAR)
    doi = sql.Column(sql.VARCHAR)
    doi_prefix = sql.Column(sql.VARCHAR)
    #TODO: This is ambiguous because we could have 
    #e_issn 
    #p_issn
    #issn
    #issn_l
    issn = sql.Column(sql.VARCHAR)
    
    #User Info
    #------------------------------------
    notes = sql.Column(sql.VARCHAR)
    #TODO: tags ...
    
    
    #JAH: Why isn't this everything?????
    # This is used for comparisons with updated information.
    fields = ['doi', 'doi_prefix', 'title', 'publication', 'date',
              'year', 'volume', 'issue', 'pages', 'keywords', 'abstract',
              'url', 'pdf_link', 'scraper_obj', 'pii', 'eid', 'notes',
              'pmid', 'issn', 'authors']

    def __repr__(self):
        return u'' + \
        '      title: %s\n' % self.title + \
        '   keywords: %s\n' % self.keywords + \
        'publication: %s\n' % self.publication + \
        '       date: %s\n' % self.date + \
        '        year %s\n' % self.year + \
        '     volume: %s\n' % self.volume + \
        '      issue: %s\n' % self.issue + \
        '      pages: %s\n' % self.pages + \
        '        doi: %s\n' % self.doi + \
        '         url %s\n' % self.url + \
        '    pdf_link %s\n' % self.pdf_link


class Authors(Base):
    """
    affiliations
    email
    main_paper_id
    name
    """
    __tablename__ = 'authors'

    id = sql.Column(sql.INTEGER, primary_key=True)
    main_paper_id = sql.Column(sql.INTEGER, sql.ForeignKey('main_paper_info.id'))
    name = sql.Column(sql.VARCHAR)
    affiliations = sql.Column(sql.VARCHAR)
    email = sql.Column(sql.VARCHAR)

    # This is used for comparisons with updated information.
    fields = ['name', 'affiliations', 'email']

    def __repr__(self):
        return u'' + \
        '        name: %s\n' % self.name + \
        'affiliations: %s\n' % self.affiliations + \
        '       email: %s\n' % self.email


class References(Base):
    __tablename__ = 'references'
    
    
    
    #For references
    #create as a foreign key?
    #
    #Props
    #-----------
    #refs
    #refs_fetch_date
    #refs_source_type
    #- url
    #- manual entry

    id = sql.Column(sql.INTEGER, primary_key=True)
    main_table_id = sql.Column(sql.INTEGER)

    # Initialize standard reference information
    ref_id = sql.Column(sql.INTEGER)
    title = sql.Column(sql.VARCHAR)
    authors = sql.Column(sql.VARCHAR)
    publication = sql.Column(sql.VARCHAR)
    volume = sql.Column(sql.VARCHAR)
    issue = sql.Column(sql.VARCHAR)
    series = sql.Column(sql.VARCHAR)
    date = sql.Column(sql.VARCHAR)
    year = sql.Column(sql.VARCHAR)
    pages = sql.Column(sql.VARCHAR)
    doi = sql.Column(sql.VARCHAR)
    pii = sql.Column(sql.VARCHAR)
    citation = sql.Column(sql.VARCHAR)

    # Initialize all possible external links
    crossref = sql.Column(sql.VARCHAR)
    pubmed = sql.Column(sql.VARCHAR)
    pubmed_central = sql.Column(sql.VARCHAR)
    cas = sql.Column(sql.VARCHAR)
    isi = sql.Column(sql.VARCHAR)
    ads = sql.Column(sql.VARCHAR)
    scopus_link = sql.Column(sql.VARCHAR)
    pdf_link = sql.Column(sql.VARCHAR)
    
    #This could be outdated, I don't think we'll use this for now
    #scopus_cite_count = sql.Column(sql.VARCHAR)
    
    #???? What is this????
    aps_full_text = sql.Column(sql.VARCHAR)

    # Make a timestamp
    timestamp = sql.Column(sql.TIMESTAMP)

    def __repr__(self):
        return u'' + \
        '     ref_id: %s\n' % self.ref_id + \
        '      title: %s\n' % self.title + \
        '    authors: %s\n' % self.authors + \
        'publication: %s\n' % self.publication + \
        '     volume: %s\n' % self.volume + \
        '      issue: %s\n' % self.issue + \
        '     series: %s\n' % self.series + \
        '       date: %s\n' % self.date + \
        '      pages: %s\n' % self.pages + \
        '        doi: %s\n' % self.doi + \
        '        pii: %s\n' % self.pii


class LinkedNotes(Base):
    __tablename__ = "linked_notes"

    id = sql.Column(sql.INTEGER, primary_key=True)
    main_paper_id = sql.Column(sql.INTEGER, sql.ForeignKey('main_paper_info.id'))
    ref_paper_id = sql.Column(sql.INTEGER, sql.ForeignKey('references.id'))
    notes = sql.Column(sql.VARCHAR)

