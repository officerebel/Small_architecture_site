from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'projects', api_views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', api_views.HomePageView.as_view(), name='home'),
    path('about/', api_views.AboutPageView.as_view(), name='about'),
    path('contact/', api_views.ContactPageView.as_view(), name='contact'),
]