<template>
  <header class="bg-white shadow-2xl text-black dark:bg-gray-800 dark:text-white transition-colors ease-in-out duration-300">
    <div class="container mx-auto text-sm">
      <div class="flex justify-between items-center flex-wrap">
        <!-- Header Sections -->
        <div class="flex items-center flex-wrap">
          <!-- Logo -->
          <router-link :to="{name: 'Index'}" class="flex flex-shrink-0 items-center block w-46 mr-12">
            <img src="/favicon.svg" alt="Logo" class="h-8 mr-3">
            <span>Python Online School</span>
          </router-link>

          <!-- Courses -->
          <TheHeaderItem title="Наши курсы">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" />
            </svg>
          </TheHeaderItem>

          <!-- Contacts -->
          <TheHeaderItem title="Контакты">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
          </TheHeaderItem>
        </div>

        <!-- Personal Area -->
        <div class="flex items-center">
          <!-- User -->
          <router-link :to="{name: 'Personal'}" v-if="token">
            <TheHeaderItem :title="user.email" :prepend="false">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
            </TheHeaderItem>
          </router-link>

          <!-- Logout -->
          <router-link :to="{name: 'Login'}" v-if="token" v-on:click="logout">
            <TheHeaderItem title="Выход" :prepend="false">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15m3 0l3-3m0 0l-3-3m3 3H9" />
              </svg>
            </TheHeaderItem>
          </router-link>

          <!-- Login / Register -->
          <router-link :to="{name: 'Login'}" v-if="!token">
            <TheHeaderItem title="Войти" :prepend="false">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15m3 0l3-3m0 0l-3-3m3 3H9" />
              </svg>
            </TheHeaderItem>
          </router-link>

          <ThemeSwitcher class="ml-4" />
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import TheHeaderItem from './TheHeaderItem.vue'
import ThemeSwitcher from '../ThemeSwitcher.vue'

export default {
  name: 'TheHeader',
  components: {
    ThemeSwitcher,
    TheHeaderItem,
  },
  methods: {
    /* Метод для выхода из аккаунта */
    logout() {
      this.$store.dispatch('AuthModule/onLogout')
        .then(() => {
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  computed: {
    /* Получение информации об аккаунте */
    user() {
      return this.$store.getters['AuthModule/getUserInfo']
    },
    /* Получение токена пользователя для проверки авторизации */
    token() {
      return this.$store.getters['AuthModule/getUserToken']
    }
  }
}
</script>

<style scoped>

</style>
