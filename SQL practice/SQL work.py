########################
### WORKING WITH SQL ###
########################

#Make a connection with SQL:
import pyodbc

conn = pyodbc.connect(Driver={SQL Server};
                      Server='localhost,1433';
                      Database='Northwind';
                      Trusted_Connection=yes;)

