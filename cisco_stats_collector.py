#!/usr/bin/python
"""
Script Name = "cisco_stats_collector"
Description = "Simple python script to collect stats from Cisco devices using SSH.
License     = GPLv3 :: Check included license file for more information
Author      = "Arwin Reprakash | ITHITMAN"
Copyright   = "Copyright 2017, Arwin Reprakash"
Email       = "arwinr@gmail.com"
Website     = "http://ithitman.com"
"""
# Importing modules
import psycopg2
import paramiko
import threading
from Queue import Queue
import time
import re


# Define variables
num_of_parallel_jobs = 10
sql_username = 'cisco'
sql_password = 'cisco'
sql_database = 'postgres'
sql_host = 'localhost'


# Function to collect the stats and print
def cisco_stats_collection(cisco_devices):
    cisco_command = "show interface status"
    try:
        # parse the variables that were picked up from the queue
        hostname = re.search('(?<=hostname:)(.*?\s)', cisco_devices)
        hostname = re.sub(r'\s', '', hostname.group(0))
        username = re.search('(?<=username:)(.*?\s)', cisco_devices)
        username = re.sub(r'\s', '', username.group(0))
        password = re.search('(?<=password:)(.*?\s)', cisco_devices)
        password = re.sub(r'\s', '', password.group(0))

    except:
        print "Error on regex parsing on cisco_stats_collection function"
        return

    try:
        # Connect to the device
        ssh_connection = paramiko.SSHClient()
        ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connection.connect(hostname, username=username, password=password, timeout=10)
        stdin, stdout, stderr = ssh_connection.exec_command(cisco_command)
        stdin.flush()
        # Get the output from the switch
        ssh_connection_output = stdout.readlines()
        # For each line in the output loop through and parse the data
        for each_line in ssh_connection_output:
            single_row = re.split('\s+', each_line)
            if single_row:
                # If the line begins with a letter. This can be edited depending on the output you are getting back.
                if re.search(r'^[a-zA-Z].*', each_line):
                    intf_name = single_row[0]
                    intf_description = single_row[1]
                    intf_status = single_row[2]
                    # Instead of printing you can insert into database table, send it to grafana for graphing or whatever you want here. I am printing just as an example
                    print "On device {} interface name is {} description is {} with status {}".format(hostname, intf_name, intf_description, intf_status)

    except paramiko.SSHException, e:
        print e
        print "Error on SSH on {}".format(hostname)
        return


# Function to take the member in the queue.
def threader():
    while True:
        # Get a device from the cisco_queue
        cisco_devices = cisco_queue.get()
        # Run the job
        cisco_stats_collection(cisco_devices)
        # completed with the job
        cisco_queue.task_done()


# Create the queue and the threader
cisco_queue = Queue()

# Record start time of the first job
start_time = time.time()

# Run jobs in parallel
for x in range(num_of_parallel_jobs):
    t = threading.Thread(target=threader)

    # classifying as a daemon, so threads will terminate when the main program terminates
    t.daemon = True

    # start
    t.start()


def main():
    # Connect to the database
    get_devices = psycopg2.connect(host=sql_host, database=sql_database, user=sql_username, password=sql_password)
    # Set autocommit 
    get_devices.autocommit = True
    cursor = get_devices.cursor()
    # Execute the statement to get the list of devices
    cursor.execute("select hostname, username, password from cisco_stats_collector")
    psql_out = cursor.fetchall()
    # Loop through the device list and add to the queue
    for device in psql_out:
        hostname = device[0]
        username = device[1]
        password = device[2]
        pass_args = "hostname:{} username:{} password:{} ".format(hostname, username, password)
        cisco_queue.put(pass_args)

    """
    Instead of connecting to a database to populate the list of devices you can also have a list of devices in a txt
    file and load it into the queue using a for or while loop if that is easier.
    """

    # Wait till all threads to be completed before exiting
    cisco_queue.join()
    print('Entire job timespan:', time.time() - start_time)


if __name__ == "__main__":
    main()
