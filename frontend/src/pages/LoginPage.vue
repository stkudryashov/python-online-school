<template>
  <section class="flex flex-1 mt-40">
    <!-- Login Form -->
    <div class="flex flex-col items-center p-4 mx-auto w-80 bg-gray-100 rounded-2xl drop-shadow-xl max-h-72 dark:bg-gray-800">
      <div class="text-xl text-black font-medium mb-4 dark:text-white">
        <span>Вход в систему</span>
      </div>

      <!-- Email Input -->
      <div class="w-56 relative flex-shrink-0 mb-4">
        <input
            v-model="loginForm.email"
            @keyup.enter="login"
            type="email"
            class="input-field"
            placeholder="Email"
        >
        <div class="absolute top-0 left-0 w-8 h-full flex justify-center items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
      </div>

      <!-- Password Input -->
      <div class="w-56 relative flex-shrink-0 mb-4">
        <input
            v-model="loginForm.password"
            @keyup.enter="login"
            type="password"
            class="input-field"
            placeholder="Пароль"
        >
        <div class="absolute top-0 left-0 w-8 h-full flex justify-center items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
          </svg>
        </div>
      </div>

      <button class="login-button" :class="{ 'shake-animation': hasErrors }" type="button" @click="login">
        Войти
      </button>

      <!-- Register Link -->
      <div class="text-xs text-black font-medium mt-12 dark:text-white">
        <span>Еще нет профиля? <a class="underline cursor-pointer">Зарегистрируйтесь</a></span>
      </div>
    </div>

    <!-- Image Block -->
    <div class="flex flex-col mx-auto">
      <div class="text-xl text-black font-medium mb-4 dark:text-white">
        <span>Изучай новое на Python Online School</span>
      </div>

      <div>
        <img src="/images/image.jpg" alt="login" class="h-96 w-96 rounded-3xl drop-shadow-xl">
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      loginForm: {
        email: '',
        password: ''
      },
      hasErrors: false
    }
  },
  methods: {
    /* Метод для входа в аккаунт */
    login() {
      const payload = {
        email: this.loginForm.email,
        password: this.loginForm.password
      }

      this.$store.dispatch('AuthModule/onLogin', payload)
        .then(() => {
          location.reload()
        })
        .catch(error => {
          console.log(error)
          this.hasErrors = true
          setTimeout(() => { this.hasErrors = false }, 1000)
        })
    }
  }
}
</script>

<style scoped>
.input-field {
  @apply w-full h-8 pr-4 pl-8 border bg-gray-100 rounded-lg focus:outline-none focus:border-blue-500;
}

.login-button {
  @apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 w-56 rounded-lg;
}

.shake-animation {
  animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both;
  transform: translate3d(0, 0, 0);
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
