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
}
