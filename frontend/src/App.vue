<template>
  <TheHeader />
  <router-view />
</template>

<script>
import TheHeader from './components/header/TheHeader.vue';

export default {
  components: {
    TheHeader,
  },
  computed: {
  }
}
</script>

<style>
body {
  font-family: Helvetica, Arial, sans-serif;
}
</style>
