from django.urls import path
from . import views

# the 'name' value as called by the {% url %} template tag
urlpatterns = [
    path('', views.index, name='index'),
]
