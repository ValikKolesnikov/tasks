import {HTTP} from './common'

export const Accounts = {
  create (data, config) {
    return HTTP.post('accounts/users/', data, config)
  },
  authUser (data) {
    return HTTP.post('accounts/tokens/obtain/', data)
  },
  update (user, data, config) {
    return HTTP.patch(`accounts/users/${user.id}/`, data, config)
  },
  getGroups () {
    return HTTP.get('accounts/groups/')
  },
  getUser (data) {
    return HTTP.post(`accounts/tokens/verify/`, data)
  }
}
