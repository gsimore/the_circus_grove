import { defineStore } from 'pinia'
import { ref } from 'vue'
import { trainingApi } from '../api'

export const useTrainingStore = defineStore('training', () => {
  const sessions = ref([])
  const currentSession = ref(null)
  const loading = ref(false)

  async function fetchSessions(params) {
    loading.value = true
    try {
      const response = await trainingApi.getSessions(params)
      sessions.value = response.data.results || response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function fetchSession(id) {
    loading.value = true
    try {
      const response = await trainingApi.getSession(id)
      currentSession.value = response.data
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function createSession(data) {
    loading.value = true
    try {
      const response = await trainingApi.createSession(data)
      sessions.value.unshift(response.data)
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function updateSession(id, data) {
    loading.value = true
    try {
      const response = await trainingApi.updateSession(id, data)
      const index = sessions.value.findIndex(s => s.id === id)
      if (index !== -1) {
        sessions.value[index] = response.data
      }
      return response.data
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  async function deleteSession(id) {
    loading.value = true
    try {
      await trainingApi.deleteSession(id)
      sessions.value = sessions.value.filter(s => s.id !== id)
    } catch (error) {
      throw error
    } finally {
      loading.value = false
    }
  }

  return {
    sessions,
    currentSession,
    loading,
    fetchSessions,
    fetchSession,
    createSession,
    updateSession,
    deleteSession,
  }
})
