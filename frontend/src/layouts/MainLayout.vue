<template>
  <div>
    <nav>
      <div class="container">
        <router-link to="/" class="logo">Portfolio</router-link>
        <ul>
          <li>
            <router-link 
              to="/projects" 
              :class="{ active: $route.name === 'projects' }"
            >
              Projects
            </router-link>
          </li>
          <li>
            <router-link 
              to="/about" 
              :class="{ active: $route.name === 'about' }"
            >
              About
            </router-link>
          </li>
          <li>
            <router-link 
              to="/contact" 
              :class="{ active: $route.name === 'contact' }"
            >
              Contact
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
    
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MainLayout'
})
</script>