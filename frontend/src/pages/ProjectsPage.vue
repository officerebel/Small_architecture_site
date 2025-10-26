<template>
  <div class="p-4">
    <div class="container">
      <div class="text-center mb-4">
        <h1>Projects</h1>
        <p class="text-gray">A collection of work and experiments</p>
      </div>

      <div class="grid grid-3">
        <div 
          v-for="project in projects" 
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
            <div class="text-gray mb-1">
              {{ project.project_year }} 
              <span v-if="project.location">• {{ project.location }}</span>
              <span v-if="project.client">• {{ project.client }}</span>
            </div>
            <h4 class="mb-1">{{ project.title }}</h4>
            <div v-html="project.description"></div>
            <span 
              v-if="project.status"
              class="status-badge"
              :class="`status-${project.status}`"
            >
              {{ project.status.replace('_', ' ') }}
            </span>
          </div>
        </div>
      </div>

      <div v-if="loading" class="text-center mb-4">
        <p>Loading projects...</p>
      </div>
    </div>
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
  name: 'ProjectsPage',
  setup() {
    const projects = ref([])
    const loading = ref(false)

    const fetchProjects = async () => {
      loading.value = true
      try {
        const response = await api.get('projects/')
        projects.value = response.data.results || response.data
      } catch (error) {
        console.error('Error fetching projects:', error)
        // Mock data for demo
        projects.value = [
          {
            id: 1,
            title: 'Modern Office Complex',
            slug: 'modern-office-complex',
            project_year: 2024,
            location: 'New York',
            client: 'Tech Corp',
            status: 'completed',
            description: 'A sustainable office building with innovative design features.'
          },
          {
            id: 2,
            title: 'Residential Tower',
            slug: 'residential-tower',
            project_year: 2023,
            location: 'Copenhagen',
            client: 'Housing Association',
            status: 'in_progress',
            description: 'High-density housing with focus on community spaces.'
          },
          {
            id: 3,
            title: 'Cultural Center',
            slug: 'cultural-center',
            project_year: 2023,
            location: 'Berlin',
            client: 'City Council',
            status: 'concept',
            description: 'Multi-purpose cultural facility for the local community.'
          }
        ]
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      fetchProjects()
    })

    return {
      projects,
      loading
    }
  }
})
</script>

<style scoped>
.status-badge {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  border-radius: 3px;
  font-size: 0.8rem;
  text-transform: uppercase;
  margin-top: 0.5rem;
}

.status-completed {
  background: #d4edda;
  color: #155724;
}

.status-in_progress {
  background: #fff3cd;
  color: #856404;
}

.status-concept {
  background: #d1ecf1;
  color: #0c5460;
}
</style>