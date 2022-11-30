<template>
  <div class="flex justify-center">
    <div class="m-8 bg-gray-100 dark:bg-gray-800 rounded-2xl drop-shadow-2xl p-8">
      <!-- Profile Form -->
      <div class="flex justify-between mb-4">
        <!-- First Name Input -->
        <div class="w-56 relative flex-shrink-0 mr-2">
          <input
              v-model="profileUser.first_name"
              type="text"
              class="input-field"
              placeholder="Имя"
          >
          <div class="absolute top-0 left-0 w-8 h-full flex justify-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>

        <!-- Last Name Input -->
        <div class="w-56 relative flex-shrink-0 ml-2">
          <input
              v-model="profileUser.last_name"
              type="text"
              class="input-field"
              placeholder="Фамилия"
          >
          <div class="absolute top-0 left-0 w-8 h-full flex justify-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="flex">
        <!-- About Me Input -->
        <div class="flex-1 relative flex-shrink-0">
          <textarea
              v-model="profileInfo.about_me"
              type="text"
              class="text-area"
              maxlength="256"
              placeholder="Обо мне"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ProfileAPI } from "../../api/accounts/index.js";

export default {
  name: 'PersonalPageProfile',
  data() {
    return {
      profileUser: {
        first_name: '',
        last_name: '',
      },
      profileInfo: {
        date_of_birth: '',
        phone_number: '',
        about_me: ''
      }
    }
  },
  methods : {
    /* Получение информации о профиле */
    loadProfileInfo() {
      ProfileAPI.getProfile()
        .then(response => {
          console.log(response.data)
          this.profileInfo = response.data})
        .catch(error => {
          console.log(error)})
    },
    fillProfileUser() {
      this.profileUser.first_name = this.user.first_name
      this.profileUser.last_name = this.user.last_name
    }
  },
  computed: {
    /* Получение информации об аккаунте */
    user() {
      return this.$store.getters['AuthModule/getUserInfo']
    },
  },
  created() {
    this.fillProfileUser()
    this.loadProfileInfo()
  }
}
</script>

<style scoped>
.input-field {
  @apply w-full h-8 pr-4 pl-8 border bg-gray-100 rounded-lg focus:outline-none focus:border-blue-500;
}

.text-area {
  @apply w-full h-32 p-2 border bg-gray-100 rounded-lg focus:outline-none focus:border-blue-500;
}
</style>
