<template>
  <Component :is="layout" :class="{ 'dark': isDarkMode }">
    <RouterView />
  </Component>
</template>

<script>
import DefaultLayout from './layouts/DefaultLayout.vue'

export default {
  components: {
    DefaultLayout,
  },
  computed: {
    layout() {
      return this.$route.meta.layout || 'default-layout'
    },
    isDarkMode() {
      const body = document.body

      const darkModeStatus = this.$store.getters['ThemeModule/isDarkMode']

      if (darkModeStatus) {
        body.classList.remove('bg-gray-200')
        body.classList.add('bg-gray-900')
      } else {
        body.classList.remove('bg-gray-900')
        body.classList.add('bg-gray-200')
      }

      return darkModeStatus
    }
  }
}
</script>

<style>
body {
  font-family: Helvetica, Tahoma, Arial, sans-serif;
}

.layout-base {
  @apply flex flex-col min-h-screen;
}
.layout-content {
  @apply flex flex-1;
}
</style>
