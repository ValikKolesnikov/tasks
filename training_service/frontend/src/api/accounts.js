import {HTTP} from './common'

export const Accounts = {
  create (data) {
    return HTTP.post('accounts/users/', data)
  },
  authUser (data) {
    return HTTP.post('accounts/tokens/obtain/', data)
  },
  update (user, data, config) {
    return HTTP.patch(`accounts/users/${user.id}/`, data, config)
  },
  getUser (data, config) {
    return HTTP.post(`accounts/users/current/`, data, config)
  }
}
