"""
URL configuration for Disaster_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Disaster_management_app.views import *
urlpatterns = [
    path('', LoginPage.as_view(), name="login"),

    # //////////////////////////// ADMIN //////////////////////////////////

    path('add_coordinator', Add_coordinatorPage.as_view(), name="coordinator"),
    path('resource_management', resource_management.as_view(), name="resourcemanagement"),
    path('add_resource', add_resource.as_view(), name="add resource"),
    path('deleteResource/<int:id>/', deleteResource.as_view(), name="deleteresource"),
    path('edit_resource/<int:id>/',edit_resource.as_view(),name="view user reports"),
    path('view_complaint', view_complaint.as_view(), name="view complaint"),
    path('view_reports', view_reports.as_view(), name="view reports"),
    path('view_coordinator', view_coordinator.as_view(), name="viewcoordinator"),
    path('deletecoordinator/<int:id>/',deletecoordinator.as_view(),name='deletecoordinator'),
    path('edit_coordinator/<int:id>/',edit_coordinator.as_view(),name='edit_coordinator'),
    path('adminhome',adminhome.as_view(), name="adminhome"),
    path('reply/<int:id>/',reply.as_view(), name="reply"),
    # //////////////////////////////// VOLUNTEERS //////////////////////////////////////
    path('Volunteer_home',Volunteers_home.as_view(), name="volunteers home"),
    path('Add_victim_info', Add_victim_info.as_view(), name="victim info"),
    path('registration', registration.as_view(), name="registration"),
    path('Send_alert', Send_alert.as_view(), name="Send alert"),
    path('Send_Resource_request', Send_Resource_request.as_view(), name="Send alert"),
    path('Resource', Resource.as_view(), name="Resource"),
    path('View_User', View_User.as_view(), name="User"),
    path('view_user_reports', view_user_reports.as_view(), name="view user reports"),

    

]


