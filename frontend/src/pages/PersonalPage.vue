<template>
  <Sidebar>
    <SidebarItem title="Мой профиль">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
    </SidebarItem>

    <SidebarItem title="Мои курсы">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2" />
      </svg>
    </SidebarItem>
  </Sidebar>

  <section class="flex-1">

  </section>
</template>

<script>
import Sidebar from '../components/sidebar/Sidebar.vue'
import SidebarItem from '../components/sidebar/SidebarItem.vue'

export default {
  name: 'PersonalPage',
  components: {
    Sidebar,
    SidebarItem,
  },
  computed: {
    permissions() {
      return Array.from(this.$store.getters['AuthModule/getUserPermissions'])
    }
  },
}
</script>

<style scoped>

</style>
