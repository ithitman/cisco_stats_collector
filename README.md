# cisco_stats_collector
- Author: Arwin Reprakash
- Email: arwinr@gmail.com
- Website: http://ithitman.com

## Table of contents

- [Summary](#summary)
- [Install Instructions](#Install-Instructions)
	- [Overview](#Overview)
	- [Postgres Installation](#Postgres-Installation)
	- [Table Creation](#Table-Creation)
	- [Inserting Devices into the Table](#Inserting-Devices-into-the-Table)
	- [Editing Script Variables](#Editing-Script-Variables)
- [Example](#Example)
- [License](#License)

## Summary
Simple python script to collect stats from Cisco devices using SSH. Read from a database for the hostnames of the Cisco devices and parallel process multiple devices at the same time and input the results into a database back-end.

## Install Instructions
### Overview
- We will install a database backend (postgres in this instruction).
- We will create a table that will house our devices and information regarding each device.
- We will create a table that will house our results from the devices. 
- We will edit some key variables that are required by script.

### Postgres Installation

This is a plain vanilla installation of postgres on fedora. Fine tuning postgres or installing it for other distributions is out of the scope for this document. Please consult appropriate manuals. 

`# su dnf install postgresql-server.x86_64 -y`

`# su postgresql-setup --initdb`

`# su systemctl start postgresql.service`

`# su systemctl enable postgresql.service`

### Table Creation

`# su postgres`

`# psql`

`postgres=# CREATE ROLE cisco WITH SUPERUSER LOGIN PASSWORD 'cisco';`

`postgres=# create table cisco_stats_collector (`<br />
`ID SERIAL PRIMARY KEY NOT NULL,` <br />
`hostname char(100),` <br />
`username char(100),` <br />
`password char(100),` <br />
`comments char(1000)` <br />
`);` <br />

### Inserting Devices into the Table

`psql -h localhost -U cisco postgres` 

`postgres=# INSERT INTO cisco_stats_collector (hostname,username,password,comments) VALUES ('arwin-router-1','user','pass','Cisco Nexus 3548');`

If you have any issues connecting to the database make sure the permissions are correct in /var/lib/pgsql/data/pg_hba.conf and it should look like this.
```
local   all             all                                     trust
host    all             all             127.0.0.1/32            trust
host    all             all             ::1/128                 trust
```
Again probably not the most secure but this should get you going. 

### Editing Variables in the cisco_stats_collector.py

## Example

After you follow the install instructions this is how to execute the script. 

## License

This project is released under GPLv3 license. Please see the included License file for more information.

Copyright © 2017 - Arwin Reprakash | ITHITMAN.com
