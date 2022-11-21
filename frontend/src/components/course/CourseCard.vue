<template>
  <div class="course-card bg-gray-100 dark:bg-gray-800 hover:from-fuchsia-300 hover:to-fuchsia-200 dark:hover:from-fuchsia-800 dark:hover:to-fuchsia-500">
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
  @apply flex flex-col rounded-2xl drop-shadow-xl p-2 w-72 h-36 mr-4 mb-4
  hover:bg-gradient-to-tl hover:scale-105 text-clip overflow-hidden
  transition-all ease-in-out duration-300;
}
</style>
