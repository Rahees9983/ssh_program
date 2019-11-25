#!/usr/bin/expect -f
# eval spawn ssh -oStrictHostKeyChecking=no -oCheckHostIP=no kworker1@192.168.56.132
# ip = 192.168.56.132
eval spawn ssh -oStrictHostKeyChecking=no -oCheckHostIP=no gslab@192.168.1.106
#use correct prompt
set prompt ":|#|\\\$"
expect "POSSIBLE BREAK-IN ATTEMPT!"
interact -o -nobuffer -re $prompt return
send "gslab@123\r"
interact -o -nobuffer -re $prompt return
# send "exit\r"
interact