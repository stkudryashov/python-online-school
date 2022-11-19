<template>
  <section class="container mx-auto mt-16">
    <h1 class="text-2xl">Наши курсы</h1>
    <div class="flex flex-wrap mt-2">
      <CourseCard v-for="course in courses"
                  :key="course.title"
                  :title="course.title"
                  :description="course.description"
      />
    </div>
  </section>
</template>

<script>
import CourseCard from '../components/course/CourseCard.vue'

export default {
  name: 'MainPage',
  components: {
    CourseCard
  },
  data() {
    return {
      courses: [
        {
          title: 'Test 1',
          description: 'Test 1'
        },
        {
          title: 'Test 2',
          description: 'Test 2'
        },
        {
          title: 'Test 3',
          description: 'Test 3'
        },
        {
          title: 'Test 4',
          description: 'Test 4'
        },
      ]
    }
  },
}
</script>

<style scoped>

</style>