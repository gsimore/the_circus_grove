import apiClient from './client'

export const nutritionApi = {
  getMeals(params) {
    return apiClient.get('/api/nutrition/meals/', { params })
  },
  
  getMeal(id) {
    return apiClient.get(`/api/nutrition/meals/${id}/`)
  },
  
  createMeal(data) {
    return apiClient.post('/api/nutrition/meals/', data)
  },
  
  updateMeal(id, data) {
    return apiClient.patch(`/api/nutrition/meals/${id}/`, data)
  },
  
  deleteMeal(id) {
    return apiClient.delete(`/api/nutrition/meals/${id}/`)
  },
  
  getFoods(mealId) {
    return apiClient.get(`/api/nutrition/meals/${mealId}/foods/`)
  },
  
  addFood(mealId, data) {
    return apiClient.post(`/api/nutrition/meals/${mealId}/foods/`, data)
  },
  
  // Nutrition Plans
  getPlans(params) {
    return apiClient.get('/api/nutrition/plans/', { params })
  },
  
  getPlan(id) {
    return apiClient.get(`/api/nutrition/plans/${id}/`)
  },
  
  createPlan(data) {
    return apiClient.post('/api/nutrition/plans/', data)
  },
  
  updatePlan(id, data) {
    return apiClient.patch(`/api/nutrition/plans/${id}/`, data)
  },
  
  deletePlan(id) {
    return apiClient.delete(`/api/nutrition/plans/${id}/`)
  },
  
  getPlanMeals(planId) {
    return apiClient.get(`/api/nutrition/plans/${planId}/meals/`)
  },
  
  addPlanMeal(planId, data) {
    return apiClient.post(`/api/nutrition/plans/${planId}/meals/`, data)
  },
}
