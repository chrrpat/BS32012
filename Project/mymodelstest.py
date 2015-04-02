# -*- coding: iso-8859-1 -*-
'''Classes to represent our gene expression objects'''

import MySQLdb
#Incomplete outline script for a database interacting class to represent a gene.

class DBHandler():
    '''The static database connection - avoids overuse of resources'''
    connection=None
    dbname='ctpaterson'
    dbuser='ctpaterson'
    dbpassword='ieF62lxl'
    
    def __init__(self):
        if DBHandler.connection == None:
            DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, \
user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

    def cursor(self):
        return DBHandler.connection.cursor()

class Gene():
    '''A class that describes an individual gene'''
    gene_des=''
    gene_name=''
    gene_id=''
    probelist=[]
    expressionvalue=''

    def __init__(self,geneid):
        '''Init method for Gene'''
        ####self.gene_id=geneid
        db=DBHandler()
        cursor=db.cursor()
        sql='select genename,genedes from gene where geneid=%s'
        cursor.execute(sql,(geneid,))
        #query database
        #get result and populate the class fields.
        result=cursor.fetchone()
        self.genename    =result[0]
        self.genedes=result[1]
        #now fetch the probes..
        probesql='select ID_ref from probes where geneid=%s'
        cursor.execute(probesql,(geneid,))
        #query database
        #get result and populate the class fields.
       


        for result in cursor.fetchall():
              self.probelist.append(result[0])

    def get_expression(self,sampleid):
        '''Retrieve expression values for a given experiment for this gene'''
        
        self.sampleid=sampleid
        db=DBHandler()
        cursor=db.cursor()
        expressionsql='SELECT expression FROM expression WHERE sampleid=%s and ID_ref=%s'
        cursor.execute(expressionsql, (sampleid,)) #DMAM Your query has two placeholders, one each for sampleid and ID_ref. 
        #you have only the sample id in the list of values.  
        for result in cursor.fetchone():
             self.expressionvalue =result[0]
        #DMAM This will return the expression value for the first probe in the list. 
        # A gene may have more than one probe associated with it. 
        #It retrieves the value(s) from the database and stores them in an instance variable. 
        #This is fine but will be overwritten with the next call on a different sampleid for the same gene
