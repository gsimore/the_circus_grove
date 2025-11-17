import { defineStore } from 'pinia'
import { ref } from 'vue'
import { nutritionApi } from '../api'

export const useNutritionStore = defineStore('nutrition', () => {
  const meals = ref([])
  const currentMeal = ref(null)
  const loading = ref(false)

  async function fetchMeals(params) {
    loading.value = true
    try {
      const response = await nutritionApi.getMeals(params)
      meals.value = response.data.results || response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function fetchMeal(id) {
    loading.value = true
    try {
      const response = await nutritionApi.getMeal(id)
      currentMeal.value = response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function createMeal(data) {
    loading.value = true
    try {
      const response = await nutritionApi.createMeal(data)
      meals.value.unshift(response.data)
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function updateMeal(id, data) {
    loading.value = true
    try {
      const response = await nutritionApi.updateMeal(id, data)
      const index = meals.value.findIndex(m => m.id === id)
      if (index !== -1) {
        meals.value[index] = response.data
      }
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function deleteMeal(id) {
    loading.value = true
    try {
      await nutritionApi.deleteMeal(id)
      meals.value = meals.value.filter(m => m.id !== id)
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  // Nutrition Plans
  const plans = ref([])
  const currentPlan = ref(null)

  async function fetchPlans(params) {
    loading.value = true
    try {
      const response = await nutritionApi.getPlans(params)
      plans.value = response.data.results || response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function fetchPlan(id) {
    loading.value = true
    try {
      const response = await nutritionApi.getPlan(id)
      currentPlan.value = response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function createPlan(data) {
    loading.value = true
    try {
      const response = await nutritionApi.createPlan(data)
      plans.value.unshift(response.data)
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function updatePlan(id, data) {
    loading.value = true
    try {
      const response = await nutritionApi.updatePlan(id, data)
      const index = plans.value.findIndex(p => p.id === id)
      if (index !== -1) {
        plans.value[index] = response.data
      }
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function deletePlan(id) {
    loading.value = true
    try {
      await nutritionApi.deletePlan(id)
      plans.value = plans.value.filter(p => p.id !== id)
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  return {
    meals,
    currentMeal,
    plans,
    currentPlan,
    loading,
    fetchMeals,
    fetchMeal,
    createMeal,
    updateMeal,
    deleteMeal,
    fetchPlans,
    fetchPlan,
    createPlan,
    updatePlan,
    deletePlan,
  }
})
