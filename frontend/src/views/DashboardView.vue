<template>
  <div class="min-h-screen bg-gray-50">
    <nav class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex space-x-8">
            <router-link to="/dashboard" class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900">
              Dashboard
            </router-link>
            <router-link to="/training" class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 hover:text-gray-900">
              Training
            </router-link>
            <router-link to="/nutrition" class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 hover:text-gray-900">
              Nutrition
            </router-link>
            <router-link to="/checkins" class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 hover:text-gray-900">
              Check-ins
            </router-link>
          </div>
          <div class="flex items-center space-x-4">
            <router-link to="/profile" class="text-sm font-medium text-gray-500 hover:text-gray-900">
              Profile
            </router-link>
            <button @click="handleLogout" class="text-sm font-medium text-gray-500 hover:text-gray-900">
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <h1 class="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>
        
        <!-- Training Plans Section -->
        <div class="mb-8">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-gray-900">Training Plans</h2>
            <router-link to="/training" class="text-sm text-blue-600 hover:text-blue-800">
              View All →
            </router-link>
          </div>
          
          <div v-if="trainingStore.loading" class="text-center py-8">
            <p class="text-gray-500">Loading training plans...</p>
          </div>
          
          <div v-else-if="activeTrainingPlans.length === 0" class="bg-white shadow rounded-lg p-6">
            <p class="text-gray-500 text-center">No active training plans. Your coach will assign you a plan.</p>
          </div>
          
          <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <router-link
              v-for="plan in activeTrainingPlans"
              :key="plan.id"
              :to="`/training/plans/${plan.id}`"
              class="bg-white overflow-hidden shadow rounded-lg hover:shadow-lg transition-shadow"
            >
              <div class="p-5">
                <div class="flex items-center justify-between mb-3">
                  <h3 class="text-lg font-semibold text-gray-900">{{ plan.name }}</h3>
                  <span v-if="plan.is_active" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                    Active
                  </span>
                </div>
                <p v-if="plan.description" class="text-sm text-gray-500 mb-3 line-clamp-2">{{ plan.description }}</p>
                <div class="flex items-center text-sm text-gray-500">
                  <svg class="h-4 w-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  <span>{{ formatDate(plan.start_date) }}</span>
                  <span v-if="plan.end_date" class="ml-2">- {{ formatDate(plan.end_date) }}</span>
                </div>
                <div v-if="plan.exercises && plan.exercises.length > 0" class="mt-3 text-sm text-gray-600">
                  <span class="font-medium">{{ plan.exercises.length }}</span> exercise{{ plan.exercises.length !== 1 ? 's' : '' }}
                </div>
              </div>
            </router-link>
          </div>
        </div>

        <!-- Nutrition Plans Section -->
        <div class="mb-8">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-gray-900">Nutrition Plans</h2>
            <router-link to="/nutrition" class="text-sm text-blue-600 hover:text-blue-800">
              View All →
            </router-link>
          </div>
          
          <div v-if="nutritionStore.loading" class="text-center py-8">
            <p class="text-gray-500">Loading nutrition plans...</p>
          </div>
          
          <div v-else-if="activeNutritionPlans.length === 0" class="bg-white shadow rounded-lg p-6">
            <p class="text-gray-500 text-center">No active nutrition plans. Your coach will assign you a plan.</p>
          </div>
          
          <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <router-link
              v-for="plan in activeNutritionPlans"
              :key="plan.id"
              :to="`/nutrition/plans/${plan.id}`"
              class="bg-white overflow-hidden shadow rounded-lg hover:shadow-lg transition-shadow"
            >
              <div class="p-5">
                <div class="flex items-center justify-between mb-3">
                  <h3 class="text-lg font-semibold text-gray-900">{{ plan.name }}</h3>
                  <span v-if="plan.is_active" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                    Active
                  </span>
                </div>
                <p v-if="plan.description" class="text-sm text-gray-500 mb-3 line-clamp-2">{{ plan.description }}</p>
                <div class="flex items-center text-sm text-gray-500 mb-3">
                  <svg class="h-4 w-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  <span>{{ formatDate(plan.start_date) }}</span>
                  <span v-if="plan.end_date" class="ml-2">- {{ formatDate(plan.end_date) }}</span>
                </div>
                <div class="grid grid-cols-3 gap-2 text-xs">
                  <div>
                    <div class="text-gray-500">Calories</div>
                    <div class="font-semibold text-gray-900">{{ plan.target_calories }}</div>
                  </div>
                  <div>
                    <div class="text-gray-500">Protein</div>
                    <div class="font-semibold text-gray-900">{{ plan.target_protein_g }}g</div>
                  </div>
                  <div>
                    <div class="text-gray-500">Carbs</div>
                    <div class="font-semibold text-gray-900">{{ plan.target_carbs_g }}g</div>
                  </div>
                </div>
                <div v-if="plan.meals && plan.meals.length > 0" class="mt-3 text-sm text-gray-600">
                  <span class="font-medium">{{ plan.meals.length }}</span> meal{{ plan.meals.length !== 1 ? 's' : '' }} scheduled
                </div>
              </div>
            </router-link>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="grid grid-cols-1 gap-6 sm:grid-cols-3">
          <router-link to="/checkins" class="bg-white overflow-hidden shadow rounded-lg hover:shadow-lg transition-shadow">
            <div class="p-5">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">Check-ins</dt>
                    <dd class="text-lg font-medium text-gray-900">Track Progress</dd>
                  </dl>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore, useTrainingStore, useNutritionStore } from '../stores'

const router = useRouter()
const authStore = useAuthStore()
const trainingStore = useTrainingStore()
const nutritionStore = useNutritionStore()

const activeTrainingPlans = computed(() => {
  return trainingStore.plans.filter(plan => plan.is_active)
})

const activeNutritionPlans = computed(() => {
  return nutritionStore.plans.filter(plan => plan.is_active)
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
}

onMounted(async () => {
  try {
    await Promise.all([
      trainingStore.fetchPlans(),
      nutritionStore.fetchPlans()
    ])
  } catch (error) {
    console.error('Error fetching plans:', error)
  }
})

const handleLogout = () => {
  authStore.logout()
  router.push({ name: 'login' })
}
</script>
