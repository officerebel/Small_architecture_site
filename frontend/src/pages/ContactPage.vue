<template>
  <div class="p-4">
    <div class="container">
      <div class="text-center mb-4">
        <h1>Contact</h1>
      </div>
      
      <div style="max-width: 600px; margin: 0 auto;">
        <div v-if="contactData">
          <div v-if="contactData.email" class="mb-2">
            <h4>Email</h4>
            <a :href="`mailto:${contactData.email}`">{{ contactData.email }}</a>
          </div>
          
          <div v-if="contactData.phone" class="mb-2">
            <h4>Phone</h4>
            <a :href="`tel:${contactData.phone}`">{{ contactData.phone }}</a>
          </div>
          
          <div v-if="contactData.address" class="mb-2">
            <h4>Address</h4>
            <div v-html="contactData.address"></div>
          </div>
        </div>
        
        <div v-else>
          <p class="text-center text-gray">
            Contact information can be managed through the Django admin interface.
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
  name: 'ContactPage',
  setup() {
    const contactData = ref(null)

    const fetchContactData = async () => {
      try {
        const response = await api.get('contact/')
        contactData.value = response.data
      } catch (error) {
        console.error('Error fetching contact data:', error)
      }
    }

    onMounted(() => {
      fetchContactData()
    })

    return {
      contactData
    }
  }
})
</script>