<template>
  <section class="container mx-auto mt-16">
    <h1 class="text-2xl">Наши курсы</h1>
    <div class="flex flex-wrap mt-2">
      <CourseCard v-for="course in courses"
                  :key="course.id"
                  :title="course.title"
                  :description="course.description"
      />
    </div>
  </section>
</template>

<script>
import CourseCard from '../components/course/CourseCard.vue'
import { CoursesAPI } from '../api/courses/index.js'

export default {
  name: 'MainPage',
  components: {
    CourseCard
  },
  data() {
    return {
      courses: [
        {
          id: 1,
          title: 'Test 1',
          description: 'Test 1'
        },
      ]
    }
  },
  methods : {
    loadCourses() {
      CoursesAPI.loadCourses()
        .then(response => {
          console.log(response.data)
          this.courses = response.data})
        .catch(error => {
          console.log(error)})
    }
  },
  created() {
    this.loadCourses()
  }
}
</script>

<style scoped>

</style>
