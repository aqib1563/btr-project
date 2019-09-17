from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
    path('contacts/', views.contact_view,name='contact_view'),
]
