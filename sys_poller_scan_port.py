#+------------------------------------------------------------+
# | Module Name:        Poller Lirbary - Scan by Port          |
# | Module Purpose:     Network Discovery & Hostname Resolver  |
# | Module Modifier:    John Marcellus                         |
# | Module Date:        8/31/2017                              |
# +------------------------------------------------------------

# Import modules
import threading
import time
import socket

# Import other Python
from cfg_db_mysqlconnector import *

from queue import Queue

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
print_lock = threading.Lock()

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

target = 'jmarcellus.com'
#ip = socket.gethostbyname(target)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port)
        con.close()
    except:
        pass


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()


# Create the queue and threader 
q = Queue()

# how many threads are we going to allow for
for x in range(30):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()


start = time.time()

# 100 jobs assigned.
for worker in range(1,100):
    q.put(worker)

# wait until the thread terminates.
q.join()