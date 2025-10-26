from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from modelcluster.fields import ParentalKey


class HomePage(Page):
    """Main landing page"""
    hero_title = models.CharField(max_length=255, default="Portfolio")
    hero_subtitle = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
    ]
    
    api_fields = [
        APIField('hero_title'),
        APIField('hero_subtitle'),
    ]


class ProjectIndexPage(Page):
    """Projects listing page"""
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    def get_projects(self):
        return ProjectPage.objects.live().descendant_of(self)
    
    api_fields = [
        APIField('intro'),
        APIField('projects', serializer='portfolio.serializers.ProjectPageSerializer'),
    ]
    
    def projects(self):
        return self.get_projects()


class ProjectPage(Page):
    """Individual project page - inspired by BIG's project structure"""
    project_year = models.IntegerField()
    location = models.CharField(max_length=255, blank=True)
    client = models.CharField(max_length=255, blank=True)
    project_type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('concept', 'Concept'),
    ], default='completed')
    
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    description = RichTextField()
    
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('gallery', blocks.ListBlock(ImageChooserBlock(), template='portfolio/blocks/gallery.html')),
    ], blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('project_year'),
            FieldPanel('location'),
            FieldPanel('client'),
            FieldPanel('project_type'),
            FieldPanel('status'),
        ], heading="Project Details"),
        FieldPanel('hero_image'),
        FieldPanel('description'),
        FieldPanel('content'),
        InlinePanel('project_images', label="Project Images"),
    ]
    
    api_fields = [
        APIField('project_year'),
        APIField('location'),
        APIField('client'),
        APIField('project_type'),
        APIField('status'),
        APIField('hero_image'),
        APIField('description'),
        APIField('content'),
        APIField('project_images'),
    ]


class ProjectImage(Orderable):
    """Additional images for projects"""
    project = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='project_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(max_length=255, blank=True)
    
    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class AboutPage(Page):
    """About page"""
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    bio = RichTextField()
    skills = RichTextField(blank=True)
    experience = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('profile_image'),
        FieldPanel('bio'),
        FieldPanel('skills'),
        FieldPanel('experience'),
    ]
    
    api_fields = [
        APIField('profile_image'),
        APIField('bio'),
        APIField('skills'),
        APIField('experience'),
    ]


class ContactPage(Page):
    """Contact page"""
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('address'),
    ]
    
    api_fields = [
        APIField('email'),
        APIField('phone'),
        APIField('address'),
    ]