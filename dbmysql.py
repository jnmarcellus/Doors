#+------------------------------------------------------------+
# | Module Name:        Connect Mysql Database                 |
# | Module Purpose:     Write Data to MySQL Databases          |
# | Module Modifier:    John Marcellus                         |
# | Module Date:        8/31/2017                              |                                     
# +------------------------------------------------------------

# Import modules
import pymysql.cursors
import json
import collections
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

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
        # Create a new record
        sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT 'id, email, password' FROM 'users' WHERE 'email'=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        #Convert query to objects of key-value pairs
        rows = cursor.fetchall()
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['ID'] = row.ID
            d['FirstName'] = row.FirstName
            d['LastName'] = row.LastName
            d['Street'] = row.Street
            d['City'] = row.City
            d['ST'] = row.ST
            d['Zip'] = row.Zip
            objects_list.append(d)#

        j = json.dumps(objects_list)
        objects_file = 'student_objects.js'
        f = open(objects_file,'w')
        print >> f, j
finally:
    connection.close()