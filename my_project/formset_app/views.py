# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponseRedirect
import json
import ipaddress

from formset_app.models import *
from formset_app.forms import *
from scan_api.models import *

#function for form
def formset(request):
    form = MetaForm(prefix = 'addform')
    if request.POST:
        try:
            form = MetaForm(request.POST, prefix = 'addform')
        except:
            print ("some random error")
            

        if form.is_valid():
            
            cd_p = form.cleaned_data
            entry = form.save(commit = False)

            entry.port_range = cd_p['port_range']
            entry.type_scan = cd_p['type_scan']
            entry.ip = cd_p['ip']
            entry.subnet = cd_p['subnet']
            entry.job_time = cd_p['job_time']
            entry.port_list=""

            try:
                if "," in entry.port_range:
                    parts = entry.port_range.split(",")
                    if len(parts) > 2:
                        print "Invalid Range"
                        return HttpResponseRedirect("wrong")
                    else:
                        if(int(parts[0])<0 or int(parts[0])<0):
                            return HttpResponseRedirect("wrong")

                        remaining = abs(int(parts[1]) - int(parts[0]))+1
                else:
                    if int(entry.port_range) <0 and int(entry.port_range) != -1:
                        return HttpResponseRedirect("wrong")
                    remaining = 1
            except:
                print "Invalid Range"
                return HttpResponseRedirect("wrong")

            try:
                if entry.subnet == 32:
                    all_hosts = [unicode(entry.ip)]

                elif entry.subnet >=0 and entry.subnet<32:
                    #print "Inside subnet check"
                    full_ip = str(entry.ip) + '/' + str(entry.subnet)

                    net_addr = unicode(full_ip)
                    print net_addr
                    ip_net = ipaddress.ip_network(net_addr)
                    
                    all_hosts = list(ip_net.hosts())
                    print all_hosts
                else:
                    print "Invalid Subnet"
                    return HttpResponseRedirect("wrong")


            except Exception as e:
                print e
                print "Invalid IP"
                return HttpResponseRedirect("wrong")

            #setting the entries to joblists and jobs current states tables
            for i in range(len(all_hosts)):
                #print all_hosts[i]
                jobdata = JobData.objects.create(
                    ip=str(all_hosts[i]),
                    client_list = "",
                    result1 = "",
                    result2= "",
                    ports_remaining = remaining,  
                    ports_remaining_after_alloted = remaining,
                    port_range = entry.port_range,
                    job_time = entry.job_time,
                    type_scan = entry.type_scan,
                    subnet = entry.subnet ,   
                )

                jobEnt = JobEntry.objects.create(
                    ip=str(all_hosts[i]),
                    port_range = entry.port_range,
                    job_time = entry.job_time,
                    type_scan = entry.type_scan,
                    subnet = entry.subnet ,   
                )


            return HttpResponseRedirect("added")
    else:
        form = MetaForm(prefix = 'addform')
    

    return render_to_response("formset_app/formset.html", {
            "form": form,
        }, context_instance = RequestContext(request))


#function for added html/ url
def added(request):
    return render_to_response('formset_app/added.html')

#function for show html/ url
def show(request):
    pok = Entry.objects.order_by('name')
    return render_to_response('formset_app/show.html', {'pok':pok})

#function for show html/ url
def wrong(request):
    return render_to_response('formset_app/wrong.html')


