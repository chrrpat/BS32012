#Project files

Here is a description of the files found in this folder, and if necessary, how to use them. 

##File Descriptions



**GDS5088.txt** : This is the file which contains the experimental data which will sorted and placed into a database. The file contains information about gene expression at different stages of pregnancy in a number of different subjects. 

**MyParser.py** : This contains script for a parser which will open the above gene expression file, select appropriate information and write a new text file with the data tabulated. A template for this file was provided by David Martin which I completed. 

**expressionNEW.txt**, **genesNEW.txt**, **probesNEW.txt** : These are text files produced by the parser script. These are text files containing information in tabulated columns. These files can then be used to produce tables using MySQL script. Below the column headers for each of these three files are described.

**expressionNEW.txt** : The three columns are sampleid, ID_ref, and expression. These are the number assigned to the sample. the number assigned to the probe and the expression value, respectively. 

**genesNEW.txt** : The three columns are geneid, genename, and genedes. These are the number assigned to the gene, the name of the gene and a short description of the gene, respectively. 

**probesNEW.txt** : The two columns are ID_ref and geneid. These are the number assigned to the probe, and the number assigned to the gene respectively. 


**samples.txt** : This is also a text file containing information in tabulated columns. It was constructed manually using the replace function. The parser was not used for two reasons- there was less data to look through, and the columns were more difficult to pick out using code. The three columns are sampleid, subject and trimester. 

**tablestuff** : This script builds tables from each of the 4 text files above. References are also used to link the tables. A template for this file was provided by David Martin which I completed. 

**mymodels.py** : This script allows the user to provide a Gene ID, and use this to query the database for the corresponding gene name, description and associated probes. Further queries can be added with more code. This A template for this file was provided by David Martin which I completed. 

**mymodelstest.py** : This is an altered version of the mymodels.py file. It has an attempt to add the ability to find the expression values with a given Sample ID and ID_ref.

