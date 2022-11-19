<template>
  <div class="course-card">
    <div class="text-xl">{{ title }}</div>
    <div>{{ description }}</div>
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
  @apply flex flex-col bg-gray-100 rounded-2xl drop-shadow-xl p-2 w-56 h-36 mr-4 mb-4 hover:bg-gradient-to-tl hover:from-fuchsia-400 hover:to-fuchsia-200;
}

</style>