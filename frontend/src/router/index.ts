import { createRouter, createWebHistory, RouteRecordRaw, } from 'vue-router'
import LoginScreen from '../views/LoginScreen.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "retro" */ '../views/AddFeedback.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginScreen,
  },
  {
    path: '/feedbacks',
    name: 'feedbacks',
    component: () => import(/* webpackChunkName: "retro" */ '../views/ReadFeedbacks.vue'),
  },
  {
    path: '/write-feedback',
    name: 'write-feedback',
    component: () => import(/* webpackChunkName: "retro" */ '../views/AddFeedback.vue'),
  },
  {
    path: '/show-participants',
    name: 'show-participants',
    component: () => import(/* webpackChunkName: "retro" */ '../views/ShowParticipants.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
