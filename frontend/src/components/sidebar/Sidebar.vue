<template>
  <aside class="bg-white text-black w-64 dark:text-white dark:bg-gray-800" :class="{ 'w-12': isCollapsed }" style="transition: width 0.5s ease">
    <div class="flex flex-col">
      <!-- Collapse Button -->
      <div @click="sidebarShow"
           class="flex items-center justify-end px-3 h-12 text-gray-500 hover:text-black dark:hover:text-white">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 h-8 sidebar-icon" :class="{ 'rotate-180': isCollapsed }" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M11 19l-7-7 7-7m8 14l-7-7 7-7" />
        </svg>
      </div>

      <!-- Sidebar Items -->
      <slot />
    </div>
  </aside>
</template>

<script>
import SidebarItem from './SidebarItem.vue'

export default {
  name: 'Sidebar',
  components: {
    SidebarItem
  },
  computed: {
    /* Получение статуса бара */
    isCollapsed() {
      return this.$store.getters['SidebarModule/getSidebarStatus']
    }
  },
  methods: {
    /* Изменение состояния бара */
    sidebarShow() {
      this.$store.dispatch('SidebarModule/changeSidebarStatus')
    }
  }
}
</script>

<style scoped>
.sidebar-icon {
  transition: 0.5s ease;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.5s ease;
}
</style>
