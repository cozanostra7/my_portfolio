from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomePage,name='home' ),
    path('project/<str:pk>/',views.singleProject,name='project'),
    path('projects/',views.projects_list,name='projects'),
    path('contact/',views.contactPage,name='contact'),
    path('message/',views.sendMessage,name='message'),
    path('',views.showSKills,name='skills'),
]