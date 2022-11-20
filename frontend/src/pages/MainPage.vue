<template>
  <section class="container mx-auto mt-16">
    <div>
      <div class="text-5xl cursor-default">
        <div class="bg-purple-200 rounded-full h-96 w-96 absolute -top-12 -left-20 -z-10"></div>
        <h2 class="text-xl mb-4">Образовательная платформа</h2>

        <div class="flex justify-between mb-12">
          <div>
            <div>
              <p>Подробно рассказываем</p>
              <p>про <span class="python-word">Python</span></p>
            </div>

            <div class="mt-28 text-xl">
              <ul class="list-disc">
                <li>групповые занятия для детей от 12 лет</li>
                <li>индивидуальный подход к каждому студенту</li>
                <li>дополнительные разборы учебного материала</li>
              </ul>
            </div>
          </div>

          <div class="relative">
            <img src="/images/snake.jpg" alt="logo" class="mr-60 logo-image">
            <div class="bg-blue-200 rounded-full h-80 w-80 absolute top-0 left-60 -z-10"></div>
          </div>
        </div>

        <hr class="h-0.5 bg-gray-400">
      </div>
    </div>

    <div class="mt-8">
      <h2 class="text-3xl">Наши курсы</h2>
      <div class="flex flex-wrap mt-4">
        <router-link v-for="course in courses"
                     :key="course.id"
                     :to="{name: 'CourseView', params: {courseId: course.id}}"
        >
          <CourseCard :id="course.id" :title="course.title" :description="course.description"/>
        </router-link>
      </div>
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
.logo-image {
  @apply h-80 w-80 rounded-full z-10 hover:rotate-12 transition ease-in-out duration-500
}

.python-word {
  @apply text-blue-400 hover:text-blue-600 transition ease-in-out duration-300
}
</style>
