
import requests

### Donwnload new (updated by SCOC) blacklist and put it to file 'blacklist_ip_new'
url = "http://kickself.com/wp-content/uploads/2019/01/CSOC_BLOCKLIST_IP.txt"
req=requests.get(url,allow_redirects=True)

with open ("blacklist_ip_new.txt","w") as blacklist_ip_new:
    blacklist_ip_new.write(req.text)

### Here we compare new and current blacklist, and new entries to the current file and to the IPS blacklist:
with open ("blacklist_ip_new.txt","r") as blacklist_ip_new:
    with open ("blacklist_ip_current.txt","r") as blacklist_ip_current:
        entries_to_add = set(blacklist_ip_new).difference(blacklist_ip_current)
sep = "\n"
for entry in entries_to_add:
    entry="https://10.2.1.140//repEntries/add?smsuser=ufirsov&smspass=Bank@123&ip={}&TagData=Reputation DV Score - Manual,90".format(entry.split(sep,1)[0])
    print(entry)    
with open("blacklist_ip_current.txt","a") as blacklist_ip_current:
    blacklist_ip_current.writelines(entries_to_add)        

### And here we're removing entries from file and blacklist
with open ("blacklist_ip_new.txt","r") as blacklist_ip_new:
    with open ("blacklist_ip_current.txt","r") as blacklist_ip_current:        
        entries_to_remove= set(blacklist_ip_current).difference(blacklist_ip_new)

for entry in entries_to_remove:
    entry="https://10.2.1.140//repEntries/delete?smsuser=ufirsov&smspass=Bank@123&ip={}&criteria=entry".format(entry.split(sep,1)[0])
    #r=requests.post(entry)
    #print(r.status_code)     
    #print(entry)

for entry in entries_to_remove:
    with open("blacklist_ip_current.txt","r+") as blacklist_ip_current:
        for string in blacklist_ip_current:
            replace (entry,'')



with open("blacklist_ip_current.txt","a") as blacklist_ip_current:
    blacklist_ip_current.writelines(entries_to_add)     
