import requests  

### Donwnload new (updated by SCOC) blacklist and put it to file 'blacklist_ip_new'
url = "http://kickself.com/wp-content/uploads/2019/01/CSOC_BLOCKLIST_IP.txt"

try:
    req=requests.get(url,allow_redirects=True)
except:
    print ("Failed fetching CSOC_BLOCKLIST_IP.txt - Please check connection to intranet.cbq.com.qa")

with open ("blacklist_ip_buffer.txt","w") as blacklist_ip_buffer:
    blacklist_ip_buffer.write(req.text)

with open("blacklist_ip_buffer.txt","r") as blacklist_ip_buffer:
    with open('blacklist_ip_new.txt','w') as blacklist_ip_new:
        for line in blacklist_ip_buffer:
            if not line.strip(): continue  # skip the empty line
            blacklist_ip_new.write(line)
                
### Here we compare new and current blacklist, and new entries to the current file and to the IPS blacklist:
############################################################################################################
with open ("blacklist_ip_new.txt","r") as blacklist_ip_new:
    with open ("blacklist_ip_current.txt","r") as blacklist_ip_current:
        blacklist_ip_current_set=set(blacklist_ip_current)
        blacklist_ip_new_set=set(blacklist_ip_new)
        entries_to_add=blacklist_ip_new_set.difference(blacklist_ip_current_set)
        entries_to_remove=blacklist_ip_current_set.difference(blacklist_ip_new_set) 
        filedata=blacklist_ip_new.read()

sep = "\n"
for entry in entries_to_add:
    if "0.0.0.0" not in entry:
        entry="https://10.2.1.140//repEntries/add?smsuser=ufirsov&smspass=Bank@123&ip={}&TagData=Reputation DV Score - Manual,90".format(entry.split(sep,1)[0])
        print (entry) 

for entry in entries_to_remove:
    entry="https://10.2.1.140//repEntries/delete?smsuser=ufirsov&smspass=Bank@123&ip={}&criteria=entry".format(entry.split(sep,1)[0])
    #r=requests.post(entry)
    #print(r.status_code)
    print(entry)

with open ("blacklist_ip_new.txt","r") as blacklist_ip_new:
    with open ('blacklist_ip_current.txt','w') as blacklist_ip_current:
        blacklist_ip_current.write(blacklist_ip_new.read())    
    







'''








import requests  

### Donwnload new (updated by SCOC) blacklist and put it to file 'blacklist_ip_new'
url = "http://kickself.com/wp-content/uploads/2019/01/CSOC_BLOCKLIST_IP.txt"
req=requests.get(url,allow_redirects=True)


with open ("blacklist_ip_buffer.txt","w") as blacklist_ip_buffer:
    blacklist_ip_buffer.write(req.text)

with open("blacklist_ip_buffer.txt","r") as blacklist_ip_buffer:
    with open('blacklist_ip_new.txt','w') as blacklist_ip_new:
        for line in blacklist_ip_buffer:
            if not line.strip(): continue  # skip the empty line
            blacklist_ip_new.write(line)
                
### Here we compare new and current blacklist, and new entries to the current file and to the IPS blacklist:
############################################################################################################
with open ("blacklist_ip_new.txt","r") as blacklist_ip_new:
    with open ("blacklist_ip_current.txt","r") as blacklist_ip_current:
        blacklist_ip_current_set=set(blacklist_ip_current)
        blacklist_ip_new_set=set(blacklist_ip_new)
        entries_to_add=blacklist_ip_new_set.difference(blacklist_ip_current_set)
        entries_to_remove=blacklist_ip_current_set.difference(blacklist_ip_new_set) 
        filedata=blacklist_ip_new.read()

sep = "\n"
for entry in entries_to_add:
    if "0.0.0.0" not in entry:
        entry="https://10.2.1.140//repEntries/add?smsuser=ufirsov&smspass=Bank@123&ip={}&TagData=Reputation DV Score - Manual,90".format(entry.split(sep,1)[0])
        print (entry) 

for entry in entries_to_remove:
    entry="https://10.2.1.140//repEntries/delete?smsuser=ufirsov&smspass=Bank@123&ip={}&criteria=entry".format(entry.split(sep,1)[0])
    #r=requests.post(entry)
    #print(r.status_code)
    print(entry)

with open ("blacklist_ip_new.txt","r") as blacklist_ip_new:
    with open ('blacklist_ip_current.txt','w') as blacklist_ip_current:
        blacklist_ip_current.write(blacklist_ip_new.read())    
    '''