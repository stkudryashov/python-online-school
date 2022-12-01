<template>
  <section class="container mx-auto mt-16 dark:text-white">
    <!-- Course Info -->
    <div class="text-2xl">{{ course.title }}</div>
    <div class="text-xl">{{ course.description }}</div>

    <!-- Modules List -->
    <div class="flex flex-col mt-4">
      <div v-for="(module, index) in course.modules" :key="module.id" class="module-card bg-gray-100 dark:bg-gray-800">
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
          this.course = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created() {
    this.getCourse()
  }
}
</script>

<style scoped>
.module-card {
  @apply rounded-2xl p-2 mb-2 w-3/5 hover:translate-x-10 transition-all ease-in-out duration-500
}
</style>
