# -*- coding: iso-8859-1 -*-
#opens the raw GEO file, writes 4 text files which can then be used to put into SQL tables
#My filled in parser template
# step 1. open the data file

infile = "GDS5088.txt"
fh = open(infile)
line = fh.readline()
#step 2. read the first line and then read more lines while the line doesn't match a specific pattern
while line[:19] != "!dataset_table_begi":
   line = fh.readline()

header= fh.readline().strip()

#capture the column names

colnames={}
index=0
for title in header.split('\t'):
   colnames[title]=index
   print '%s\t%s'%(title,index)
   index=index+1

#open our output files, one per table.

genefile=open('genesNEW.txt', 'w')
expressionfile=open('expressionNEW.txt','w')
probefile=open('probesNEW.txt', 'w')

#defines which columns are to go in each output file. For samples it is the 3rd header until the gene title header and they will be separated by '\t'
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

def buildrow(row, fields):
   '''This creates a tab separated list of values, according to the columns listed in fields
   row: a list of values
   fields: a list of columns. Only the values in row corresponding to the columns in fields are output
   returns: A string that is a tab separated list of values terminated with a newline
   '''
   newrow=[]
   for f in fields:
      newrow.append(row[int(colnames[f])])
   return "\t".join(newrow)+"\n"


#creates the rows for the expression file, is slightly different because for each probe and experiment there are several gene expression values.
def build_expression(row, samples):
   '''Builds tab separated rows for expression data. For each of the sameples listed
   it generates a line with the probe id, sample id and expression value.
   row: a list of values
   samples: a list of column headings corresponding to the samples
   '''
   exprrows=[]
   for s in samples:
      newrow=[s,]
      newrow.append(row[int(colnames['ID_REF'])])
      newrow.append(row[int(colnames[s])])
      exprrows.append("\t".join(newrow))
   return "\n".join(exprrows)+"\n"

#Counter which counts how many probe rows were processed.    
#writes the data to the files 


rows=0    
for line in fh.readlines():
   try:
      if line[0]=='!':
         continue
      row=line.strip().split('\t')
      if row[colnames['Gene ID']]=='':
          continue
      genefile.write(buildrow(row, genefields))
      probefile.write(buildrow(row, probefields))
      expressionfile.write(build_expression(row, samples))	
      rows=rows+1
   except:
      pass


#closing the written files


genefile.close()
probefile.close()
expressionfile.close()

#prints a message to show how many rows have been processed

print '%s rows processed'%rows



