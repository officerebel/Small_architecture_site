const routes = [
  {
    path: '/',
    component: () => import('../layouts/MainLayout.vue'),
    children: [
      { 
        path: '', 
        name: 'home',
        component: () => import('../pages/IndexPage.vue') 
      },
      { 
        path: '/projects', 
        name: 'projects',
        component: () => import('../pages/ProjectsPage.vue') 
      },
      { 
        path: '/projects/:slug', 
        name: 'project-detail',
        component: () => import('../pages/ProjectDetailPage.vue') 
      },
      { 
        path: '/about', 
        name: 'about',
        component: () => import('../pages/AboutPage.vue') 
      },
      { 
        path: '/contact', 
        name: 'contact',
        component: () => import('../pages/ContactPage.vue') 
      }
    ]
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('../pages/ErrorNotFound.vue')
  }
]

export default routes