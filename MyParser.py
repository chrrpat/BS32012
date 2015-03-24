# -*- coding: iso-8859-1 -*-
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

genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')

#defines which columns are to go in each output file. For samples it is the 3rd header until the gene title header and they will be separated by '\t'
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

def buildrow(row, fields):
   '''Docstring'''
   newrow=[]
   for f in fields:
      newrow.append(row[int(colnames[f])])
   return "\t".join(newrow)+"\n"


#creates the rows for the expression file, is slightly different because for each probe and experiment there are several gene expression values.
def build_expression(row, samples):
   '''Docstring'''
   exprrows=[]
   for s in samples:
      newrow=[s,]
      newrow.append(row[int(colnames['ID_REF'])])
      newrow.append(row[int(colnames[s])])
      exprrows.append("\t".join(newrow))
   return "\n".join(exprrows)+"\n"

#initialise a counter to count how many probe rows were processed.    
#writes the data to the files 


rows=0    
for line in fh.readlines():
   try:
      if line[0]=='!':
         continue
      row=line.strip().split('\t')
      genefile.write(buildrow(row, genefields))
      probefile.write(buildrow(row, probefields))
      expressionfile.write(build_expression(row, samples))	
      rows=rows+1
   except:
      pass




genefile.close()
probefile.close()
expressionfile.close()

print '%s rows processed'%rows



