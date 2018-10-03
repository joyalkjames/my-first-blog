from django.conf.urls import url
from .views import WelcomeView
from django.urls import path, include



urlpatterns = [

	path('',WelcomeView),
]



