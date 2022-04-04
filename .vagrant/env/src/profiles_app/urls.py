from django.urls import path

from .views import HelloApiView

app_name = 'profiles_app'
urlpatterns = [
    path('hello-view/',HelloApiView.as_view(),name='hello-view')
]
