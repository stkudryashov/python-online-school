import { createRouter, createWebHistory } from 'vue-router'

import store from '../store/index.js'

import MainPage from '../pages/MainPage.vue'
import LoginPage from '../pages/LoginPage.vue'
import CoursePage from '../pages/CoursePage.vue'

import PersonalPage from '../pages/personal/PersonalPage.vue'
import PersonalPageInfo from '../pages/personal/PersonalPageInfo.vue'
import PersonalPageCourses from '../pages/personal/PersonalPageCourses.vue'

import PageNotFound from '../pages/PageNotFound.vue'


const routes = [
  {
    path: '/',
    name: 'Index',
    component: MainPage
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/personal',
    name: 'Personal',
    component: PersonalPage,
    children: [
      {
        path: 'info',
        name: 'PersonalInfo',
        component: PersonalPageInfo,
      },
      {
        path: 'courses',
        name: 'PersonalCourses',
        component: PersonalPageCourses,
      }
    ]
  },
  {
    path: '/courses/:courseId',
    name: 'CourseView',
    component: CoursePage,
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'PageNotFound',
    component: PageNotFound,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to, from, next) => {
  /* Проверка на авторизацию пользователя */
  await store.dispatch('AuthModule/onVerify')

  /* Получение токена из localStorage */
  const isAuthenticated = localStorage.getItem('token')

  if (to.name === 'Login' && isAuthenticated) {
    next({name: 'Index'})
  }
  else next()
})

export default router
