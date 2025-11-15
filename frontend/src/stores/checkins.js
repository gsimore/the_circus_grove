import { defineStore } from 'pinia'
import { ref } from 'vue'
import { checkinsApi } from '../api'

export const useCheckinsStore = defineStore('checkins', () => {
  const checkins = ref([])
  const currentCheckin = ref(null)
  const loading = ref(false)

  async function fetchCheckins(params) {
    loading.value = true
    try {
      const response = await checkinsApi.getCheckins(params)
      checkins.value = response.data.results || response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function fetchCheckin(id) {
    loading.value = true
    try {
      const response = await checkinsApi.getCheckin(id)
      currentCheckin.value = response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function createCheckin(data) {
    loading.value = true
    try {
      const response = await checkinsApi.createCheckin(data)
      checkins.value.unshift(response.data)
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function updateCheckin(id, data) {
    loading.value = true
    try {
      const response = await checkinsApi.updateCheckin(id, data)
      const index = checkins.value.findIndex(c => c.id === id)
      if (index !== -1) {
        checkins.value[index] = response.data
      }
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function deleteCheckin(id) {
    loading.value = true
    try {
      await checkinsApi.deleteCheckin(id)
      checkins.value = checkins.value.filter(c => c.id !== id)
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  return {
    checkins,
    currentCheckin,
    loading,
    fetchCheckins,
    fetchCheckin,
    createCheckin,
    updateCheckin,
    deleteCheckin,
  }
})
