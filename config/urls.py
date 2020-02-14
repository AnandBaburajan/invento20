from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from django.views import defaults as default_views
from rest_framework import routers

from invento18.events.views import EventDetailView, departmentview, event_register_view, event_register, campus_ambassador, ambassador_register_view, ambassador_login_view
from invento18.events.serializers import EventList

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/$', TemplateView.as_view(template_name='pages/login.html'), name='login'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^3d/$', TemplateView.as_view(template_name='pages/3d.html'), name='3d'),
    url(r'share/$', TemplateView.as_view(template_name='pages/ambassador.html'), name='share'),
    url(r'caportal/$', TemplateView.as_view(template_name='pages/campus.html'), name='campus-ambassador'),
    url(r'^events/$', event_register, name='events'),
    url(r'^event-register/$', event_register_view, name='event-register'),
    #url(r'^campus-ambassador/$', campus_ambassador, name='campus-ambassador'),
    url(r'^ambassador_register/$', ambassador_register_view, name='ambassador_register'),
    url(r'^ambassador_login/$', ambassador_login_view, name='ambassador_login'),
    url(r'api/v1/events/(?P<category>[\w]{1,3})/(?P<_type>[\w]{0,3})', EventList.as_view()),
    url(r'^general/$', departmentview, name='general'),
    url(r'^cse/$', departmentview, name='cse'),
    url(r'^ece/$', departmentview, name='ece'),
    url(r'^eee/$', departmentview, name='eee'),
    url(r'^it/$', departmentview, name='it'),
    url(r'^me/$', departmentview, name='me'),
    url(r'^saptha/$', departmentview, name='sta'),
    url(r'^events/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event-view'),
    url(r'^wp-content/uploads/2018/02/Invento18-CSE-Brochure.pdf',
        RedirectView.as_view(url="https://images.inventogec.org/invento18csebrochure.pdf")),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include(('invento18.users.urls', 'users'), namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),



    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
