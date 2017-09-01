#+------------------------------------------------------------+
# | Module Name:        Poller Lirbary - Scan by Ping          |
# | Module Purpose:     Network Discovery & Hostname Resolver  |
# | Module Modifier:    John Marcellus                         |
# | Module Date:        8/31/2017                              |
# +------------------------------------------------------------

# Import modules
import subprocess
import ipaddress
import socket

# Import other Python
from cfg_db_mysqlconnector import *

def lookup(addr):
    try:
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return None, None, None
# Prompt the user to input a network address
net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")

# Create/Append the subnet/ip address to a TXT to later use to scan automatically
sub_file = open("subnet.txt","a")
sub_file.write(net_addr+";")
sub_file.close()

# Create the network
ip_net = ipaddress.ip_network(net_addr)

# Get all hosts on that network
all_hosts = list(ip_net.hosts())

# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

# For each IP address in the subnet, 
# run the ping command with subprocess.popen interface
for i in range(len(all_hosts)):
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    if "Destination host unreachable" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Offline")
    elif "Request timed out" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Offline")
    else:
        print(str(all_hosts[i]), "is Online")
        sub_file = open("found.txt","a")
        sub_file.write(str(all_hosts[i])+";")
        sub_file.close()
        name,alias,addresslist = lookup(str(all_hosts[i]))
        print(str(name))
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `found` (`ip`, `hostname`) VALUES (%s, %s)"
                cursor.execute(sql, (str(all_hosts[i]), str(name)))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `ip`, `hostname`  FROM `found`"
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            print(result)

connection.close()