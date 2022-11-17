import axios from 'axios'

const loginConfig = {
  baseURL: 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json'
  }
}

export const loginRequest = axios.create(loginConfig)

const defaultConfig = {
  baseURL: 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json'
  }
}

const token = localStorage.getItem('token')
if (token) defaultConfig.headers['Authorization'] = `Bearer ${token}`

export const defaultRequest = axios.create(defaultConfig)
