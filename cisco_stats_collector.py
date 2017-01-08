#!/usr/bin/python
"""
Script Name = "cisco_stats_collector"
Description = "Simple python script to collect stats from Cisco devices using SSH.
Author      = "Arwin Reprakash | ITHITMAN"
Copyright   = "Copyright 2017, Arwin Reprakash"
Email       = "arwinr@gmail.com"
"""
# Importing modules
import psycopg2


def main():
    # Connect to the database
    get_devices = psycopg2.connect(database='postgres', user='cisco', password='cisco', host='localhost')
    # Set autocommit 
    get_devices.autocommit = True
    cursor = get_devices.cursor()
    # Execute the statement 
    cursor.execute("select hostname from cisco_stats_collector")
    psql_out = cursor.fetchall()
    #
    for device in psql_out:
        print device


if __name__ == "__main__":
    main()
