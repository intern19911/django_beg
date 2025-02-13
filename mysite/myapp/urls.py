from django.urls import path
from myapp import views


app_name = 'myapp'

urlpatterns = [
  path("", views.index),
  path("<int:my_id>/", views.indexItem, name='detail'),
]