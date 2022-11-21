<template>
  <div class="course-card">
    <div class="text-xl">{{ title }}</div>
    <div class="text-sm">{{ description }}</div>
  </div>
</template>

<script>
export default {
  name: 'CourseCard',
  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
.course-card {
  @apply flex flex-col bg-gray-100 rounded-2xl drop-shadow-xl p-2 w-72 h-36 mr-4 mb-4
  hover:bg-gradient-to-tl hover:from-fuchsia-300 hover:to-fuchsia-200 hover:scale-105
  text-clip overflow-hidden transition-all ease-in-out duration-300;
}
</style>
