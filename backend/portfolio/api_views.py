from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import ProjectPage, HomePage, AboutPage, ContactPage
from .serializers import (
    ProjectPageSerializer, HomePageSerializer, 
    AboutPageSerializer, ContactPageSerializer
)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for projects"""
    queryset = ProjectPage.objects.live().order_by('-project_year')
    serializer_class = ProjectPageSerializer
    lookup_field = 'slug'


class HomePageView(generics.RetrieveAPIView):
    """API endpoint for home page"""
    serializer_class = HomePageSerializer
    
    def get_object(self):
        return HomePage.objects.live().first()


class AboutPageView(generics.RetrieveAPIView):
    """API endpoint for about page"""
    serializer_class = AboutPageSerializer
    
    def get_object(self):
        return AboutPage.objects.live().first()


class ContactPageView(generics.RetrieveAPIView):
    """API endpoint for contact page"""
    serializer_class = ContactPageSerializer
    
    def get_object(self):
        return ContactPage.objects.live().first()