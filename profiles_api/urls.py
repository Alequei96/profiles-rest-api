from django.urls import path,include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('API-viewset', views.ViewSet, base_name='viewset')
"""Multiple view sets can be listed and display per default just adding more classes on views.py"""
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('API-view/', views.ApiView.as_view()),
    path('', include(router.urls)),
]