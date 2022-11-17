import { loginRequest, defaultRequest } from '../config.js'

export const AuthAPI = {
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
