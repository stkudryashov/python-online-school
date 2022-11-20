<template>
  <div class="sidebar-item">
    <div v-if="prepend" class="sidebar-item-icon mr-2">
      <slot />
    </div>

    <span class="truncate" :class="{ 'sidebar-item-hidden': isCollapsed }">
      {{ title }}
    </span>

    <div v-if="!prepend" class="sidebar-item-icon ml-2">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'SidebarItem',
  props: {
    title: {
      type: String,
      required: true
    },
    prepend: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    isCollapsed() {
      return this.$store.getters['SidebarModule/getSidebarStatus']
    }
  },
}
</script>

<style scoped>
.sidebar-item {
  @apply flex items-center hover:h-12 hover:bg-gray-200 cursor-pointer px-3 h-12;
}

.sidebar-item-icon {
  @apply flex items-center;
}

.sidebar-item-hidden {
  opacity: 0;
  transition: opacity 0.5s ease;
}
</style>
