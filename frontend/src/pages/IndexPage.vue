<template>
  <div>
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <h1>{{ homeData?.hero_title || 'Portfolio' }}</h1>
        <div class="text-gray" v-html="homeData?.hero_subtitle || 'Welcome to my portfolio'"></div>
      </div>
    </section>

    <!-- Featured Projects Preview -->
    <section class="p-4">
      <div class="container">
        <h2 class="text-center mb-4">Featured Projects</h2>
        <div class="grid grid-3">
          <div 
            v-for="project in featuredProjects" 
            :key="project.id"
            class="card cursor-pointer"
            @click="$router.push(`/projects/${project.slug}`)"
          >
            <img
              v-if="project.hero_image"
              :src="project.hero_image.url"
              :alt="project.title"
            />
            <div class="card-content">
              <h4>{{ project.title }}</h4>
              <div class="text-gray mb-1">{{ project.project_year }} • {{ project.location }}</div>
              <div v-html="project.description"></div>
            </div>
          </div>
        </div>
        
        <div class="text-center mb-4">
          <router-link to="/projects" class="btn btn-outline">View All Projects</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'

const api = axios.create({ 
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8002/api/',
  timeout: 10000
})

export default defineComponent({
  name: 'IndexPage',
  setup() {
    const homeData = ref(null)
    const featuredProjects = ref([])

    const fetchHomeData = async () => {
      try {
        const response = await api.get('home/')
        homeData.value = response.data
      } catch (error) {
        console.error('Error fetching home data:', error)
      }
    }

    const fetchFeaturedProjects = async () => {
      try {
        const response = await api.get('projects/?limit=3')
        featuredProjects.value = response.data.results || response.data
      } catch (error) {
        console.error('Error fetching projects:', error)
        // Mock data for demo
        featuredProjects.value = [
          {
            id: 1,
            title: 'Sample Project 1',
            slug: 'sample-project-1',
            project_year: 2024,
            location: 'New York',
            description: 'A modern architectural project showcasing innovative design.'
          },
          {
            id: 2,
            title: 'Sample Project 2',
            slug: 'sample-project-2',
            project_year: 2023,
            location: 'Copenhagen',
            description: 'Sustainable building design with focus on environmental impact.'
          }
        ]
      }
    }

    onMounted(() => {
      fetchHomeData()
      fetchFeaturedProjects()
    })

    return {
      homeData,
      featuredProjects
    }
  }
})
</script>