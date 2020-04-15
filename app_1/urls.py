from django.urls import path
from app_1 import views


urlpatterns = [
    path('upload/', views.upload),
    path('examAjax/', views.examAjax),
    path('exam/', views.exam),
    path('examData/', views.examData, name='ajax_handle'),
    path('typeData/', views.examType, name='getType'),
    path('examDataByType/', views.examDataBytype, name='getData'),
    path('examPage/', views.examPage),
]
