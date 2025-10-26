<template>
  <div class="p-4">
    <div class="container">
      <div v-if="project">
        <h1>{{ project.title }}</h1>
        <div class="text-gray mb-2">
          {{ project.project_year }} • {{ project.location }} • {{ project.client }}
        </div>
        
        <img 
          v-if="project.hero_image"
          :src="project.hero_image.url"
          :alt="project.title"
          style="width: 100%; max-height: 400px; object-fit: cover; margin: 2rem 0;"
        />
        
        <div v-html="project.description"></div>
        
        <!-- Project Images Gallery -->
        <div v-if="project.project_images && project.project_images.length > 0" class="mb-4">
          <h3>Project Gallery</h3>
          <div class="grid grid-3" style="margin-top: 1rem;">
            <div v-for="img in project.project_images" :key="img.id" class="card">
              <img 
                :src="img.image.url" 
                :alt="img.caption || project.title"
                style="width: 100%; height: 200px; object-fit: cover;"
              />
              <div v-if="img.caption" class="card-content">
                <p>{{ img.caption }}</p>
              </div>
            </div>
          </div>
        </div>
        
        <div v-if="project.content" class="mb-4">
          <!-- Content blocks would be rendered here -->
        </div>
      </div>
      
      <div v-else-if="loading">
        <p>Loading project...</p>
      </div>
      
      <div v-else>
        <h1>Project Not Found</h1>
        <p class="text-gray mb-2">The requested project could not be found.</p>
        <router-link to="/projects" class="btn">Back to Projects</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const api = axios.create({ 
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8002/api/',
  timeout: 10000
})

export default defineComponent({
  name: 'ProjectDetailPage',
  setup() {
    const route = useRoute()
    const project = ref(null)
    const loading = ref(false)

    const fetchProject = async () => {
      loading.value = true
      try {
        const response = await api.get(`projects/${route.params.slug}/`)
        project.value = response.data
      } catch (error) {
        console.error('Error fetching project:', error)
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      fetchProject()
    })

    return {
      project,
      loading
    }
  }
})
</script>