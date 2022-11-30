<template>
  <div class="flex justify-center">
    <!-- Profile Form -->
    <div class="m-8 bg-gray-100 dark:bg-gray-800 rounded-2xl drop-shadow-2xl p-8">
      <div class="text-xl text-black font-medium mb-4 dark:text-white">
        <span>Личная информация</span>
      </div>

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

      <div class="flex justify-between mb-4">
        <!-- Date Of Birth Input -->
        <div class="w-56 relative flex-shrink-0 mr-2">
          <input
              v-model="profileInfo.date_of_birth"
              type="date"
              class="input-field"
          >
          <div class="absolute top-0 left-0 w-8 h-full flex justify-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5m-9-6h.008v.008H12v-.008zM12 15h.008v.008H12V15zm0 2.25h.008v.008H12v-.008zM9.75 15h.008v.008H9.75V15zm0 2.25h.008v.008H9.75v-.008zM7.5 15h.008v.008H7.5V15zm0 2.25h.008v.008H7.5v-.008zm6.75-4.5h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V15zm0 2.25h.008v.008h-.008v-.008zm2.25-4.5h.008v.008H16.5v-.008zm0 2.25h.008v.008H16.5V15z" />
            </svg>
          </div>
        </div>

        <!-- Phone Number Input -->
        <div class="w-56 relative flex-shrink-0 ml-2">
          <input
              v-model="profileInfo.phone_number"
              type="tel"
              class="input-field"
              placeholder="Номер телефона"
          >
          <div class="absolute top-0 left-0 w-8 h-full flex justify-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" />
            </svg>

          </div>
        </div>
      </div>

      <div class="flex mb-4">
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

      <button
          class="login-button float-right"
          :class="{ 'shake-animation': hasErrors, 'success-animation': isSuccess }"
          type="button"
          @click="saveProfile">
        Сохранить
      </button>
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
      },
      hasErrors: false,
      isSuccess: false
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
    },
    saveProfile() {
      const payload = {
        user: {
          first_name: this.profileUser.first_name,
          last_name: this.profileUser.last_name,
        },
        ...this.profileInfo
      }

      ProfileAPI.saveProfile(payload)
        .then(response => {
          console.log(response.data)
          this.isSuccess = true
          setTimeout(() => { this.isSuccess = false }, 1000)
        })
        .catch(error => {
          console.log(error)
          this.hasErrors = true
          setTimeout(() => { this.hasErrors = false }, 1000)
        })
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
  @apply w-full h-32 pl-2 pt-1 border bg-gray-100 rounded-lg focus:outline-none focus:border-blue-500;
}

.login-button {
  @apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 w-56 rounded-lg
  transition-colors ease-in-out duration-500;
}

.shake-animation {
  animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both;
  transform: translate3d(0, 0, 0);
}

.success-animation {
  background-color: forestgreen;
}

.success-animation:hover {
  background-color: forestgreen;
}

@keyframes shake {
  10%, 90% {
    transform: translate3d(-1px, 0, 0);
  }
  20%, 80% {
    transform: translate3d(2px, 0, 0);
  }
  30%, 50%, 70% {
    transform: translate3d(-4px, 0, 0);
  }
  40%, 60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>
