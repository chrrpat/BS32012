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

    def __init__(self,geneid):
        '''Init method for Gene'''
        self.gene_id=geneid
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
    #fill in the blanks yourself
        cursor.execute(probesql,(geneid,))
        #query database
        #get result and populate the class fields.
       


        for result in cursor.fetchall():
              self.probelist.append(result[0])

    def get_expression(self,experiment):
        '''Retrieve expression values for a given experiment for this gene'''
        self.experiment=None