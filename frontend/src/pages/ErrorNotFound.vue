<template>
  <div class="p-4">
    <div class="container text-center">
      <h1>404</h1>
      <p class="text-gray mb-2">Page not found</p>
      <router-link to="/" class="btn">Go Home</router-link>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ErrorNotFound'
})
</script>