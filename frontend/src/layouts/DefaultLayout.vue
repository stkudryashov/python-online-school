<template>
  <div class="layout-base">
    <TheHeader />

    <!-- Main Content -->
    <main class="layout-content">
      <Slot />
    </main>
  </div>
</template>

<script>
import TheHeader from '../components/header/TheHeader.vue'

export default {
  name: 'MainLayout',
  components: {
    TheHeader
  }
}
</script>

<style scoped>

</style>
