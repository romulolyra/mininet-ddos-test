#!/bin/bash    
while true; do
        if wget http://10.0.0.1 -O /dev/null 2>/dev/null; then
            echo "$(date) - Accessed the web page successfully" >> ./logs/usr_log.txt
        else
            echo "$(date) - Error accessing the web page" >> ./logs/usr_log.txt
        fi
        sleep 1
    done
