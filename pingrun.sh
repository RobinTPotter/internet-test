#! /bin/sh
## ping 8.8.8.8 | while read pong; do echo "$(date +%s) $pong"; done >> pingtest.txt &
ping -w 299 8.8.8.8 | while read pong; do echo "$(date +%s) $(echo $pong |grep -i from| awk '{ print $7 }')"; done >> pingtest2.txt
