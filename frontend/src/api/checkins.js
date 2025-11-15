import apiClient from './client'

export const checkinsApi = {
  getCheckins(params) {
    return apiClient.get('/api/checkins/', { params })
  },
  
  getCheckin(id) {
    return apiClient.get(`/api/checkins/${id}/`)
  },
  
  createCheckin(data) {
    return apiClient.post('/api/checkins/', data)
  },
  
  updateCheckin(id, data) {
    return apiClient.patch(`/api/checkins/${id}/`, data)
  },
  
  deleteCheckin(id) {
    return apiClient.delete(`/api/checkins/${id}/`)
  },
}
