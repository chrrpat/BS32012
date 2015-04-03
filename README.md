# BS32012

This repository will act as a lab book for the project module BS32012. 


The aim of the project is to develop a range of useful skills in bioinformatics, such as Python coding, database building, and the use of collaborative tools like GitHub.

In practical terms, the aim of the project is to extract data from a Gene Expression Omnibus dataset and insert this data into an SQL database. Python code will then be produced which will enable the user to query the database. A report will be produced based on the work seen in this repository.
## File Descriptions

Here each file or folder is described. If applicable, the use of the file will be explained. 

**README.md** : This is the file you are currently reading. It contains information about the respository and the files inside.

**Project** : This contains the important files for  the project. These files include the parser script, and table building scripts.

**Misc** : This contains extra files that might be useful to see how the scripts developed. These are not necessary for use of the files in the Project folder.

##Work Diary


###Week 1 (01/03/15)
- Opened GitHub account. 
- Made practise repository and practised cloning, pushing, merging repositories. 
- Revised using XMing, Unix, and very basic Python. 

###Week 2 (08/03/15)
- Virtual Machine operational on laptop for use off campus.
- Given MySQL username and password.
- Made practise tables, linking through references.
- Downloaded a practise Gene Expression Omnibus file and transferred to virtual machine.

###Week 3 (15/03/15)
- Downloaded a different GEO file to use.
- Began completing parser and encountered some problems with the file.
- Downloaded a different GEO file which had the appropriate layout.
- Completed parser which correctly produces output files. 

###Week 4 (22/03/15)
- Began producing real tables in MySQL to hold the output files from the parser.
- Given 'deleting gaps' code (found in Misc folder) to remove some of the problems with missing entries in the output files.
- Revised python classes.
- Began working on completing the models.py template, producing mymodels.py

###Week 5 (29/03/15)
- Manually produce samples.txt and added a samples table to the MySQL script.
- Continued working on mymodels.py.
  - Model now succesfully answers basic genename, genedes queries.
- Produced mymodelstest.py to try writing additional queries.
  - Attempted to implement query to retrieve expression values with a given sampleid and ID_ref. 
    - Does not work at the moment.
- Structured and tidied repository so it will be more useful to other users.







