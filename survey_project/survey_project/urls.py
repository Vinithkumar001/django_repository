"""
URL configuration for survey_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from survey_app.views import create_survey,get_survey,update_survey,delete_survey
from survey_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('create/', create_survey,name='createsurvey'),
    path('getall/', get_survey,name='add_question'),
    path("update/<int:survey _id>",update_survey,name="updatesurvey"),
    path("delete/<int:survey_id>",delete_survey),
    path('create_answer/<int:survey_id>',views.create_survey_answer,name='create_survey_answer'),
    path('update_answer/<int:surveyid>',views.update_answer,name="update_answer"),
    path("delete_answer/<int:surveyid>",views.delete_answer),
]
