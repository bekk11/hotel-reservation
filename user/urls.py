from django.urls import path

from user.api.client.create_client import CreateClient
from user.api.client.destroy_client import DestroyClient
from user.api.client.list_client import ListClient
from user.api.client.retrieve_client import RetrieveClient
from user.api.client.update_client import UpdateClient

urlpatterns = [
    path('client/list/', ListClient.as_view()),
    path('client/create/', CreateClient.as_view()),

    path('client/retrieve/<str:pk>/', RetrieveClient.as_view()),
    path('client/update/<str:pk>/', UpdateClient.as_view()),
    path('client/destroy/<str:pk>/', DestroyClient.as_view()),
]
