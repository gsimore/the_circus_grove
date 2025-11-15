import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/dashboard',
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/auth/LoginView.vue'),
      meta: { requiresGuest: true },
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/auth/RegisterView.vue'),
      meta: { requiresGuest: true },
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/training',
      name: 'training',
      component: () => import('../views/training/TrainingListView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/training/:id',
      name: 'training-detail',
      component: () => import('../views/training/TrainingDetailView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/nutrition',
      name: 'nutrition',
      component: () => import('../views/nutrition/NutritionListView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/nutrition/:id',
      name: 'nutrition-detail',
      component: () => import('../views/nutrition/NutritionDetailView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/checkins',
      name: 'checkins',
      component: () => import('../views/checkins/CheckinsListView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
      meta: { requiresAuth: true },
    },
  ],
})

// Navigation guards
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'login' })
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next({ name: 'dashboard' })
  } else {
    next()
  }
})

export default router
