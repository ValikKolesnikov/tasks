import { Accounts } from '../../api/accounts'
import { SET_AUTH_USER, GET_GROUPS, SET_ERRORS, GET_USER } from '../mutation-types'

const state = {
  jwt: localStorage.getItem('token'),
  groups: [],
  errors: [],
  authUser: {}
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
  },
  [GET_USER] (state, { user }) {
    state.authUser = user
  }
}

const actions = {
  login ({ commit }, data) {
    return Accounts.authUser(data).then(response => commit(SET_AUTH_USER, response.data))
  },
  createUser ({commit}, data) {
    let config = {
      headers: {
        'Authorization': 'Bearer '.concat(state.jwt)
      }
    }
    return Accounts.create(data, config)
  },
  updateUser ({commit}, {user, data}) {
    let config = {
      headers: {
        'Authorization': 'Bearer '.concat(state.jwt)
      }
    }
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
  },
  getUser ({commit}, token) {
    return Accounts.getUser(token).then(response => commit(GET_USER, response.data))
  }
}

export default{
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
