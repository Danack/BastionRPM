#!/bin/bash

intahwebzGroup="www-data"

groupadd -r $intahwebzGroup
useradd --key UMASK=0022 -m -g $intahwebzGroup intahwebz

# echo "intahwebz" | passwd --stdin intahwebz

#nginx requires the directory tree to be executable
#chmod +x /home/intahwebz/

