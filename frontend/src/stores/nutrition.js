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

  return {
    meals,
    currentMeal,
    loading,
    fetchMeals,
    fetchMeal,
    createMeal,
    updateMeal,
    deleteMeal,
  }
})
