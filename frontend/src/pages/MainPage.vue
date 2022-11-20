<template>
  <section class="container mx-auto mt-16">
    <h1 class="text-2xl">Наши курсы</h1>
    <div class="flex flex-wrap mt-2">
      <router-link v-for="course in courses"
                   :key="course.id"
                   :to="{name: 'CourseView', params: {courseId: course.id}}"
      >
        <CourseCard :id="course.id" :title="course.title" :description="course.description"/>
      </router-link>
    </div>
  </section>
</template>

<script>
import CourseCard from '../components/course/CourseCard.vue'
import { CoursesAPI } from '../api/courses/index.js'

import Sidebar from '../components/sidebar/Sidebar.vue'
import SidebarItem from '../components/sidebar/SidebarItem.vue'

export default {
  name: 'MainPage',
  components: {
    CourseCard,
    Sidebar,
    SidebarItem
  },
  data() {
    return {
      courses: [
        {
          id: 1,
          title: '',
          description: ''
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
