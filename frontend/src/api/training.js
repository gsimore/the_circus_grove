import apiClient from './client'

export const trainingApi = {
  getSessions(params) {
    return apiClient.get('/api/training/sessions/', { params })
  },
  
  getSession(id) {
    return apiClient.get(`/api/training/sessions/${id}/`)
  },
  
  createSession(data) {
    return apiClient.post('/api/training/sessions/', data)
  },
  
  updateSession(id, data) {
    return apiClient.patch(`/api/training/sessions/${id}/`, data)
  },
  
  deleteSession(id) {
    return apiClient.delete(`/api/training/sessions/${id}/`)
  },
  
  getExercises(sessionId) {
    return apiClient.get(`/api/training/sessions/${sessionId}/exercises/`)
  },
  
  addExercise(sessionId, data) {
    return apiClient.post(`/api/training/sessions/${sessionId}/exercises/`, data)
  },
  
  // Training Plans
  getPlans(params) {
    return apiClient.get('/api/training/plans/', { params })
  },
  
  getPlan(id) {
    return apiClient.get(`/api/training/plans/${id}/`)
  },
  
  createPlan(data) {
    return apiClient.post('/api/training/plans/', data)
  },
  
  updatePlan(id, data) {
    return apiClient.patch(`/api/training/plans/${id}/`, data)
  },
  
  deletePlan(id) {
    return apiClient.delete(`/api/training/plans/${id}/`)
  },
  
  getPlanExercises(planId) {
    return apiClient.get(`/api/training/plans/${planId}/exercises/`)
  },
  
  addPlanExercise(planId, data) {
    return apiClient.post(`/api/training/plans/${planId}/exercises/`, data)
  },
}
