<template>
  <div class="p-4">
    <div class="container">
      <div class="text-center mb-4">
        <h1>About</h1>
      </div>
      
      <div style="max-width: 800px; margin: 0 auto;">
        <div v-if="aboutData">
          <img 
            v-if="aboutData.profile_image"
            :src="aboutData.profile_image.url"
            :alt="aboutData.title"
            style="width: 200px; height: 200px; object-fit: cover; border-radius: 50%; margin: 0 auto 2rem; display: block;"
          />
          
          <div class="mb-4" v-html="aboutData.bio"></div>
          
          <div v-if="aboutData.skills" class="mb-4">
            <h3>Skills</h3>
            <div v-html="aboutData.skills"></div>
          </div>
          
          <div v-if="aboutData.experience" class="mb-4">
            <h3>Experience</h3>
            <div v-html="aboutData.experience"></div>
          </div>
        </div>
        
        <div v-else>
          <p class="text-center text-gray">
            Welcome! This is where you can learn more about the portfolio owner. 
            Content can be managed through the Django admin interface.
          </p>
        </div>
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
  name: 'AboutPage',
  setup() {
    const aboutData = ref(null)

    const fetchAboutData = async () => {
      try {
        const response = await api.get('about/')
        aboutData.value = response.data
      } catch (error) {
        console.error('Error fetching about data:', error)
      }
    }

    onMounted(() => {
      fetchAboutData()
    })

    return {
      aboutData
    }
  }
})
</script>