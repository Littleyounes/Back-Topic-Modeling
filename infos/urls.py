from django.urls import path
from . import views
urlpatterns=[
    path('stats/',views.getstats,name='get-stats'),

]