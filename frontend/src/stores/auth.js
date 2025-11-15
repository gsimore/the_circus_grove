import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '../api'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const accessToken = ref(localStorage.getItem('accessToken'))
  const refreshToken = ref(localStorage.getItem('refreshToken'))
  const isAuthenticated = computed(() => !!accessToken.value)

  async function login(credentials) {
    try {
      const response = await authApi.login(credentials)
      accessToken.value = response.data.access
      refreshToken.value = response.data.refresh
      
      localStorage.setItem('accessToken', response.data.access)
      localStorage.setItem('refreshToken', response.data.refresh)
      
      await fetchProfile()
      return response.data
    } catch (error) {
      throw error
    }
  }

  async function register(userData) {
    try {
      await authApi.register(userData)
      // After registration, automatically log in
      await login({
        username: userData.username,
        password: userData.password,
      })
    } catch (error) {
      throw error
    }
  }

  async function fetchProfile() {
    try {
      const response = await authApi.getProfile()
      user.value = response.data
      return response.data
    } catch (error) {
      throw error
    }
  }

  async function updateProfile(data) {
    try {
      const response = await authApi.updateProfile(data)
      user.value = response.data
      return response.data
    } catch (error) {
      throw error
    }
  }

  function logout() {
    user.value = null
    accessToken.value = null
    refreshToken.value = null
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
  }

  return {
    user,
    accessToken,
    refreshToken,
    isAuthenticated,
    login,
    register,
    fetchProfile,
    updateProfile,
    logout,
  }
})
