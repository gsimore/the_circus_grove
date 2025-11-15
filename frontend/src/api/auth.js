import apiClient from './client'

export const authApi = {
  login(credentials) {
    return apiClient.post('/api/auth/token/', credentials)
  },
  
  register(userData) {
    return apiClient.post('/api/users/register/', userData)
  },
  
  refreshToken(refreshToken) {
    return apiClient.post('/api/auth/token/refresh/', { refresh: refreshToken })
  },
  
  getProfile() {
    return apiClient.get('/api/users/profile/')
  },
  
  updateProfile(data) {
    return apiClient.patch('/api/users/profile/', data)
  },
}
