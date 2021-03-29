import Vuex from 'vuex'
import Vue from 'vue'
import accounts from './modules/accounts'
import courses from './modules/courses'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accounts,
    courses
  }
})
