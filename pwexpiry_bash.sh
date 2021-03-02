#!bin/bash

date1=$(date +%s)
epoch=86400
date2=$((date1 / epoch))
date3=$((date2 + 30))



users=$(awk -F: '($3>=1000)&&($1!="nobody"){print $1}' /etc/passwd)

OUT=$(sudo awk -F: '(($3 < $date3))' /etc/shadow | cut -d: -f1)
echo "These are the users that have not change their passwords in the last 30 days: ${OUT:369}"
