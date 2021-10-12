# run this in cmd or Powershell to install 
# python -m pip install mysql-connector-python

import sys
sys.path.insert(0, './mod')
import Logger as audit
import mysql.connector

audit.setup_logging("./logs/")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="FrustrateWetMuppet21",
  database="sakila"
)

print(mydb)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sakila.customer;")

for x in mycursor:
#   print(x[3],x[2],x[4])
  audit.logging.info("Surname:" + x[3] + " \t\tFirstName:" + x[2] + " \t\temail:" + x[4])

# print(mycursor.rowcount)
audit.logging.debug("Query returned " + str(mycursor.rowcount) + " rows")
audit.logging.error("test")
