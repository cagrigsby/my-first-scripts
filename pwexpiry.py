#!/usr/bin/env python

import datetime
import pprint
users = []
daysSince = []
epoch = datetime.datetime.utcfromtimestamp(0)
today = datetime.datetime.today()
d = today - epoch #time since epoch
d2 = d.days-30 #days since epoch from 30 days ago
for line in open("/etc/shadow","r").readlines():
        line = line.strip()
        loginInfo = line.split(":")
        users.append(loginInfo[0])  #append users to users
        daysSince.append(int(loginInfo[2])) # append int of days since epoch to daysSince

login_dict = dict(zip(users,daysSince))   #combines two lists into k,v of dictionary
for key, value in dict(login_dict).items():      #filters dictionary for accounts by age
        if value <= 18557:                  #remove system accounts by seeing they all have 18557 in their /etc/shadow line
            del login_dict[key]
        elif value >= d2:                   #remove accounts if they have changed their pw in the last 30 days
            del login_dict[key]
unKeys = list(login_dict.keys())

if len(unKeys) > 1:                 #add and to the second to last item
    unKeys.insert(-1, 'and')

def listToString(unKeys):    #convert list to string
    str1 = ", "              # seperation in string
    return (str1.join(unKeys)) #


print("These non-system users have not updated their passwords in 30 days:\n", listToString(unKeys))