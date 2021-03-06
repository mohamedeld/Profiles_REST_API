from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView,HelloViewSet


router = DefaultRouter()
router.register('hello-viewsets',HelloViewSet,basename='hello-viewsets')

app_name = 'profiles_app'
urlpatterns = [
    path('hello-view/',HelloApiView.as_view(),name='hello-view'),
    path('',include(router.urls)),
]
