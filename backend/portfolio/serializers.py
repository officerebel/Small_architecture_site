from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField
from .models import ProjectPage, HomePage, AboutPage, ContactPage, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    image = ImageRenditionField('fill-400x300', read_only=True)
    
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Fix image URLs to include full backend URL
        if data.get('image') and data['image'].get('url'):
            request = self.context.get('request')
            if request:
                data['image']['url'] = request.build_absolute_uri(data['image']['url'])
            else:
                # Fallback for local development
                data['image']['url'] = f"http://localhost:8002{data['image']['url']}"
        return data


class ProjectPageSerializer(serializers.ModelSerializer):
    hero_image = ImageRenditionField('fill-800x600', read_only=True)
    url = serializers.CharField(source='get_url', read_only=True)
    project_images = ProjectImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProjectPage
        fields = [
            'id', 'title', 'slug', 'url', 'project_year', 'location', 
            'client', 'project_type', 'status', 'hero_image', 'description', 'project_images'
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Fix image URLs to include full backend URL
        if data.get('hero_image') and data['hero_image'].get('url'):
            request = self.context.get('request')
            if request:
                data['hero_image']['url'] = request.build_absolute_uri(data['hero_image']['url'])
            else:
                # Fallback for local development
                data['hero_image']['url'] = f"http://localhost:8002{data['hero_image']['url']}"
        return data


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = ['title', 'hero_title', 'hero_subtitle']


class AboutPageSerializer(serializers.ModelSerializer):
    profile_image = ImageRenditionField('fill-400x400', read_only=True)
    
    class Meta:
        model = AboutPage
        fields = ['title', 'profile_image', 'bio', 'skills', 'experience']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Fix image URLs to include full backend URL
        if data.get('profile_image') and data['profile_image'].get('url'):
            request = self.context.get('request')
            if request:
                data['profile_image']['url'] = request.build_absolute_uri(data['profile_image']['url'])
            else:
                # Fallback for local development
                data['profile_image']['url'] = f"http://localhost:8002{data['profile_image']['url']}"
        return data


class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = ['title', 'email', 'phone', 'address']