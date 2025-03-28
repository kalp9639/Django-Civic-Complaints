# notifications/urls.py
from django.urls import path
from . import views

# app_name = 'notifications' # Optional: Add namespace if needed

urlpatterns = [
    path('mark-all-read/', views.mark_all_notifications_read, name='mark_all_notifications_read'),
    path('redirect/<int:notification_id>/', views.notification_redirect, name='notification_redirect'),
    path('all/', views.all_notifications_list, name='all_notifications_list'),
]