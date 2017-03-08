from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns =  patterns('',
        url('^$', TemplateView.as_view(template_name='index.html')),
        url(r'^login/', TemplateView.as_view(template_name='login.html')),
        )
