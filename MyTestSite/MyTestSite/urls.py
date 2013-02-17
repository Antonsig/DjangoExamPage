from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Exams.views.index', name='index'),
    # url(r'about', 'Exams.views.about', name='about'),
    url(r'exam/(\d+)/$', 'Exams.views.exam_details', name='exam'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$', 'Exams.views.home'),
    url(r'results', 'Exams.views.results', name='results'),
    url(r'useranswers', 'Exams.views.useranswers', name='useranswers'),
    url(r'createxam/$', 'Exams.views.createxam'),
    url(r'createxamquestion/$', 'Exams.views.createxamquestion'),
    url(r'logout', 'Exams.views.logout_view', name='logout'),
    # url(r'^accounts/logout$', 'django.contrib.auth.views.logout'),
    url(r'register', 'Exams.views.register', name='register'),
    # url(r'^accounts/', include('registration.urls')),
    # url(r'^MyTestSite/', include('MyTestSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
