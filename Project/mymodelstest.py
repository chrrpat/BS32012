# -*- coding: iso-8859-1 -*-
'''Classes to represent our gene expression objects'''
#This is a script for a database interacting class to represent a gene. more can be added to the script for further queries
# This allows connection to a MySQL database server from Python
import MySQLdb


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
    # Preparing a cursor
    def cursor(self):
        return DBHandler.connection.cursor()

class Gene():
    '''A class that describes an individual gene'''
    gene_des=''
    gene_name=''
    gene_id=''
    probelist=[]
    sample_id=''
    ID__ref=''
    expressionvalue=[]
    

    def __init__(self,geneid):
        '''Init method for Gene'''
        self.gene_id=geneid
        db=DBHandler()
        cursor=db.cursor()
        sql='select genename,genedes from gene where geneid=%s'
        #Executing the SQL query
        cursor.execute(sql,(geneid,))
        #Fetches the single relevant row
        result=cursor.fetchone()
        self.genename    =result[0]
        self.genedes=result[1]
        #Fetching the probes
        probesql='select ID_ref from probes where geneid=%s'
        #Executing the SQL query
        cursor.execute(probesql,(geneid,))
        
        #Get result and populate the class fields.
       


        for result in cursor.fetchall():
              self.probelist.append(result[0])
              #Results in list of relevant probes

    def get_expression(self,sampleid):
        '''If completed this would retrieve expression values for a given experiment for this gene
        Does not currently work.
        '''
        self.sample_id=sampleid
        self.ID__ref=ID_ref
        db=DBHandler()
        cursor=db.cursor()
        expressionsql='SELECT expression FROM expression WHERE sampleid=%s and ID_ref=%s'
        cursor.execute(expressionsql, (sampleid,) (ID_ref)) 
        for result in cursor.fetchall():
             self.expressionvalue.append(result[0])
            #Attempted to implement suggestions by David Martin but still needs more work before functioning.
            #Use of mygene.expressionvalue will always result in '[]'. 
            
