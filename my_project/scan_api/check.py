import json
from scan_api.models import *
import random

#function gets K random number between From and To, which are not present in Exclude
def get_random_in_range(From, To, Exclude, K):
    count = 0
    ports = ""
    checkset = set()
    print "Exclude",Exclude
    for i in range(0, 5000):
        r = random.randint(From, To)
        if str(r) in Exclude or r in checkset:
            continue
        else:

            if len(ports) <= 0:
                ports+=str(r)
            else:
                ports= ports + ","+(str(r))
            count += 1
            checkset.add(r)
            if count>=K:
                break
    
    return ports
    

#Function to assign job to a client, gets the earliest job available (not started or in progress) and give it to the client
def get_ip_range(name):
    K = 20
    job_data_entries  = JobData.objects.order_by('job_time')
    answer = []
    
    required_entry = None
    for entry in job_data_entries:
        if "Done" not in entry.status and "Error" not in entry.status and entry.ports_remaining_after_alloted > 0:
            required_entry = entry
            break
    
    if required_entry == None:
        return answer
    
    client_lists = required_entry.client_list.split(",")
    elist = None 
    Exclude = required_entry.exclude.split(",")
    for c in client_lists:
        try:
            elist = SlaveEntry.objects.get(pk = c.strip())
            if elist is not None:
                Exclude.extend(elist.port_list.split(","))
        except:
            print ("Slave Entry Does Not Exist")

    
    if required_entry == None:
        return answer

    parts = required_entry.port_range.split(",")
    answer.append(required_entry.ip)
    if len(parts) == 2:
        To = max(int(parts[0]), int(parts[1]))
        From = min(int(parts[0]), int(parts[1]))
        ports = get_random_in_range(From, To, Exclude, K)
        if ports != None and len(ports)>0:
            required_entry.ports_remaining_after_alloted -= len(ports.split(","))
            print "required alloted",required_entry.ports_remaining_after_alloted
            answer.append(ports)
            required_entry.status = "In Progress"
            if len(required_entry.client_list) <= 0:
                required_entry.client_list = str(name)
            else:
                required_entry.client_list = required_entry.client_list + ","+str(name)

            required_entry.save()
    
    else:
        answer.append(parts[0])
        required_entry.status = "In Progress"
        required_entry.client_list = str(name)
        required_entry.ports_remaining_after_alloted = 0
        required_entry.save()
    
    answer.append(required_entry.subnet)
    answer.append(required_entry.type_scan)
    
    return answer

