"""edusys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^student/$', views.student_list, name='student_list'),
    url(r'^student/(?P<pk>\d+)/delete/$', views.student_delete, name='student_delete'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.student_edit, name='student_edit'),
    url(r'^student/create/$', views.student_new, name='student_new'),
    url(r'^parent/$', views.parent_list, name='parent_list'),
    url(r'^parent/(?P<pk>\d+)/delete/$', views.parent_delete, name='parent_delete'),
    url(r'^parent/(?P<pk>\d+)/edit/$', views.parent_edit, name='parent_edit'),
    url(r'^parent/create/$', views.parent_new, name='parent_new'),
    url(r'^teacher/$', views.teacher_list, name='teacher_list'),
    url(r'^teacher/(?P<pk>\d+)/delete/$', views.teacher_delete, name='teacher_delete'),
    url(r'^teacher/(?P<pk>\d+)/edit/$', views.teacher_edit, name='teacher_edit'),
    url(r'^teacher/create/$', views.teacher_new, name='teacher_new'),
    url(r'^event/$', views.event_list, name='event_list'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.event_delete, name='event_delete'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/create/$', views.event_new, name='event_new'),
    url(r'^invoice/$', views.invoice_list, name='invoice_list'),
    url(r'^invoice/(?P<pk>\d+)/delete/$', views.invoice_delete, name='invoice_delete'),
    url(r'^invoice/(?P<pk>\d+)/edit/$', views.invoice_edit, name='invoice_edit'),
    url(r'^invoice/create/$', views.invoice_new, name='invoice_new'),
    url(r'^course/$', views.course_list, name='course_list'),
    url(r'^course/(?P<pk>\d+)/delete/$', views.course_delete, name='course_delete'),
    url(r'^course/(?P<pk>\d+)/edit/$', views.course_edit, name='course_edit'),
    url(r'^course/create/$', views.course_new, name='course_new'),
    url(r'^grade/$', views.grade_list, name='grade_list'),
    url(r'^grade/(?P<pk>\d+)/delete/$', views.grade_delete, name='grade_delete'),
    url(r'^grade/(?P<pk>\d+)/edit/$', views.grade_edit, name='grade_edit'),
    url(r'^grade/create/$', views.grade_new, name='grade_new'),
    url(r'^mark/$', views.mark_list, name='mark_list'),
    url(r'^mark/(?P<pk>\d+)/delete/$', views.mark_delete, name='mark_delete'),
    url(r'^mark/(?P<pk>\d+)/edit/$', views.mark_edit, name='mark_edit'),
    url(r'^mark/create/$', views.mark_new, name='mark_new'),
    url(r'^exam/$', views.exam_list, name='exam_list'),
    url(r'^exam/(?P<pk>\d+)/delete/$', views.exam_delete, name='exam_delete'),
    url(r'^exam/(?P<pk>\d+)/edit/$', views.exam_edit, name='exam_edit'),
    url(r'^exam/create/$', views.exam_new, name='exam_new'),
]


