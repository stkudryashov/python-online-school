<template>
  <div class="header-item hover:bg-gray-200 dark:hover:bg-gray-900">
    <div v-if="prepend" class="header-item-icon mr-2">
      <slot />
    </div>

    <span class="truncate">
      {{ title }}
    </span>

    <div v-if="!prepend" class="header-item-icon ml-2">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheHeaderItem',
  props: {
    title: {
      type: String,
      required: true
    },
    prepend: {
      type: Boolean,
      default: true
    }
  }
}
</script>

<style scoped>
.header-item {
  @apply flex items-center cursor-pointer px-3 h-16 hover:h-12 hover:rounded-full;
}

.header-item-icon {
  @apply flex items-center;
}
</style>
