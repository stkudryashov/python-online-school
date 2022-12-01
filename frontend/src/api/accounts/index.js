import { loginRequest, defaultRequest } from '../config.js'

export const AuthAPI = {
  /* API для авторизации */
  login(email, password) {
    const url = '/accounts/login/'
    const data = { email, password }
    return loginRequest.post(url, data)
  },
  verify() {
    const url = '/accounts/login/verify/'
    return defaultRequest.get(url)
  }
}

export const ProfileAPI = {
  /* API для профиля */
  getProfile() {
    const url = '/accounts/profile/'
    return defaultRequest.get(url)
  },
  saveProfile(data) {
    const url = '/accounts/profile/'
    return defaultRequest.put(url, data)
  }
}
