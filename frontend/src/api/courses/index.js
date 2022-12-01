import { defaultRequest } from '../config.js'

export const CoursesAPI = {
  /* API для курсов */
  loadCourses() {
    const url = '/courses/'
    return defaultRequest.get(url)
  },
  getCourse(courseId) {
    const url = `/courses/${courseId}/`
    return defaultRequest.get(url)
  }
}
