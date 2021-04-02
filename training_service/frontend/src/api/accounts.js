import {HTTP} from './common'

export const Accounts = {
  create (data, config) {
    return HTTP.post('accounts/users/', data, config)
  },
  authUser (data) {
    return HTTP.post('accounts/tokens/obtain/', data)
  },
  update (data, config) {
    return HTTP.patch(`accounts/users/update_user/`, data, config)
  },
  getGroups () {
    return HTTP.get('accounts/groups/')
  },
  getUser (data, config) {
    return HTTP.post(`accounts/users/current/`, data, config)
  }
}
