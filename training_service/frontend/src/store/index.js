import Vue from 'vue'
import Vuex from 'vuex'
import { Accounts } from '../api/accounts'
import { SET_AUTH_USER, GET_GROUPS, SET_ERRORS } from './mutation-types'

Vue.use(Vuex)

const state = {
  jwt: localStorage.getItem('token'),
  groups: [],
  errors: []
}

const getters = {
  isAuth: state => !!state.jwt
}

const mutations = {
  [SET_AUTH_USER] (state, { user, token }) {
    localStorage.setItem('token', token)
  },
  [GET_GROUPS] (state, groups) {
    state.groups = groups
  },
  [SET_ERRORS] (state, errors) {
    state.errors = errors
  }
}

const actions = {
  login ({ commit }, data) {
    return Accounts.authUser(data).then(response => commit(SET_AUTH_USER, response.data))
  },
  createUser ({commit}, data) {
    let config = {
      headers: {
        'Authorization': 'JTW '.concat(state.jwt)
      }
    }
    return Accounts.create(data, config)
  },
  updateUser ({commit}, user, data, config) {
    return Accounts.update(user, data, config)
  },
  getGroups ({commit}, groups) {
    return Accounts.getGroups().then(response => commit(GET_GROUPS, response.data))
  },
  setErrors ({commit}, errors) {
    let errorsData = []
    for (let key in errors.response.data) {
      errors.response.data[key].forEach(element => {
        errorsData = [element, ...errorsData]
      })
    }
    commit(SET_ERRORS, errorsData)
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
