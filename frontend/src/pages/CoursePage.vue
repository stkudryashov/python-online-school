<template>
  <section class="container mx-auto mt-16">
    <div>{{ course.title }}</div>
  </section>
</template>

<script>
import { CoursesAPI } from '../api/courses/index.js'

export default {
  name: 'CoursePage',
  data() {
    return {
      course: {
        title: '',
        description: '',
      }
    }
  },
  methods: {
    getCourse() {
      const courseId = this.$route.params.courseId

      CoursesAPI.getCourse(courseId)
        .then(response => {
          console.log(response.data)
          this.course = response.data})
        .catch(error => {
          console.log(error)})
    }
  },
  created() {
    this.getCourse()
  }
}
</script>

<style scoped>

</style>