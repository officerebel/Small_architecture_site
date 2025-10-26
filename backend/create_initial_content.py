#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from wagtail.models import Site
from portfolio.models import HomePage, ProjectIndexPage, AboutPage, ContactPage, ProjectPage

def create_initial_content():
    # Get the root page
    root_page = Site.objects.get(is_default_site=True).root_page
    
    # Create home page
    home_page = HomePage(
        title="Portfolio",
        hero_title="Welcome to My Portfolio",
        hero_subtitle="<p>Showcasing innovative architectural and design projects</p>",
        slug="home"
    )
    root_page.add_child(instance=home_page)
    
    # Create projects index page
    projects_page = ProjectIndexPage(
        title="Projects",
        intro="<p>A collection of architectural projects and design experiments</p>",
        slug="projects"
    )
    home_page.add_child(instance=projects_page)
    
    # Create sample projects
    project1 = ProjectPage(
        title="Modern Office Complex",
        project_year=2024,
        location="New York, USA",
        client="Tech Corporation",
        project_type="Commercial",
        status="completed",
        description="<p>A sustainable office building featuring innovative design and energy-efficient systems.</p>",
        slug="modern-office-complex"
    )
    projects_page.add_child(instance=project1)
    
    project2 = ProjectPage(
        title="Residential Tower",
        project_year=2023,
        location="Copenhagen, Denmark",
        client="Housing Association",
        project_type="Residential",
        status="in_progress",
        description="<p>High-density housing with focus on community spaces and sustainable living.</p>",
        slug="residential-tower"
    )
    projects_page.add_child(instance=project2)
    
    project3 = ProjectPage(
        title="Cultural Center",
        project_year=2023,
        location="Berlin, Germany",
        client="City Council",
        project_type="Cultural",
        status="concept",
        description="<p>Multi-purpose cultural facility designed to serve the local community.</p>",
        slug="cultural-center"
    )
    projects_page.add_child(instance=project3)
    
    # Create about page
    about_page = AboutPage(
        title="About",
        bio="<p>I am an architect and designer passionate about creating innovative spaces that enhance human experience and environmental sustainability.</p>",
        skills="<p>Architecture, Urban Planning, Sustainable Design, 3D Modeling, Project Management</p>",
        experience="<p>10+ years of experience in architectural design and project management.</p>",
        slug="about"
    )
    home_page.add_child(instance=about_page)
    
    # Create contact page
    contact_page = ContactPage(
        title="Contact",
        email="hello@portfolio.com",
        phone="+1 (555) 123-4567",
        address="<p>123 Design Street<br>Architecture City, AC 12345</p>",
        slug="contact"
    )
    home_page.add_child(instance=contact_page)
    
    # Set home page as the site's root page
    site = Site.objects.get(is_default_site=True)
    site.root_page = home_page
    site.save()
    
    print("Initial content created successfully!")

if __name__ == "__main__":
    create_initial_content()