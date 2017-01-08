# cisco_stats_collector
- Author: Arwin Reprakash
- Email: arwinr@gmail.com
- Website: http://ithitman.com

## Table of contents

- [Summary](#summary)
- [Prerequisites](#prerequisites)
- [Install Instructions](#install-instructions)
- [Licensing](#licensing)

# Summary
Simple python script to collect stats from Cisco devices using SSH. Read from a database for the hostnames of the Cisco devices and parallel process multiple devices at the same time and input the results into a database back-end.

# Prerequisites

# Install Instructions
1. Overview
* We will install a database backend (postgres in this instruction).
* We will create a table that will house our device list and information regarding the device.
* We will edit some key variables that are required by script.

2. Postgres Installation
This is a plain vanilla installation of postgres for fedora. Fine tuning postgres or installing it for other distributions is out of the scope for this document.

`su dnf install postgresql-server.x86_64 -y`
`su postgresql-setup --initdb`
`su systemctl start postgresql.service`
`su systemctl enable postgresql.service`

3. Table Creation
4. Inserting Devices into the Table
5. Editing Variables in the cisco_stats_collector.py
6. Example

# Licensing 
This project is released under GPLv3 license. Please see the included License file for more information. 
