<template>
  <section class="container mx-auto mt-16">
    <div class="text-2xl">{{ course.title }}</div>
    <div class="text-xl">{{ course.description }}</div>
    <div class="flex flex-col mt-4">
      <div v-for="(module, index) in course.modules" :key="module.id" class="bg-gray-100 rounded-2xl p-2 mb-2 w-3/5">
        <div>{{ index + 1 }}. {{ module.title }}</div>
        <div>{{ module.description }}</div>
      </div>
    </div>
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
        modules: [
          {
            title: '',
            description: '',
          }
        ]
      }
    }
  },
  methods: {
    /* Получить курс по параметру из ссылки */
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
