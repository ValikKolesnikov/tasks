// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import store from './store/index'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import Login from '@/components/accounts/Login'
import SignUp from '@/components/accounts/SignUp'
import CoursesList from '@/components/courses/CoursesList'
import Home from '@/components/Home'
import UpdateUser from '@/components/accounts/UpdateUser'
import UserPage from '@/components/accounts/UserPage'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueRouter)
Vue.config.productionTip = false

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: SignUp
  },
  {
    path: '/update',
    name: 'update',
    component: UpdateUser
  },
  {
    path: '/courses',
    name: 'coursesList',
    component: CoursesList
  },
  {
    path: '/user-page',
    name: 'userPage',
    component: UserPage
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  store,
  components: {App},
  template: '<App/>'
})
