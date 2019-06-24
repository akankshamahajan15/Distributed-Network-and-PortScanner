from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    



#table for slave/client entry
class SlaveEntry(models.Model):
    #token is primary key for SlaveEntry
    token = models.CharField(primary_key = True, max_length = 25,verbose_name = 'security token')
    port_range = models.CharField(max_length = 25,verbose_name = 'Port Range')
    start_time = models.TimeField(verbose_name='Scan_start_time')
    result_time = models.TimeField(verbose_name='result_time', null=True)
    active = models.CharField(max_length = 25,verbose_name = 'Active')

    result = models.TextField(max_length = 500,verbose_name = 'Description', null=True)
    slave_ip = models.TextField(max_length = 500,verbose_name = 'SlaveIP', null=True)
    dest_ip = models.TextField(max_length = 500,verbose_name = 'DestIP', null=True)
    port_list = models.CharField(max_length = 25,verbose_name = 'Port List to Scan', null=True)

#table for registered jobs entry
class JobEntry(models.Model):
    port_range = models.CharField(max_length = 15,verbose_name = 'Port No/Range(ex. 1,10)/Ping = "-1"',null = True, default = '-1')
    subnet = models.IntegerField(verbose_name = 'Subnet',null = True, default = 32)
    ip = models.CharField(max_length = 16,verbose_name = 'DestIP', null=False)
    #type of scans drop down
    type_of_scans = (
		('FULL_TCP_Connect','FULL_TCP_Connect'),
		('TCP_SYN','TCP_SYN'),
		('TCP_FIN','TCP_FIN'),
	)
    type_scan = models.CharField(max_length = 25,choices = type_of_scans,verbose_name = 'Scan Type',null = True, default = 'FULL_TCP_Connect')
    job_time = models.TimeField(default=datetime.now())

#table for job status and results , basically user view
class JobData(models.Model):
    ip = models.CharField(max_length = 16,verbose_name = 'DestIP', null=False)
    client_list = models.TextField(max_length = 5000,verbose_name = 'Clients List', null=True)
    result1 = models.TextField(max_length = 5000,verbose_name = 'Results 1', null=True)
    result2 = models.TextField(max_length = 5000,verbose_name = 'Results 2', null=True)
    ports_remaining = models.IntegerField(verbose_name = 'Port Scan Remaining',null = True, default = 0)
    ports_remaining_after_alloted = models.IntegerField(verbose_name = 'Port Scan Remaining after alloted',null = True, default = 0)
    status = models.CharField(max_length = 25,verbose_name = 'Status', default = 'Not Started')
    port_range = models.CharField(max_length = 10,verbose_name = 'Port No/Range(ex. 1,10)/Ping = "-1"',null = True, default = '-1')
    job_time = models.TimeField(default=datetime.now())
    result_time = models.TimeField(verbose_name='result_time', null=True)
    type_scan = models.CharField(max_length = 25,verbose_name = 'Scan Type',null = True, default = 'FULL_TCP_Connect')
    subnet = models.IntegerField(verbose_name = 'Subnet',null = True, default = 32)
    exclude = models.TextField(max_length = 5000,verbose_name = 'exclude', null=True, default="")








