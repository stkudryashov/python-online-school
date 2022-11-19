import { defaultRequest } from '../config.js'

export const CoursesAPI = {
  loadCourses() {
    const url = '/courses/'
    return defaultRequest.get(url)
  }
}
