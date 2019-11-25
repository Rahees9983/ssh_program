#!/bin/bash
# spawn script.sh
# expect "Are you sure you want to continue connecting (yes/no)?"
# send "yes"
# ssh gslab@192.168.1.106
/usr/bin/expect -c 'expect "\n" { eval spawn ssh -oStrictHostKeyChecking=no -oCheckHostIP=no gslab@192.168.1.106; interact }'
sshpass -p gslab@123 ssh user@192.168.1.106