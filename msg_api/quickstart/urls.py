from django.urls import include, path
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('create_message/', views.CreateMessage.as_view(), name='create_message'),
    path('all_messages/<username>/', views.GetAllUserMessages.as_view(), name='all_messages'),
    path('all_unread_messages/<username>/', views.GetAllUnreadUserMessages.as_view(), name='all_unread_messages'),
    path('read_message/<username>/', views.ReadMessage.as_view(), name='read_message'),
    path('delete_message/<id>/', views.DeleteMessage.as_view(), name='delete_message'),
]