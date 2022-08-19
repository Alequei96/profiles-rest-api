from django.urls import path,include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('API-viewset', views.ViewSet, base_name='viewset')


urlpatterns = [
    path('API-view/', views.ApiView.as_view()),
    path('', include(router.urls)),
]