from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'formset_app.views.formset', name = 'formset'),
    url(r'^added/$', 'formset_app.views.added', name = 'added'),
    url(r'^wrong/$', 'formset_app.views.wrong', name = 'wrong'),
    url(r'^show/$', 'formset_app.views.show', name = 'show'),
)

urlpatterns += staticfiles_urlpatterns()
