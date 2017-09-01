#+------------------------------------------------------------+
# | Module Name:        Connect Mysql Database & Create JSON   |
# | Module Purpose:     Write Data from Maria/MySQL            |
# | Module Modifier:    John Marcellus                         |
# | Module Date:        8/31/2017                              |                                     
# +------------------------------------------------------------

# Import modules
import pymysql.cursors
import json
import collections

# Definitions

#------------------------------------------------------------------------------------------------------------------------------------------------------#
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='pythonuser',
                             password='pythonuser',
                             db='db_python',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM found"
        cursor.execute(sql)
        #Convert query to objects of key-value pairs
        j = json.dumps(cursor.fetchall())
        objects_file = 'network_objects_found.json'
        f = open(objects_file,'w')
        f.write(j)
        print(j)
        f.close
finally:
    connection.close()