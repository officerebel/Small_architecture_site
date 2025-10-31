import axios from 'axios'

const api = axios.create({ 
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8002/api/',
  timeout: 10000
})

// Vue 3 plugin for axios
export default {
  install(app) {
    app.config.globalProperties.$axios = axios
    app.config.globalProperties.$api = api
  }
}

export { api }