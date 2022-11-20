<template>
  <Component :is="layout">
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
    }
  }
}
</script>

<style>
body {
  font-family: Helvetica, Arial, sans-serif;
}

.layout-base {
  @apply flex flex-col min-h-screen;
}
.layout-content {
  @apply flex flex-1;
}
</style>
