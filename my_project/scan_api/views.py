from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import logging
from scan_api.models import *
from django.http import HttpResponse, JsonResponse

import datetime
import subprocess
import json

from rest_framework import status

from check import get_ip_range


def ping_test(address):
    # address = '127.0.0.1'
    res = subprocess.call(['ping', address, "-c","2"])
    return res



def ping_main(portRange, ip):

    if portRange == 'all':
	    portStart = 1
	    portEnd = 1024
    else:
        try:
		    portStart = (int)(portRange.split(',')[0], 10)
		    portEnd = (int)(portRange.split(',')[1], 10)
		    if (portStart <=0 or portEnd <=0 or portStart > portEnd):
			    print("INVALID RANGE")
			    sys.exit(1)
        except ValueError:
            print("INVALID RANGE")
            sys.exit(1)

    return ping_test(ip)


def records(request):
    rec = SlaveEntry.objects.order_by('start_time')
    return render_to_response('scan_api/records.html', {'records':rec})

def jobs(request):
    job = JobEntry.objects.order_by('ip')
    return render_to_response('scan_api/jobs.html', {'jobs':job})

def jobdata(request):
    jobData = JobData.objects.order_by('ip')
    return render_to_response('scan_api/jobdata.html', {'jobdata':jobData})
   
    
        

#function triggered from REST GET request
def get(request):
    return saveScanData(request)

#Util function for get request
def saveScanData(request):
    create = False
    master_response=[]

    jsonResponse = {}

    try:
        entry = SlaveEntry.objects.get(token=request.GET['token'])
        if entry.slave_ip != request.GET['slave_ip']:
            jsonResponse['error'] = "Unauthorized access, client token and port don't match"
            return JsonResponse(jsonResponse)

   
    except SlaveEntry.DoesNotExist:
        jsonResponse['message'] = "Info : Welcome, your details will be stored, Make sure you use the same security token next time"
        entry = None
        create = True

    #if client entry all ready present , operate on it
    if entry and entry.active == 'YES':

        if 'result' in request.GET:
            entry.result = request.GET['result']
            master_response.append(entry.dest_ip+"  ")
            entry.result_time = datetime.datetime.now()
            entry.active = 'NO'
            jsonResponse['token'] = request.GET['token']
            jsonResponse['End_Time'] = entry.result_time
            
            jsonResponse['IP'] = entry.dest_ip

        else:
            jsonResponse['message'] = 'No result in the request, discarding this attempt'
            jsonResponse['error'] = 'You already got job to do, finish it first'
            return JsonResponse(jsonResponse)
            
        

        job_data_entries  = JobData.objects.filter(ip = str(entry.dest_ip).strip())
        for j in job_data_entries:
            if str(entry.token).strip() in j.client_list:
                p = j.client_list.split(",")
                p.remove(str(entry.token).strip())
                job_data_entry = j
                job_data_entry.client_list = ",".join(p)

                break
        
        if "error" in str(request.GET['result']).lower():
            job_data_entry.status = "Error"
            job_data_entry.result1 = request.GET['result']
            job_data_entry.result2 = request.GET['result']
            job_data_entry.ports_remaining = 0
            job_data_entry.result_time = datetime.datetime.now()
            job_data_entry.client_list = ""
            job_data_entry.save()
        elif "alive" in str(request.GET['result']).lower()  and ("yes" in str(request.GET['result']).lower() or "not" in str(request.GET['result']).lower()):
            job_data_entry.status = "Done"
            job_data_entry.result1 = request.GET['result']
            job_data_entry.result2 = ""
            job_data_entry.ports_remaining = 0
            job_data_entry.result_time = datetime.datetime.now()
            job_data_entry.client_list = ""
            job_data_entry.save()
        else:
            portspart = str(request.GET['result']).split("-")
            portsScannedPart = entry.port_list   
            portsScanned = len(portsScannedPart.split(","))
            
            print "port scanned ",portsScanned,"remaining",job_data_entry.ports_remaining
            job_data_entry.ports_remaining -= portsScanned
            if job_data_entry.ports_remaining <= 0:
                job_data_entry.status = "Done"
                job_data_entry.client_list = ""
                job_data_entry.ports_remaining = 0
                job_data_entry.result_time = datetime.datetime.now()
                
                job_data_entry.result1 += ","+str(portspart[0])
                
                if len(portspart)>1:
                    job_data_entry.result2 += ","+str(portspart[1])
                job_data_entry.save()
                # JobEntry.objects.get(pk = str(entry.dest_ip).strip()).delete()
            else:    
                job_data_entry.status = "In Progress"
                job_data_entry.result1 += ","+str(portspart[0])
                job_data_entry.exclude +=  ",".join(str(portsScannedPart).split(","))
                if len(portspart)>1:
                    job_data_entry.result2 += ","+str(portspart[1])
                job_data_entry.save()

        entry.save()
  
    else:
        #if client entry is not present , do the following checks
        #if an inactive client tries to send a result, repel it
        if entry != None and entry.result != None and 'result' in request.GET:
            # entry.result = request.GET['result']
            jsonResponse["Error"] = 'Result Already Exist!! Please ask for another job'
            jsonResponse["Message"] = 'Last Result was:  '+str(entry.result)
            # entry.save()
            return JsonResponse(jsonResponse)

        #if inactive entry is present , delete it
        
       
        destinations = get_ip_range(request.GET['token'])
        if len(destinations) == 0:
            jsonResponse['Error'] = 'No Job Available'
            return JsonResponse(jsonResponse)

        if entry != None:
            entry.delete()

        #create a new entry
        entry = SlaveEntry.objects.create(
            token=request.GET['token'],
            start_time = datetime.datetime.now(),
            active = 'YES',
            slave_ip = request.GET['slave_ip'],
            dest_ip = destinations[0],
            port_range = destinations[1],
            port_list = destinations[1],        
        )
        jsonResponse['Description'] = 'Entry added'
        jsonResponse['token'] = request.GET['token']
        jsonResponse['Start_Time'] = datetime.datetime.now()
        jsonResponse['IP'] = destinations[0]
        jsonResponse['port_list'] = destinations[1]
        jsonResponse['type'] = destinations[3]
        jsonResponse['subnet'] = destinations[2]

        

    return JsonResponse(jsonResponse)




