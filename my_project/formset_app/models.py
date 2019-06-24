# coding: utf-8

from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Entry(models.Model):
	# name = models.CharField(max_length = 25,verbose_name = 'Name')
	rangeFrom = models.CharField(max_length = 10,verbose_name = 'Port No/Range(ex. 1,10)/Ping = "-1"',null = True, default = '-1')
	subnet = models.IntegerField(verbose_name = 'Subnet',null = True, default = '0')

	type_of_scans = (
		('FULL_TCP_Connect','FULL_TCP_Connect'),
		('TCP_SYN','TCP_SYN'),
		('TCP_FIN','TCP_FIN'),
	)
	type_scan = models.CharField(max_length = 15,choices = type_of_scans,verbose_name = 'Scan Type',null = True, default = 'FULL_TCP_Connect')
	ip = models.CharField(max_length = 15,verbose_name = 'IP',null = True)

	

	