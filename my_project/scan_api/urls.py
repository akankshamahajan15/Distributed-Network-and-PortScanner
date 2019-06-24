from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # url(r'^$', 'formset_app.views.formset', name = 'formset'),
    url(r'^scan/$', 'scan_api.views.get', name = 'scan'),
    url(r'^isalive/$', 'scan_api.views.show', name = 'isalive'),
    url(r'^records/$', 'scan_api.views.records', name = 'records'),
    url(r'^jobs/$', 'scan_api.views.jobs', name = 'jobs'),
    url(r'^jobdata/$', 'scan_api.views.jobdata', name = 'jobdata'),
)

urlpatterns += staticfiles_urlpatterns()
