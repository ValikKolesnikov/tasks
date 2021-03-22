import Vue from 'vue'
import Vuex from 'vuex'
import { Accounts } from '../api/accounts'
import { SET_AUTH_USER } from './mutation-types'

Vue.use(Vuex)

const state = {
  authUser: {},
  isAuth: false,
  jwt: localStorage.getItem('token')
}

const getters = {}

const mutations = {
  [SET_AUTH_USER] (state, { user, token }) {
    state.authUser = user
    state.isAuth = true
    state.jwt = token
  }
}

const actions = {
  login ({ commit }, data) {
    return Accounts.authUser(data).then(response => commit(SET_AUTH_USER, response))
  },
  createUser ({commit}, data) {
    return Accounts.create(data)
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
